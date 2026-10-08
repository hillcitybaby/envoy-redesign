# Moodboard — direction the references collectively point toward

Guidance, not law. Written to be argued with at Checkpoint 2.

---

## The one-line read

**Warm, calm, and evidence-led — a page that looks like the product it's selling.**

The references don't converge on an aesthetic so much as on a *posture*. The sites that solve Envoy's problems (Wise, Thumbtack, Linear, Zola) all share one trait: **they show you something true instead of telling you something flattering.** That's the through-line, and it's more important than any palette decision below.

---

## The strongest single argument, before any taste enters

The current landing page is a near-black field with an electric-blue WebGL shader. **The product it sells is white, soft-blue and friendly** (`01-current-state/product/demo-07-login-full.png`). Warming the page isn't a preference — it's a correction. Right now every visitor who converts walks from a dark, technical marketing site into a light, calm app and experiences a small jolt of "wait, is this the same product?"

So: the redesign moves toward the app, not away from it. That reframes your friend's note — "make it less masculine and technical" isn't a request to abandon the brand, it's a request to make the front door match the house.

---

## Tone

Where the register should sit, on a line from Thumbtack to Zola:

```
Thumbtack ──────────────── ★ ──────── Zola ─────── The Knot
utilitarian            HERE       warm/plural      bridal
```

Slightly warmer than the midpoint, well short of anything bridal. Envoy has to say *"a 1920s kitchen renovation"* and *"an outdoor wedding for 150"* in the same breath without either sounding out of place — which rules out the bridal end absolutely, and rules out the procurement end just as firmly.

Concretely:
- **Contractions, always.** "You're", "we'll", "it's". The current page already does this and it's the warmest thing about it.
- **Second person, present tense.** The reader is doing the project, not evaluating a category.
- **Name real things.** Venue, caterer, florist, photographer, general contractor, cabinetmaker. Not "providers across every trade and category."
- **The banned list**, from the audit: `commercial build-outs`, `multi-vendor project`, `project hub`, `AV`, `trades and industries`, `service providers`. Every one of these is technically accurate and every one is why the page feels the way it feels.
- **CTA voice:** Zola's "Let's do this!" is the register; "Join the waitlist" is not. Somewhere in between — an invitation, not a form submission.
- **Keep, verbatim:** *"Projects fail in the messy middle."* *"Not post-and-wait."* *"You're in control."* *"Delegate outreach without losing your voice."* *"Email me this lineup to finish later."* These are the best sentences available and four of the five are already written.

---

## Density

**Medium, and variable — the opposite of the current page.**

Today every section is one heading, one paragraph, one list, on its own full screen: uniformly sparse and therefore uniformly weightless. The references that work are *rhythmic* — Linear alternates image-dense and text-dense; Stripe alternates wide bands and tight grids. Rest comes from contrast, not from emptiness.

- Free scroll. **Kill `scroll-snap` entirely** — it's the direct cause of the skimming problem, the overflow bug, and the redundancy.
- Aim for **6–7 bands** on a continuously scrollable page, roughly half the current vertical length.
- One section should be visibly the densest thing on the page — the vendor lineup — and it should earn that by being the most informative.
- Tiles for the case studies and vendor categories; stacked prose only where an argument genuinely needs sentences.

---

## Type

**Introduce a serif for display. Keep Instrument Sans for everything else.**

This is the highest-leverage single change to the "masculine and technical" problem. Zola sets its hero in a large serif; The Knot and Joy both use serif display. A geometric sans at 700 weight with `-0.03em` tracking — Envoy's current headline style — is the house style of developer tools, and no colour change will undo that on its own.

