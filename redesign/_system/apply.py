"""Roll the Envoy design system into every page.

system.css is the law. This script injects it into each page between markers,
deletes the local button declarations it supersedes, rewires the markup onto the
system classes, and folds the duplicate colours onto their canonical tokens.

    python redesign/_system/apply.py          # apply to the source pages
    python redesign/06-responsive/build.py    # rebuild the combined page

check.mjs then verifies the result and fails the build if anything drifts.
"""
import io, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SRC = ROOT / 'src'      # the only files anyone edits
OUT = ROOT / 'build'    # generated — overwritten on every run
START = '/* ==ENVOY-SYSTEM:START== */'
END = '/* ==ENVOY-SYSTEM:END== */'


def inject(css_text, system):
    block = START + '\n' + system + '\n' + END
    if START in css_text:
        return re.sub(re.escape(START) + r'.*?' + re.escape(END), lambda m: block, css_text, flags=re.S)
    return block + '\n' + css_text


def drop_rules(css, selectors):
    """Delete whole rules whose selector list exactly matches one we now own."""
    out, i, dropped = [], 0, []
    while i < len(css):
        brace = css.find('{', i)
        if brace == -1:
            out.append(css[i:]); break
        pre = css[i:brace]
        # don't walk into at-rules
        if pre.strip().startswith('@'):
            depth, j = 0, brace
            while j < len(css):
                if css[j] == '{': depth += 1
                elif css[j] == '}':
                    depth -= 1
                    if depth == 0: break
                j += 1
            out.append(css[i:j + 1]); i = j + 1; continue
        close = css.find('}', brace)
        sel = pre.strip()
        if sel in selectors:
            dropped.append(sel)
        else:
            out.append(css[i:close + 1])
        i = close + 1
    return ''.join(out), dropped


def apply_file(src, out, root_keep, drop, replacements, label, pre_css=(), post_css=''):
    import transforms
    s = io.open(src, encoding='utf-8').read()
    system = io.open(HERE / 'system.css', encoding='utf-8').read()

    head, css, tail = s[:s.index('<style>') + 7], s[s.index('<style>') + 7:s.index('</style>')], s[s.index('</style>'):]

    # remove any previous system block first, so re-running can't rewrite the system's own :root
    css = re.sub(re.escape(START) + r'.*?' + re.escape(END), '', css, flags=re.S)

    # the page keeps only its own layout tokens; every colour token comes from the system
    css = re.sub(r':root\{.*?\}', root_keep, css, count=1, flags=re.S)
    css, dropped = drop_rules(css, drop)

    # structural edits first, while the CSS still reads as it was authored
    for old, new in pre_css:
        if old not in css:
            print('  !! pre_css not found in %s: %s' % (label, old[:60]))
            continue
        css = css.replace(old, new)

    if post_css:
        css += post_css

    # then the systematic passes from the layout audit
    css, nh = transforms.heights_to_min(css)
    css, nt = transforms.type_to_scale(css)
    css, ns = transforms.spacing_to_scale(css)
    print('  %s: %d heights -> min-height, %d font sizes -> scale, %d spacing values -> scale'
          % (label, nh, nt, ns))

    css = inject(css, system)

    s = head + css + tail
    applied = []
    for old, new in replacements:
        if old not in s:
            print('  !! not found in %s: %s' % (label, old[:70]))
            continue
        s = s.replace(old, new)
        applied.append(old[:40])
    out.parent.mkdir(parents=True, exist_ok=True)
    nl = chr(10)
    banner = (nl.join(['<!-- GENERATED FILE — do not edit.',
                       '     Source: redesign/src/' + src.name,
                       '     Rebuild: python redesign/build.py -->']) + nl)
    s = s.replace('<!doctype html>', '<!doctype html>' + nl + banner, 1)
    io.open(out, 'w', encoding='utf-8').write(s)
    print('  %s: dropped %d superseded rules, applied %d rewrites' % (label, len(dropped), len(applied)))
    return dropped


