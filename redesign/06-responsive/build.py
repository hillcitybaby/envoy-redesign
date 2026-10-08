"""Combine the desktop build (04-final) and the mobile build (05-mobile) into one responsive page.

Both source pages are pixel-matched to different design files (Figma desktop frames and the
Claude Design mobile screen), so their markup is kept intact rather than blended. Each page's
CSS is scoped to its own container (.vd desktop, .vm mobile), mobile IDs are prefixed with m-,
and a media query decides which view is shown:

    < 768px   mobile design   (.vm)
    >= 768px  desktop design  (.vd, with its own 1180/900 tablet reflows)

Edit the source pages, then re-run:   python redesign/06-responsive/build.py
"""
import re, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
DESK = HERE.parent / '04-final' / 'index.html'
MOB = HERE.parent / '05-mobile' / 'index.html'
BREAK = 768


def parts(html):
    head = html[:html.index('<style>')]
    css = html[html.index('<style>') + 7: html.index('</style>')]
    body = html[html.index('<body>') + 6: html.rindex('<script>')]
    js = html[html.rindex('<script>') + 8: html.rindex('</script>')]
    return head, css, body, js


# ---------- CSS scoping ----------
def split_top(css):
    """Split a stylesheet into top-level chunks: ('rule', prelude, body) or ('at', text)."""
    out, i, n = [], 0, len(css)
    while i < n:
        if css.startswith('/*', i):
            j = css.index('*/', i) + 2
            out.append(('raw', css[i:j])); i = j; continue
        if css[i].isspace():
            j = i
            while j < n and css[j].isspace(): j += 1
            out.append(('raw', css[i:j])); i = j; continue
        # read prelude up to '{' or ';'
        j, depth = i, 0
        while j < n and not (css[j] in '{;' and depth == 0):
            if css[j] == '(': depth += 1
            elif css[j] == ')': depth -= 1
            j += 1
        if j >= n: out.append(('raw', css[i:])); break
        pre = css[i:j]
        if css[j] == ';':
            out.append(('raw', css[i:j + 1])); i = j + 1; continue
        k, depth = j + 1, 1
        while depth:
            if css[k] == '{': depth += 1
            elif css[k] == '}': depth -= 1
            k += 1
        out.append(('rule', pre, css[j + 1:k - 1])); i = k
    return out


def split_selectors(pre):
    sels, cur, depth = [], '', 0
    for ch in pre:
        if ch == '(': depth += 1
        elif ch == ')': depth -= 1
        if ch == ',' and depth == 0: sels.append(cur); cur = ''
        else: cur += ch
    sels.append(cur)
    return [s.strip() for s in sels]


def scope_selector(sel, scope, decls):
    if sel == ':root': return scope
    if sel == ':root.framed':  # mobile preview mode: tokens scoped, scrollbar hiding stays global
        return ':root.framed ' + scope if '--' in decls else sel
    if sel.startswith(':root.framed::') or sel == 'html': return sel
    if sel == 'body': return scope
    if sel.startswith('body'): return scope + sel[4:]
    return scope + ' ' + sel


def scope_css(css, scope):
    out = []
    for c in split_top(css):
        if c[0] == 'raw': out.append(c[1]); continue
        _, pre, body = c
        p = pre.strip()
        if p.startswith('@media') or p.startswith('@supports'):
            out.append(pre + '{' + scope_css(body, scope) + '}')
        elif p.startswith('@'):  # @keyframes, @font-face: leave untouched
            out.append(pre + '{' + body + '}')
        else:
            sels = split_selectors(p)
            if sels == ['body']:
                # the page's body rule now styles its container; overflow-x:hidden on a
                # non-root element would create a scroll container, so use clip instead
                body = body.replace('overflow-x:hidden', 'overflow-x:clip')
            out.append(','.join(scope_selector(s, scope, body) for s in sels) + '{' + body + '}')
    return ''.join(out)