- **Display/headlines:** a warm transitional or old-style serif. Candidates on Google Fonts: **Fraunces** (has an optical-size axis and real character — first choice), **Instrument Serif** (pairs by name and by design with the existing sans, so it's the conservative pick), **Source Serif 4** (the safe, quiet option).
- **Body, UI, labels:** **Instrument Sans**, unchanged. It's a good face and it's already the brand.
- Loosen the display tracking from `-0.03em` toward `-0.01em`; the tight tracking is part of the technical read.
- Keep the size range roughly as-is (~52px display max) — the problem was never scale.
- Fewer, more decisive steps: the current 9 sizes can become about 6.

**If the founder rejects a serif outright**, the fallback is Instrument Sans at 600 rather than 700 with looser tracking and a lighter ground. Less effective, still directionally right.

---

## Colour temperature

**Keep the blue as the brand. Move it from electric to considered. Add exactly one warm accent.**

`#003fb3` and `#7191f7` stay identifiable but should stop being the *entire* system. The current palette is one hue with no warm tone anywhere, which is a large part of the coldness.

- **Ground: light.** White or a warm off-white (`#FBF9F6`-ish), matching the app. This is the single biggest change and it should be argued explicitly — see Direction A/B/C at Phase 4, where at least one direction should test keeping a dark treatment for the hero only.
- **Primary: the existing blue**, possibly warmed a step and used for actions and accents rather than as a field.
- **One warm accent** — terracotta, clay, warm sand, or a muted amber — for eyebrows, highlights, the "Envoy" vendor badge, and small emphasis. One accent, used sparingly, does an enormous amount of temperature work.
- **Ink: a warm near-black**, not the current cold `#061228`.
- **The shader:** as-is, it's 353 KB gzipped, ships React, and is the direct cause of measured 1.26:1 contrast. It should not survive in its current form. If the atmosphere is worth keeping — and it may be, it's genuinely distinctive and it's what the founder's link looks like today — keep it as **a small, static or CSS-only gradient moment in the hero only, with text never sitting on top of the volatile region.** Never behind body copy.

---

## Imagery

**The page needs pictures, and there are three honest kinds available.**

1. **Product UI** — the vendor lineup with its per-category rationale sentences. The most persuasive asset Envoy has and it has never appeared on the site. Because the demo's vendor data is synthetic and visibly inconsistent (an Austin wedding returning Brooklyn venues), this gets **rebuilt as a faithful HTML component with clearly illustrative content**, never a screenshot passed off as a live result.
2. **Category photography** — venue, catering, florals, a kitchen mid-renovation. The Knot's move, and the cheapest way to make "vendors" mean something instantly. Licensable, unlike anything else here. Must span project types, or it becomes a wedding page by the back door.
3. **The draft email** — one real-looking outreach message with a visible approve control. This is the trust artifact (see S1), and it is far more convincing than any security sentence.

**No stock photography of people in offices. No abstract 3D. No AI-generated imagery presented as real.**

---

## Motion

The current page's motion instincts are good — the staggered reveals are tasteful and `prefers-reduced-motion` is properly handled. Keep that discipline, reduce the quantity.

- Keep: gentle staggered entrances, honoured reduced-motion.
- Cut: the skewed button wipe (fussy), the mandatory scroll-snap, the fixed footer slide-up (it hides the footer from anyone who doesn't scroll to the exact end).
- Consider: one purposeful animated moment — the lineup assembling — because it *is* the product's argument. One demonstration beats five decorations.

---

## What to carry forward from the current design

Not a rebrand. These stay:

- **Instrument Sans** for body and UI.
- **The blue**, re-roled from field to accent.
- **The wordmark and the geometric mark** — distinctive and the founder's; note the logo is currently a CSS `mask-image`, so it inherits its colour and will need a real asset on a light ground.
- **The narrative skeleton** — problem → what it is → how it works → why not the alternative → who it's for → act. It's sound; it needs compression, not replacement.
- **The best sentences**, listed under Tone.
- **The accessibility discipline** — visible focus rings and reduced-motion support are already right. Add the contrast fix.

---

## Anti-goals

- **Bridal.** No script fonts, no blush-and-gold, no floral flourishes. It would break the kitchen renovation instantly and would misrepresent a horizontal product.
- **Generic SaaS.** Purple gradient, three icon cards, a logo wall we don't have. If a direction could be any B2B product with the logo swapped, it has failed the brief.
- **Enterprise-serious.** Compliance badges, "platform," "solutions." Wrong audience entirely.
- **Sparse-as-a-substitute-for-hierarchy.** The current page's failure mode. Empty space that doesn't direct attention is just empty.
- **Fake proof.** No invented testimonials, counts, ratings or logos, and no reuse of the demo's mock "Maya R." quote or its 48h / 4× statistics. Placeholders stay visibly labelled.
