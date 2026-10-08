"""Systematic CSS transforms applied by apply.py.

These implement the layout audit:
  1. every structural fixed height becomes min-height (WCAG 1.4.12)
  2. every font-size becomes a scale token (rem, so it follows the reader's setting)
  3. rhythmic spacing snaps to the 4px scale
  4. body copy in stacked layouts gets a comfortable measure

Load-bearing geometry is deliberately left alone: the panel strides, tooltip
offsets, composer internals and icon positions come from the design frames and
are what make the overlap and the stacked cards line up.
"""
import re

# --- 1. heights -------------------------------------------------------------
# selectors whose height is a genuine graphic dimension, not a content box
HEIGHT_KEEP = ('svg', '::before', '::after', '.go', '.btn-icon', '.menu-btn i',
               '.sr', 'label', '.states', '.eyebrow i', '.menu-btn', '.art')

def heights_to_min(css):
    out, n = [], 0
    for part in re.split(r'(\}|\{)', css):
        out.append(part)
    text = css
    def repl(m):
        nonlocal n
        sel, body = m.group(1), m.group(2)
        if any(k in sel for k in HEIGHT_KEEP):
            return m.group(0)
        new = re.sub(r'(?<![-\w])height\s*:\s*(\d+)px', lambda x: 'min-height:%spx' % x.group(1), body)
        # a breakpoint that releases a fixed height must release the minimum too,
        # otherwise the min-height we just introduced keeps applying there
        new = re.sub(r'(?<![-\w])height\s*:\s*auto\s*!important',
                     'height:auto!important;min-height:0!important', new)
        new = re.sub(r'(?<![-\w])height\s*:\s*auto(?!\s*!important)(?![-\w])',
                     'height:auto;min-height:0', new)
        if new != body: n += 1
        return sel + '{' + new + '}'
    text = re.sub(r'([^{}]+)\{([^{}]*)\}', repl, text)
    return text, n

# --- 2. type ----------------------------------------------------------------
TYPE_MAP = [
    (44, '--t-display'), (41, '--t-display'), (40, '--t-display'),
    (38, '--t-h1'), (36, '--t-h1'), (34, '--t-h1'), (30, '--t-h1'),
    (26, '--t-h2'), (24, '--t-h2'), (22, '--t-h2'), (21.6, '--t-h2'),
    (18, '--t-lead'), (17, '--t-lead'),
    (16, '--t-body'), (15, '--t-body'),
    (14, '--t-ui'), (13.5, '--t-ui'),
    (13, '--t-small'), (12.5, '--t-small'), (12, '--t-small'),
    (11, '--t-micro'), (10.5, '--t-micro'), (10, '--t-micro'),
    (220, '--t-ghost-xl'), (150, '--t-ghost-l'), (130, '--t-ghost-l'),
    (120, '--t-ghost-l'), (98, '--t-ghost-m'), (96, '--t-ghost-m'), (72, '--t-ghost-m'),
]
def type_to_scale(css):
    n = 0
    def repl(m):
        nonlocal n
        v = float(m.group(1))
        for size, tok in TYPE_MAP:
            if abs(size - v) < 0.01:
                n += 1
                return 'font-size:var(%s)' % tok
        return m.group(0)
    css = re.sub(r'font-size\s*:\s*([\d.]+)px', repl, css)
    return css, n

# --- 3. spacing -------------------------------------------------------------
SCALE = [(4, '--sp-1'), (8, '--sp-2'), (12, '--sp-3'), (16, '--sp-4'),
         (24, '--sp-5'), (32, '--sp-6'), (40, '--sp-7'), (56, '--sp-8'), (80, '--sp-9')]
def snap(v):
    return min(SCALE, key=lambda s: abs(s[0] - v))

# only these carry rhythm; everything else is structural geometry
SPACING_OK = ('.about', '.features', '.pricing', '.biz-sec', '.shell', 'footer',
              '.pr-panel', '.pr-head', '.tiers', '.tier', '.biz', '.biz-copy',
              '.feat-head', '.about-stmt', '.stmt', '.lede', '.micro', '.menu',
              '.top', '.nav', '.eyebrow', '.pr-sub', '.h-36', 'h1', 'h2', 'h3', '.sec')
SPACING_SKIP = ('.rail', '.cell', '.stack', '.ghost', '.lab', '.cap', '.card', '.deck',
                '.tip', '.go', '.states', '.composer', '.comp', '.dock', '.overlay',
                '.ov-', '.brand', '.util', '.marquee', '.wm', '.hit-extend', '.badge',
                '.ptag', '.photo', '.stage', '.tips', '.scrim', '.menu-btn', '.btn',
                '.tier-cta', '.tier-head', '.tier-name', '.tier-price', '.tier-body',
                '.biz-ctas', '.biz-cta', '.tipchips', '.skip', '.login', '.start')
def spacing_to_scale(css):
    n = 0
    def rule(m):
        nonlocal n
        sel, body = m.group(1), m.group(2)
        if any(k in sel for k in SPACING_SKIP): return m.group(0)
        if not any(k in sel for k in SPACING_OK): return m.group(0)
        def decl(d):
            nonlocal n
            prop, val = d.group(1), d.group(2)
            if 'var(' in val or 'calc(' in val or 'clamp(' in val: return d.group(0)
            def num(x):
                nonlocal n
                v = float(x.group(1))
                if v == 0: return x.group(0)
                if v > 100: return x.group(0)          # functional clearance, left alone
                tok = snap(v)
                n += 1
                return 'var(%s)' % tok[1]
            return prop + ':' + re.sub(r'(?<![\w-])([\d.]+)px', num, val)
        body = re.sub(r'(?<![-\w])(margin|padding|gap|row-gap|column-gap)\s*:\s*([^;}]+)', decl, body)
        return sel + '{' + body + '}'
    return re.sub(r'([^{}]+)\{([^{}]*)\}', rule, css), n