# ----------------------------------------------------------------- desktop ---
DESK_DROP = {
    '.util a', '.util a:hover', '.btn-start', '.btn-start:hover',
    '.tier .cta', '.tier.pop .cta', '.biz-cta a', '.biz-cta .solid',
    '.biz-cta .solid:hover', '.biz-cta .outline', '.biz-cta .outline:hover',
}
DESK_REPL = [
    # --- markup onto the system -------------------------------------------
    ('<div class="util"><a href="#">', '<div class="util"><a class="btn btn-chip btn-sm" href="#">'),
    ('<button class="btn-start" type="submit">', '<button class="btn btn-primary btn-md" type="submit">'),
    ('<button class="go" type="button"', '<button class="btn-icon go" type="button"'),
    ('<article class="tier pop">', '<article class="tier pop on-dark">'),
    ('<a class="cta" href="#">Get started free</a>', '<a class="btn btn-secondary btn-md cta" href="#">Get started free</a>'),
    ('<a class="cta" href="#">Choose Pro</a>', '<a class="btn btn-primary btn-md cta" href="#">Choose Pro</a>'),
    ('<a class="cta" href="#">Choose Agency</a>', '<a class="btn btn-secondary btn-md cta" href="#">Choose Agency</a>'),
    ('<div class="biz">', '<div class="biz on-dark">'),
    ('<a class="solid" href="#">', '<a class="btn btn-primary btn-lg" href="#">'),
    ('<a class="outline" href="#pricing">', '<a class="btn btn-secondary btn-lg" href="#pricing">'),
    # --- what the page still owns: position, not appearance ----------------
    ('.go{position:absolute;left:284px;bottom:13px;width:34px;height:34px;border-radius:999px;border:0;cursor:pointer;\n'
     '  background:rgba(255,255,255,.94);color:var(--ink);display:inline-flex;align-items:center;justify-content:center}',
     '.go{position:absolute;left:278px;bottom:13px}  /* 40px icon button, right edge still 13px in */\n'
     '.states button:hover::before{background:#fff}'),
    ('.tiers{display:grid', '.tier .cta{margin-top:auto}\n.tiers{display:grid'),
    ('.skip:focus{top:10px}', '.skip:hover{background:var(--indigo-600)}\n.skip:focus{top:10px}'),
    ('.brand svg{', '.brand:hover{color:var(--indigo-600)}\n.brand svg{'),
    # the active dot is already white, so hovering it needs its own cue
    ('.states button:hover::before{background:#fff}',
     '.states button:hover::before{background:#fff}\n'
     '.states button[aria-selected="true"]:hover::before{background:var(--indigo-100)}'),
    # --- colour consolidation ---------------------------------------------
    ('linear-gradient(160deg,#1B1836,#0C1024);color:#EDECF7', 'linear-gradient(160deg,var(--biz),var(--ink));color:var(--on-dark)'),
    ('linear-gradient(150deg,#191735,#0C1024);color:#EDECF7', 'linear-gradient(150deg,var(--biz),var(--ink));color:var(--on-dark)'),
    ('.tier.pop li svg{color:#A79BFF}', '.tier.pop li svg{color:var(--indigo-200)}'),
    ('.biz-copy .rule-lab{color:#B3AEE8}', '.biz-copy .rule-lab{color:var(--on-dark-eyebrow)}'),
    ('.biz-copy>p{font-size:var(--t-body);line-height:1.6;color:#CBC9E2}', '.biz-copy>p{font-size:var(--t-body);line-height:1.6;color:var(--on-dark-muted)}'),
    ('border:1px solid #DAD8FB;', 'border:1px solid var(--line-2);'),
    ('rgba(8,10,22,.93) 0%,rgba(8,10,22,.76) 46%,rgba(8,10,22,.34) 72%,rgba(8,10,22,.0',
     'rgba(var(--shadow-ink),.93) 0%,rgba(var(--shadow-ink),.76) 46%,rgba(var(--shadow-ink),.34) 72%,rgba(var(--shadow-ink),.0'),
    ('background:rgba(10,13,32,.5);backdrop-filter', 'background:rgba(var(--shadow-ink),.5);backdrop-filter'),
    ('rgba(8,10,26,.35)', 'rgba(var(--shadow-ink),.35)'),
    ('rgba(8,10,26,.40)', 'rgba(var(--shadow-ink),.40)'),
]

