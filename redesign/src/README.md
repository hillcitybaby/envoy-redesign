# Source

**These are the only files anyone edits.**

```
src/desktop.html     the desktop page
src/mobile.html      the mobile page
src/waitlist.html    the waitlist page
src/img/             hero photography
```

Everything in `build/` is generated and is overwritten on every run. Editing a
file there loses the change the next time anyone builds.

## Building

```
python redesign/build.py
```

That does three things:

1. **`_system/apply.py`** injects the design system into each source page,
   removes the local rules it supersedes, rewires the markup onto the system
   classes, and converts fixed heights, font sizes and spacing onto the scales.
   Output: `build/desktop.html`, `build/mobile.html`, `build/waitlist.html`.
2. **`build.py`** combines the desktop and mobile pages into one responsive
   page that switches at 768px. Output: `build/index.html`.
3. **`_system/check.mjs`** and **`_system/layout-check.mjs`** verify the result
   in headless Chrome and **fail the build** on any violation.

## Where to make a change

| You want to change | Edit |
|---|---|
| a colour, type size, spacing step, button | `_system/system.css` |
| a rule for one page only, or a breakpoint | `_system/apply.py` |
| copy, markup, structure | the matching file in `src/` |

Never edit `build/`.

## The rest of the folders

`00-brief` … `03-exploration` are the research phases. `07-buttons` and
`08-layout-audit` are the audit documents. `04-final/spec` holds the Figma
geometry dump, `05-mobile` holds the original Claude Design export and a device
preview. None of those are part of the build.
