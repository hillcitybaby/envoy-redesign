# Exploration prompt — Envoy landing page

*Phase 4. This is the instruction set for the three builds. It synthesizes the approved brief, the inventory contract, the reference library, the moodboard, and every ruling made at Checkpoints 1–2. Where this document conflicts with anything earlier, this document wins.*

---

## 1. Value proposition

> **Describe your project once. Envoy lines up the right vendors and writes the outreach — you approve every send.**

Sharpest wording the research supports, and every clause is defensible: the plain-language input exists, the reasoned category-by-category lineup exists, drafted email exists, and *"awaiting approval before sending"* is a real state in the product.

Supporting frame, for subheads and the meta description — adapted from the demo's own (sanctioned) meta description, softened per the tier ruling:

> Envoy finds the vendors your project needs, drafts the emails, and keeps every reply in one place. Free to plan.

**Deliberately not claimed** (see §6): SMS, phone calls, and fully autonomous outreach.

---

## 2. Audience and the primary action

**Audience.** Someone running a high-stakes, deadline-fixed, multi-category project — a wedding, a renovation, an offsite — usually for the first and only time, without a professional coordinator. High stakes, low tooling sophistication. They are not evaluating software; they are trying to stop feeling behind. They arrive cold from a friend's link or a founder's post, with borrowed trust and zero context.

**The job:** *"stop me from losing track, and make me feel like I'm running this instead of drowning in it."*

**Primary action — one, and only one:**

> **Start a project — type it into the hero field. Free, no card.**

Every other action on the page is secondary and must visibly recede: `Log in`, `Pricing`, `For pros`, `Email me this lineup to finish later`.

**The waitlist is dead.** Per the Checkpoint-3 ruling the product is live. No "Join the waitlist" copy, no Fillout link, anywhere. This removes the current site's only CTA and replaces it with a lower-friction, higher-value one.

---

## 3. The three problems, paired with the patterns that solve them

### Problem 1 — Abstract where it should be concrete, and written in procurement English

*Re-stated per the Checkpoint-1 ruling: we stay horizontal. Abstraction, not breadth, is what makes the page cold.*

| Pattern | From | Applied as |
|---|---|---|
| Hero is an input, not a claim | **Thumbtack** | The project-description field is the hero element. The visitor supplies the specificity the page can't. |
| Two-layer structure — abstract-but-warm promise up top, concrete worked examples below | **Notion** | Headline stays true for everyone; the case-study band gets specific for someone. The headline never has to hedge. |
| Serif + human photograph + contractions | **Zola** | The register. CTA voice is an invitation, not a form submission. |
| Name the artifact the visitor receives | **Joy** | "A vendor lineup and drafted emails" — checkable, unlike "a project hub." |

**Banned vocabulary, absolute:** `multi-vendor project`, `commercial build-outs`, `project hub`, `AV`, `trades and industries`, `service providers`, `providers`, `Join the waitlist`. Say venue, caterer, florist, photographer, general contractor, cabinetmaker.

### Problem 2 — Tells, never shows; no reason to believe

| Pattern | From | Applied as |
|---|---|---|
| Product UI carries the page (~60/40 image to text) | **Linear** | The lineup and the Canvas are rebuilt as real HTML components and given the most vertical space on the page. |
| Vendor categories as pictures, not words | **The Knot** | Category imagery so "vendors" means something in one second. |
| Enacted scenario rather than described capability | **Superhuman** | The lineup assembles in response to the visitor's own input. |
| A reserved proof slot, placed after comprehension | **Stripe** | An explicit, visibly-labelled `[PROOF — TBD]` band mid-page. Empty on purpose, so the absence is legible to the founder. |

### Problem 3 — Seven full-screen slides forbid scanning

| Pattern | From | Applied as |
|---|---|---|
| Numbered sections as a visible skim rail | **Linear** | A visible spine; alternating text-dense and image-dense bands as the replacement for scroll-snap. |
| Modular, independently comprehensible bands | **Stripe** | Free scroll. Read top-to-bottom, or jump to the band that answers your question. |
| Tiles as scan targets | **Thumbtack** | Case studies and vendor categories as tiles, not stacked lists. |

**`scroll-snap` is removed entirely.** It causes the skimming failure, the overflow bug that hides the trust sentence, and the section 3/4/5 redundancy.

### Secondary — Trust for a sensitive permission

The library's key finding is negative: Shortwave, Superhuman and Monarch all bury security and lean on enterprise logos Envoy doesn't have. That route is closed. **Plaid's grammar** — *"you're in control of who has access"* — is the wording model, and the product already ships the mechanism.

**Applied as:** the approval step becomes a first-class section showing a real draft email with a visible approve control and the state *"awaiting your approval."* Don't claim safety; display the safeguard. Translate the product's developer-language trace (`Thought / Action / Observation`, `compose_email(...)`) into human terms while keeping its structure.