# ------------------------------------------------------------------ mobile ---
MOB_DROP = {
    '.login', '.login:hover', '.start', '.start:hover',
    '.tier-cta', '.tier.open .tier-cta',
    '.biz-ctas a', '.biz-ctas .solid', '.biz-ctas .outline', '.biz-ctas .outline:hover',
    'footer nav a::after',
}
MOB_REPL = [
    ('<a class="login" href="#">Log in</a>', '<a class="btn btn-chip btn-sm login" href="#">Log in</a>'),
    ('<button class="start" type="submit">Start project</button>', '<button class="btn btn-primary btn-md start" type="submit">Start project</button>'),
    ('<section class="biz" id="business"', '<section class="biz on-dark" id="business"'),
    ('<div class="biz-ctas"><a class="solid" href="#">Join Envoy for Business</a><a class="outline" href="#pricing">See pricing</a></div>',
     '<div class="biz-ctas"><a class="btn btn-primary btn-lg" href="#">Join Envoy for Business</a><a class="btn btn-secondary btn-lg" href="#pricing">See pricing</a></div>'),
    ('<nav aria-label="Footer"><a href="#start">Start a project</a><a href="#pricing">Pricing</a><a href="#business">For business</a><a href="#">Privacy</a></nav>',
     '<nav aria-label="Footer"><a class="hit-extend" href="#start">Start a project</a><a class="hit-extend" href="#pricing">Pricing</a><a class="hit-extend" href="#business">For business</a><a class="hit-extend" href="#">Privacy</a></nav>'),
    # the decks are controls too, so they need a hover
    ('.deck{position:relative;cursor:pointer;', '.deck:hover{filter:brightness(1.06)}\n.deck{position:relative;cursor:pointer;'),
    ('.menu-btn i{', '.menu-btn:hover{background:var(--indigo-50)}\n.menu-btn i{'),
    ('.tier-head{width:100%',
     '.tier-head:hover{background:rgba(12,16,36,.06)}\n'
     '.tier.on-dark .tier-head:hover{background:rgba(255,255,255,.06)}\n'
     '.tier-head{width:100%'),
    # tier CTAs are generated — class them from the system
    ("var cta=el('a','tier-cta',t.cta); cta.href='#start'; body.appendChild(cta);",
     "var cta=el('a','btn btn-md tier-cta',t.cta); cta.href='#start'; body.appendChild(cta);"),
    ('tiersEl.appendChild(row); rows.push({t:t,row:row,head:head});',
     'tiersEl.appendChild(row); rows.push({t:t,row:row,head:head,cta:cta});'),
    ("function paintTiers(){ rows.forEach(function(r){ var o=r.t.id===open; r.row.classList.toggle('open',o); r.head.setAttribute('aria-expanded',o); }); }",
     "function paintTiers(){ rows.forEach(function(r){ var o=r.t.id===open;\n"
     "    r.row.classList.toggle('open',o); r.row.classList.toggle('on-dark',o);\n"
     "    r.cta.classList.toggle('btn-primary',o); r.cta.classList.toggle('btn-secondary',!o);\n"
     "    r.head.setAttribute('aria-expanded',o); }); }"),
    # colour consolidation
    ('linear-gradient(159deg,rgb(27,24,54) 0%,rgb(12,16,36) 77%);color:#EDECF7', 'linear-gradient(159deg,var(--biz) 0%,var(--ink) 77%);color:var(--on-dark)'),
    ('linear-gradient(115deg,rgb(25,23,53) 6%,rgb(12,16,36) 70%)', 'linear-gradient(115deg,var(--biz) 6%,var(--ink) 70%)'),
    ('var(--biz-eyebrow)', 'var(--on-dark-eyebrow)'),
    ('var(--biz-copy)', 'var(--on-dark-muted)'),
    ('var(--biz-foot)', 'var(--on-dark-muted)'),
    ('rgba(8,10,26,.5)', 'rgba(var(--shadow-ink),.5)'),
]