# ---------- mobile ID prefixing ----------
def prefix_mobile_ids(body, js):
    ids = sorted(set(re.findall(r'\bid="([^"]+)"', body)), key=len, reverse=True)
    for i in ids:
        body = re.sub(r'(\b(?:id|for|aria-controls|aria-describedby|aria-labelledby)=")' + re.escape(i) + '"', r'\1m-' + i + '"', body)
        body = body.replace('href="#' + i + '"', 'href="#m-' + i + '"')
        js = js.replace("getElementById('" + i + "')", "getElementById('m-" + i + "')")
        js = js.replace('a[href="#' + i + '"]', 'a[href="#m-' + i + '"]')
    js = js.replace("'tier-'+t.id", "'m-tier-'+t.id")
    return body, js, ids


def main():
    d_head, d_css, d_body, d_js = parts(DESK.read_text(encoding='utf-8'))
    _, m_css, m_body, m_js = parts(MOB.read_text(encoding='utf-8'))
    m_body, m_js, ids = prefix_mobile_ids(m_body, m_js)
    for i in ids:  # ID selectors in the mobile stylesheet must follow the rename (e.g. #pricing{margin-top:80px})
        m_css = re.sub(r'#' + re.escape(i) + r'(?![\w-])', '#m-' + i, m_css)

    head = d_head.replace('content="width=device-width, initial-scale=1"',
                          'content="width=device-width, initial-scale=1, viewport-fit=cover"')
    head = head.replace('<link rel="preconnect" href="https://fonts.googleapis.com">',
                        '<meta name="theme-color" content="#F4F5FC">\n<link rel="preconnect" href="https://fonts.googleapis.com">', 1)

    switch = f"""
/* ================= view switch ================= */
.vd[hidden],.vm[hidden]{{display:none!important}}
@media (max-width:{BREAK - 0.02}px){{ .vd{{display:none!important}} }}
@media (min-width:{BREAK}px){{ .vm{{display:none!important}} }}
html,body{{background:#EAECFA}}   /* one ground for both views */
body{{margin:0}}
"""
    page = (head
            + '<style>\n/* ================= desktop (04-final), scoped to .vd ================= */'
            + scope_css(d_css, '.vd')
            + '\n/* ================= mobile (05-mobile), scoped to .vm ================= */'
            + scope_css(m_css, '.vm')
            + switch + '</style>\n</head>\n<body>\n'
            + '<div class="vd">' + d_body + '</div>\n\n'
            + '<div class="vm">' + m_body + '</div>\n\n'
            + '<script>\n/* desktop */' + d_js + '</script>\n'
            + '<script>\n/* mobile */' + m_js + '</script>\n'
            + f"""<script>
/* Only one view is ever live: the other is hidden from assistive tech and the tab order. */
(function(){{
  var vd=document.querySelector('.vd'), vm=document.querySelector('.vm'), mq=matchMedia('(min-width:{BREAK}px)');
  function sync(){{ var desk=mq.matches; vd.hidden=!desk; vd.inert=!desk; vm.hidden=desk; vm.inert=desk; }}
  (mq.addEventListener?mq.addEventListener('change',sync):mq.addListener(sync)); sync();
}})();
</script>
</body>
</html>
""")
    (HERE / 'index.html').write_text(page, encoding='utf-8')
    wl = HERE.parent / '09-waitlist' / 'waitlist.html'
    if wl.exists():
        shutil.copy(wl, HERE / 'waitlist.html')
        print(f'copied waitlist.html ({wl.stat().st_size:,} bytes)')

    src_img, dst_img = DESK.parent / 'img', HERE / 'img'
    shutil.copytree(src_img, dst_img, dirs_exist_ok=True)
    print(f'wrote {HERE / "index.html"} ({len(page):,} bytes); mobile ids prefixed: {", ".join(ids)}')

    # the design system is not advisory — a page that breaks it does not ship
    import subprocess
    failed = False
    for name in ('check.mjs', 'layout-check.mjs'):
        check = HERE.parent / '_system' / name
        if not check.exists():
            continue
        r = subprocess.run(['node', str(check)], capture_output=True, text=True)
        print(r.stdout.strip() or r.stderr.strip())
        failed = failed or r.returncode != 0
    if failed:
        raise SystemExit('\nBUILD REJECTED — the page breaks the design system. '
                         'Fix the violations above, or change redesign/_system/system.css if the law itself should change.')


if __name__ == '__main__':
    main()