### Secondary — No low-commitment first action

**Wise's** in-hero tool is the model, and Envoy's own demo already has the capture line: **"Email me this lineup to finish later."** Use it verbatim as the secondary CTA after a lineup renders.

### Secondary — Two audiences

**Thumbtack Pro's** architecture: one nav link (`For pros`) plus one clearly-signposted band low on the page. Nothing more on this page.

---

## 4. Real content available (the contract)

Full detail in `../01-current-state/inventory.md`. Summary of what may be used:

**Reuse verbatim — the strongest lines we have**
- `Projects fail in the messy middle`
- `Not post-and-wait`
- `You're in control.` / `Every message sends from your address only after you approve it.`
- `Your digital representative for outreach.`
- `Delegate outreach without losing your voice`
- `Email me this lineup to finish later`
- `Free to plan. Pay only to automate.`
- Problem list: `Searching for service providers across dozens of tabs` / `Losing track of who you've contacted` / `Writing the same intro emails over and over` / `Losing context as replies trickle in over weeks` — *sharpen the vocabulary, keep the observations*
- FAQ answers: `Outreach is written in your voice and sent on your behalf. You stay in full control of tone and what gets sent.` · `Anything that needs multiple vendors — weddings, events, renovations, repairs, fundraisers, company offsites, and more.`
- Vendor side: `Win more work, without chasing leads.`

**Reuse as structure, rebuilt in honest HTML**
- The lineup: category → rationale sentence → count badge → 3 ranked cards (name, city, price band, rating) → "See N more"
- The Canvas: `TOTAL CONTACTS / NEEDS YOU / REACHING OUT / HEARD BACK`, plus *Who Envoy is talking to* by category with `replied · pending`
- The agent trace: recalled details → searched → saved preference → drafted email → **awaiting approval**

**Pricing — approved for use, real figures**
Frame: `Free to plan. Pay only to automate.` · Free (1 active project, Envoy-built lineups, reach out yourself, track every reply) · **Pro $96/yr** (unlimited projects, Pro mode) · **Agency $200/yr per user** (automated Envoy outreach, drafts replies & follow-ups in your voice, multiple seats, priority vendor responses). Vendor tiers available but likely out of scope for this page.

**Never invent, never reuse — mock data**
`Maya R.` testimonial · `48h` / `4×` / `34 jobs won` / `4.3× autonomy ratio` / `1,284 views` / `37 leads` / `$110,100 funnel` · all demo vendor and lead names · any user count, rating, logo or press mention. Anything a layout needs but we don't have renders as a visible `[LABEL — TBD]`.

---

## 5. Page narrative

Six content bands between header and footer. Each does exactly one job; if a band can't state its job in a sentence, it shouldn't exist.

| # | Band | Its one job |
|---|---|---|
| 0 | **Header** | Orient, and route pros away. `Envoy` · How it works · Pricing · For pros · Log in · *Start a project*. |
| 1 | **Hero — search-led** | Say what this is and let them start in the same viewport. Headline carries the agent claim; the project field is the primary action. |
| 2 | **The lineup** | Prove it. The visitor's input (or a default example) produces a real, reasoned, category-by-category lineup. The page's densest, most informative band. Secondary CTA: *Email me this lineup to finish later*. |
| 3 | **The messy middle** | Name the pain, using the site's best line — and give it the picture it has never had (the Canvas: contacts, needs you, reaching out, heard back). |
| 4 | **How it works → ending on approval** | Make the mechanism legible in three steps, and let step three *show* the drafted email awaiting approval. This band carries both comprehension and trust. |
| 5 | **Case studies: wedding → kitchen renovation → company offsite** | Let anyone self-identify in one second, and carry the warmth. Tiles, concrete, in that order. |
| 6 | **Not post-and-wait + pricing** | Separate Envoy from marketplaces, then remove cost as an objection. `Free to plan. Pay only to automate.` |
| — | **`[PROOF — TBD]`** | Reserved slot, after comprehension. Visibly empty. |
| — | **Vendor band** | One signposted strip: *Are you a vendor?* → `Win more work, without chasing leads.` → link out. |
| 7 | **Closing CTA + footer** | Repeat the one action. Footer carries LinkedIn, pricing, for-pros, legal. |

**No new sections beyond this list without asking.**

---

## 6. Constraints

**From the ground rules**
- Never fabricate social proof. Placeholders are visibly labelled.
- Real copy first; reframe, never invent capability.
- Self-contained HTML, all CSS/JS inline, Google Fonts the only external dependency.
- Genuinely responsive; reviewed at 375 / 768 / 1440 before presenting.
- WCAG AA contrast on all text, visible focus states, semantic landmarks, alt text, no information by colour alone.