# --- structural fixes from the layout audit, applied before the generic passes ---
DESK_PRE = [
    # the features row needs 1418px and the business row 1460px before they fit
    # side by side, so each stacks at its own content-driven point instead of a
    # shared 1180 that leaves both broken for 240px
    ("""@media(max-width:1180px){
  .features{height:auto;flex-direction:column;align-items:flex-start;gap:40px;padding-block:64px}
  .feat-head{width:100%}
  .feat-head h2,.feat-head p{max-width:none}
  .biz{flex-direction:column;align-items:flex-start;gap:40px;padding:44px}
  .biz-copy{width:100%}
  .biz .rail{width:100%}
}""",
     """@media(max-width:1420px){
  .features{height:auto;flex-direction:column;align-items:flex-start;gap:40px;padding-block:64px}
  .feat-head{width:100%}
  .feat-head h2,.feat-head p{max-width:none}
  .feat-head p{max-width:var(--measure)}
}
@media(max-width:1460px){
  .biz{flex-direction:column;align-items:flex-start;gap:40px;padding:44px}
  .biz-copy{width:100%}
  .biz .rail{width:100%}
  .biz-copy>p{max-width:var(--measure)}
}"""),
    # body copy keeps a comfortable measure once a column goes full width
    (".pr-head p{font-size:16px;line-height:1.6;color:var(--muted);max-width:448px}",
     ".pr-head p{font-size:16px;line-height:1.6;color:var(--muted);max-width:min(448px,var(--measure))}"),
]
MOB_PRE = [
    # the composer filled 369px regardless of the page, so it was cramped under
    # 390 and undersized above 414
    ("display:flex;align-items:center;gap:8px;padding:14px 10px 14px 18px;width:min(369px,100%);height:75px}",
     "display:flex;align-items:center;gap:8px;padding:14px 10px 14px 18px;width:100%;height:75px}"),
    (".lede{margin:18px 0 0;font-size:16px;line-height:1.55;color:var(--muted);max-width:320px}",
     ".lede{margin:18px 0 0;font-size:16px;line-height:1.55;color:var(--muted);max-width:min(320px,var(--measure))}"),
]

# appended last so it wins over the base .composer rules
MOB_POST = """
/* Under 400px the button goes full width beneath the field: the label survives
   and the target becomes a comfortable 44px across. */
@media(max-width:399px){
  .composer{flex-direction:column;align-items:stretch;height:auto;min-height:0;gap:10px;padding:14px}
  .composer textarea{height:auto;min-height:44px}
  .composer .start{width:100%}
}
/* A reader's own text-spacing settings must never cost content (WCAG 1.4.12). */
.composer textarea{min-height:52px;height:auto;overflow:auto}
"""



# The hero card is an absolutely positioned block with a percentage height, so it
# is tight from about 940px up. Reflowing it at 1100 instead of 900 removes that
# band entirely — a content-driven breakpoint rather than a round number.
HERO_REFLOW = """@media(max-width:1100px){
  /* Tablet: the stage becomes the white container. The photo is cropped to the
     same 1372:830 frame the desktop uses — so the tooltip percentages still land
     on the right part of the picture — and the copy and the conversation starter
     sit beneath it inside the same card. */
  .stage{aspect-ratio:auto;background:var(--card);border-radius:38px;overflow:hidden;
    padding:8px;box-shadow:0 30px 70px -24px rgba(8,10,26,.35)}
  .photo{position:relative;inset:auto;aspect-ratio:1372/830;border-radius:30px;overflow:hidden}
  .photo img{width:auto;height:100%;left:50%!important;top:0!important;transform:translateX(-50%)}
  /* the tooltip layer sits exactly over the photo, in the same proportions */
  .tips{left:8px;right:8px;top:8px;bottom:auto;aspect-ratio:1372/830}
  /* each tooltip scales from its own anchor, so it keeps pointing at the same
     spot in the picture as everything shrinks */
  .tips .tip{transform:scale(.62);transform-origin:top left}
  .util{top:22px;right:22px}
  .states{left:22px;right:auto;bottom:auto;top:22px}
  .overlay{position:static;width:auto;height:auto;min-height:0;background:transparent;
    box-shadow:none;margin:0;padding:var(--sp-5) var(--sp-3) var(--sp-3)}
  .ov-copy{padding-top:0;gap:var(--sp-5)}
  .ov-mid{height:auto;min-height:0;display:block}
  .ov-mid h1{font-size:clamp(1.8rem,5.2vw,2.5rem);max-width:none}
  .ov-lede{font-size:16px;max-width:var(--measure);margin-top:16px}
  /* the tooltip layer is aria-hidden, so the chips stay for screen readers —
     visually hidden rather than removed, or the vendor counts are lost here */
  .tipchips{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
}
@media(max-width:880px){
  .tips .tip{transform:scale(.5)}
}
@media(max-width:900px){
  .tier{height:auto}"""

DESK_PRE.append((
    ".rail,.biz .rail{height:auto;display:grid;grid-template-columns:1fr;gap:12px;width:100%}",
    ".rail,.biz .rail{height:auto;display:grid;grid-template-columns:1fr;gap:12px;width:100%;overflow:visible}"))

HERO_ANCHOR = "@media(max-width:900px){" + chr(10) + "  .tier{height:auto}"
DESK_PRE.append((HERO_ANCHOR, HERO_REFLOW))

# The 900 block carried its own copy of the hero reflow. The 1100 block above now
# owns the whole tablet range, so those lines are removed rather than left to
# override it between 768 and 900.
for _dead in [
    "  .stage{aspect-ratio:auto;border-radius:0;background:transparent;overflow:visible}\n",
    "  .photo{position:relative;inset:auto;aspect-ratio:16/11;border-radius:30px;overflow:hidden}\n",
    "  .tips{display:none}\n",
    "  .overlay{position:static;width:auto;height:auto;margin:-34px 8px 0;box-shadow:0 20px 50px -34px rgba(8,10,26,.5)}\n",
    "  .ov-copy{padding-top:24px;gap:26px}\n",
    "  .ov-mid{height:auto;display:block}\n",
    "  .ov-mid h1{font-size:clamp(1.8rem,7vw,2.5rem);max-width:none}\n",
    "  .ov-lede{font-size:16px;max-width:none;margin-top:16px}\n",
    "  .util{top:14px;right:14px}\n",
    "  .states{right:auto;left:14px;bottom:auto;top:14px}\n",
    "  .tipchips{display:flex;flex-wrap:wrap;gap:7px;margin-top:16px;padding:0;list-style:none}\n",
]:
    DESK_PRE.append((_dead, ""))



# --- waitlist CTA wiring — DISABLED. The waitlist page still builds and is
#     reachable at /waitlist.html, but nothing on the landing page links to it.
#     Set WAITLIST_LINKED = True to wire every call to action back up.
WAITLIST_LINKED = False

if WAITLIST_LINKED:
    DESK_REPL += [
        ('<a class="btn btn-secondary btn-md cta" href="#">Get started free</a>',
         '<a class="btn btn-secondary btn-md cta" href="waitlist.html">Get started free</a>'),
        ('<a class="btn btn-primary btn-md cta" href="#">Choose Pro</a>',
         '<a class="btn btn-primary btn-md cta" href="waitlist.html">Choose Pro</a>'),
        ('<a class="btn btn-secondary btn-md cta" href="#">Choose Agency</a>',
         '<a class="btn btn-secondary btn-md cta" href="waitlist.html">Choose Agency</a>'),
        ('<a class="btn btn-primary btn-lg" href="#">Join Envoy for Business</a>',
         '<a class="btn btn-primary btn-lg" href="waitlist.html?business=1">Join Envoy for Business</a>'),
        ('<a href="#">Start a project</a>', '<a href="waitlist.html">Start a project</a>'),
        ("document.getElementById('finder').addEventListener('submit',function(e){ e.preventDefault(); proj.focus(); });",
         "document.getElementById('finder').addEventListener('submit',function(e){ e.preventDefault(); location.href='waitlist.html'; });"),
    ]
    MOB_REPL += [
        ('<a class="btn btn-primary btn-lg" href="#">Join Envoy for Business</a>',
         '<a class="btn btn-primary btn-lg" href="waitlist.html?business=1">Join Envoy for Business</a>'),
        ("var cta=el('a','btn btn-md tier-cta',t.cta); cta.href='#start';",
         "var cta=el('a','btn btn-md tier-cta',t.cta); cta.href='waitlist.html';"),
        ('<a href="#start" data-close>Start a project</a>', '<a href="waitlist.html" data-close>Start a project</a>'),
        ('<a class="hit-extend" href="#start">Start a project</a>', '<a class="hit-extend" href="waitlist.html">Start a project</a>'),
        ("document.getElementById('start').addEventListener('submit',function(e){ e.preventDefault(); proj.focus(); });",
         "document.getElementById('start').addEventListener('submit',function(e){ e.preventDefault(); location.href='waitlist.html'; });"),
    ]



if __name__ == '__main__':
    print('applying the system  src/ -> build/')
    apply_file(SRC / 'desktop.html', OUT / 'desktop.html',
               ':root{ --pad:34px }', DESK_DROP, DESK_REPL, 'desktop', DESK_PRE)
    MOB_ROOT = chr(10).join([
        ':root{',
        '  --inset-top:calc(env(safe-area-inset-top,0px) + 18px);',
        '  --inset-bottom:max(12px, calc(env(safe-area-inset-bottom,0px) + 6px));',
        '}'])
    apply_file(SRC / 'mobile.html', OUT / 'mobile.html',
               MOB_ROOT, MOB_DROP, MOB_REPL, 'mobile', MOB_PRE, MOB_POST)
    apply_file(SRC / 'waitlist.html', OUT / 'waitlist.html',
               ':root{ --pad:34px }', set(), [], 'waitlist')