**From the rulings**
- **Horizontal positioning.** Not wedding-led. Weddings lead the case studies only.
- **Live product.** Primary action is *start a project*, free, no card. No waitlist anywhere.
- **Search-led hero with an agent headline.**
- **Email only.** No SMS, no phone calls — anywhere, including inside rebuilt UI components. The demo's texting and 6-minute call must be stripped from anything I build.
- **Softened hero.** The hero promises the lineup and the drafted outreach (free). Full hands-off delegation is presented as the upgrade, not the headline.
- **Pricing goes on the page**, real figures.
- **No Maya R.**, and no mock metrics.
- **Serif and sans both explored** — the type question gets answered by seeing it, not by argument. A is the sans option, B is the serif option, C proposes a third position.

**From the audit — fix, don't inherit**
- Kill `scroll-snap`. Kill the 353 KB React shader. Fix the `<h1>` `<br/>` so it doesn't announce as "project.We". Add `<header>`/`<nav>`. Name the sections. Recompress the OG image reference. Never let text sit on a volatile background.

---

## 7. The three directions

### Direction A — Conservative cleanup
> *The version he could ship tomorrow without it feeling like a rebrand.*

Keep the dark ground, the electric blue, and Instrument Sans — the brand your friend already has and already shares. Keep the existing narrative order. Everything that changes is craft and truth: scroll-snap dies so the page can be skimmed; the shader becomes a static CSS gradient confined to the hero so body copy never sits on a volatile background and contrast clears AA everywhere; the hero gains the project-description field; one real product artifact (the lineup) enters the page; the redundant "What is Envoy / How it works / Why Envoy" triplet collapses from three screens into one; the trust sentence comes above the fold; procurement vocabulary is replaced throughout; the case-study tiles and pricing are added. **Type: refined sans** — Instrument Sans at 600 rather than 700, looser tracking, fewer steps. This is the direction that answers "is the page's problem really its brand, or just its execution?" — and it is the sans half of the type question.

### Direction B — Opinionated rework
> *The version that best expresses the brief.*

Rebuild the structure strictly around the three problems, and move the marketing site toward the product it sells: a light, warm ground matching the app, one warm accent alongside the existing blue, and **a serif display face** over Instrument Sans body. The search-led hero resolves into a live lineup — the visitor's own project, reasoned category by category — which is the single most persuasive artifact Envoy owns and has never shown. The messy middle finally gets its picture in the Canvas. "How it works" ends on a real drafted email with a visible approve control, so the inbox-trust objection is answered by demonstration rather than assertion. Case-study tiles run wedding → kitchen → offsite, carrying warmth without narrowing the product. Brand stays recognisably Envoy — same mark, same blue, same voice, better register. **This is the serif half of the type question, and my recommendation.**

### Direction C — Radical rethink
> *What the page could be if nothing were sacred.*

Question the premise that this is a landing page at all. The current site argues in feature bands; the product's real subject is **time** — the eight weeks of chasing between deciding and deciding well. So: the page *is* a project. You type yours at the top, and everything below becomes your project unfolding — week one, the lineup; week two, the first drafts going out and the first replies; week five, the Canvas filling with *heard back* and *needs you*; week eight, decisions made. Sections are not features, they are elapsed time, and scrolling the page is scrolling the messy middle with Envoy in it. The primary action shifts subtly from "start a project" to "see what the next eight weeks look like," with signup as its natural end. Aesthetically it leaves SaaS entirely for something editorial and photographic — closer to a magazine feature about a project than a product page. Grounded in the research: it's the Wise in-hero-tool pattern taken to its conclusion, and it's the only structure where the page's best sentence is the page's actual architecture. **Type: an editorial display serif with a distinct sans companion** — a third position on the type question.

**Divergence check.** A and B differ in ground, type, and how much structure moves. B and C differ *structurally*, not just visually: B is a conventional band-based page arguing from problems; C is organised on a time axis and has a different primary action. If, when built, B and C start converging, C gets pushed further before either is shown.

---

## 8. Open items carried into Phase 5

Not blocking; I'll build under the stated assumption and flag each in `compare.html`.

1. **Logo asset** — the wordmark is a CSS `mask-image` PNG that inherits its colour. Directions B and C need a real dark-ink SVG on a light ground. *Assumption: I'll render the wordmark as text plus the geometric mark until a proper asset exists.*
2. **Photography** — no confirmed licence or budget. *Assumption: I'll build category imagery slots as labelled placeholders with CSS treatment, so the layouts hold without stock and improve with it.*
3. **Inline signup vs. hosted** — the Fillout waitlist question is moot now that the product is live, but I still don't know whether the hero field can post to the real app. *Assumption: the field routes to the app's own start-a-project flow.*
4. **Real proof** — one early user or design partner quote would convert the `[PROOF — TBD]` slot into a real band.
5. **Vendor tiers** — planner pricing is on the page; vendor pricing is assumed out of scope here and lives on `/pros`.
