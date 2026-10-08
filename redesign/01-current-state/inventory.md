# Current-state inventory

**This file is the contract.** Everything in Part 1 is real content from the live site and may be reused verbatim or sharpened. Part 2 is sanctioned copy from the founder's demo app — usable, but flagged where it commits the product to something. Part 3 is the design-token audit. Part 4 lists what does **not** exist and must never be invented.

Captured 2026-08-25. Source HTML: `source-original.html`. Screenshots: this directory (desktop), `mobile/` (375px), `product/` (demo app).

---

## Part 1 — Live site: https://hello-envoy.com/

Structure: 7 full-viewport scroll-snapped panels + a fixed footer that slides up at the end. No navigation, no header.

### Document-level

| Field | Value |
|---|---|
| `<title>` | Envoy — Plan any project. Line up the vendors. |
| `meta description` | Envoy helps you plan multi-vendor projects, compare providers, and send outreach from your own inbox — all in one place. |
| `og:title` | Envoy — Plan any project. Line up the vendors. |
| `og:description` | *(same as meta description)* |
| `og:image` | `https://hello-envoy.com/og-image.png` — 2400×1260, **5.44 MB** ⚠ |
| `twitter:card` | summary_large_image |
| Analytics | Google Analytics `G-W1CP3DNWCY`; Cloudflare Insights RUM |
| `robots.txt` / `sitemap.xml` | **both 404** ⚠ |

### Section 01 — Hero  (`01-hero.png`, `mobile/01-hero.png`)

- Logo wordmark, rendered as a CSS mask over `envoy-logo.png` (22.5 KB), `role="img"` `aria-label="Envoy"`
- **H1:** `Plan any project.` / `We line up the vendors.` *(line break between; renders to AT as "project.We" — bug)*
- **Lead:** `Describe what you need and where. Envoy brings your vendors, project details, and outreach together — so you can compare options and decide with confidence.`
- Scroll affordance: `SCROLL` + down arrow, `aria-hidden`
- Floating CTA (fixed, all panels): **`Join the waitlist`**

### Section 02 — The problem  (`02-problem.png`)

- **Eyebrow:** `The problem`
- **H2:** `Projects fail in the messy middle` ← *best line on the site*
- **Lead:** `Not at the idea stage — when you're finding people, keeping details straight, and waiting for replies.`
- **List:**
  1. `Searching for service providers across dozens of tabs`
  2. `Losing track of who you've contacted`
  3. `Writing the same intro emails over and over`
  4. `Losing context as replies trickle in over weeks`

### Section 03 — What is Envoy  (`03-what-is-envoy.png`) ⚠ *overflows its snap point: 929px in an 805px viewport*

- **Eyebrow:** `What is Envoy`
- **H2:** `Everything you need to decide, one place`
- **Lead:** `A project hub for renovations, events, commercial build-outs, and any multi-vendor project — with the contacts, context, and outreach tools to move from research to decision.`
- **Feature list:**
  - `Discover contacts` — `Describe your project and location. Envoy surfaces relevant providers across every trade and category your project needs.`
  - `Organize your project` — `Timeline, budget, goals, and contacts in one view — compare options side by side instead of piecing together scattered notes.`
  - `Plan with Envoy` — `Ask Envoy to sharpen your scope, timeline, and brief before you reach out — grounded in your project, not generic advice.`
  - `Send outreach` — `Draft, review, and send from your connected Gmail or Microsoft inbox.` ⚠ *undersells — see brief addendum §2*
- **Note (trust):** **`You're in control.`** `Every message sends from your address only after you approve it.` ← *most trust-critical sentence on the page; currently cut off below the fold*

### Section 04 — How it works  (`04-how-it-works.png`)

- **Eyebrow:** `How it works`
- **H2:** `One project, every vendor type`
- **Lead:** `Envoy flips the marketplace model. Find providers across trades and industries, shortlist your options, and reach out on your terms.`
- **Steps:**
  1. `Discover` — `Search by project and location. Find providers across every vendor type your project needs — contractors, caterers, AV, florists, and more — without jumping between sites.`
  2. `Organize` — `Attach contacts and capture what each pro needs — dates, budget, goals — so you can weigh options and decide from one hub.`
  3. `Plan` — `Ask Envoy to refine your scope and brief before your first email goes out.`
  4. `Reach out` — `Draft and send from your inbox. Follow up in the same thread.`

### Section 05 — Why Envoy  (`05-why-envoy.png`)

- **Eyebrow:** `Why Envoy`
- **H2:** `Not post-and-wait` ← *second-best line on the site*
- **Lead:** `Marketplaces work for one-off jobs. They break when you're coordinating multiple trades for one project.`
- **Feature list:**
  - `Start before you sign up` — `See relevant contacts by trade before you create an account.` ⚠ *claimed but not delivered on the live page*
  - `Outreach from your inbox` — `Contacts reply to you — not a marketplace relay.`
  - `Decisions, not dead ends` — `Weeks of research, replies, and follow-up stay in one project hub — so you always have the full picture when it's time to choose.`

### Section 06 — Who it's for  (`06-who-its-for.png`)

- **Eyebrow:** `Who it's for`
- **H2:** `Anyone running a multi-vendor project`
- **List** (bold lead-ins as marked):
  1. **`Homeowners`** ` planning renovations who want to run the process themselves`
  2. **`Small business owners`** ` opening locations or coordinating launch vendors`
  3. **`Project coordinators`** ` tired of repeating the same brief in five different apps`
  4. **`Couples and wedding planners`** ` coordinating venue, catering, florals, photography, and more — without losing the thread`

### Section 07 — CTA  (`07-cta.png`)

- **Eyebrow:** `Early access`
- **H2:** `Join the waitlist`
- **Lead:** `Be first to plan projects, discover contacts, and send outreach from your own inbox.`
- **Button:** `Join the waitlist`

### Footer  (`08-footer.png`)

- **`Follow us`** → LinkedIn link → `https://www.linkedin.com/company/hello-envoy/`
- `Service providers interested in joining as a pro — join the waitlist and we'll reach out as we onboard new categories.` ← *the only mention of the vendor side of the business*
- **`Keep in touch`** — `Join the waitlist for early access and product updates.` + button
- `© 2026 Envoy`

### CTA inventory — complete

| # | Label | Type | Destination |
|---|---|---|---|
| 1 | `Join the waitlist` | button, fixed top-right | `window.open('https://forms.fillout.com/t/k29bspbPEWus', '_blank')` |
| 2 | `Join the waitlist` | button, section 07 | same |
| 3 | `Join the waitlist` | button, footer | same |
| 4 | `LinkedIn` | link, footer | `https://www.linkedin.com/company/hello-envoy/` |

**Four interactive elements on the entire page. Three are the same button. All conversion leaves the site.**

### Images & illustrations

| Asset | Role | Notes |
|---|---|---|
| `envoy-logo.png` | Wordmark, hero | 22.5 KB; used as a CSS `mask-image`, so it inherits `--color-text` and cannot carry its own colour |
| `favicon.svg` | Favicon | — |
| `og-image.png` | Social share | **5.44 MB** ⚠ needs recompression |
| WebGL shader canvas | Full-bleed animated background | `assets/shader-bg.js`, **1.54 MB raw / 353 KB gzipped**, bundles React |

**Zero `<img>` elements in the document. No photography, no product UI, no illustration.**

---

## Part 2 — Demo app copy (mockvoy.lovable.app) — sanctioned, use with care

Provided by the founder as source material. Screenshots in `product/`.

### Taglines & positioning

- **`Your digital representative for outreach.`** *(footer, every page)*
- `Your digital representative for mass asynchronous outreach and fact finding.` *(login)*
- `Describe your project and Envoy lines up the right vendors, then handles outreach for you. Plan weddings, renovations, and events faster.` *(meta description — sharper than the live site's)*
- `Delegate outreach without losing your voice` *(login)*
- `Coordinate vendors and partners effortlessly` · `Track every interaction in one place` *(login)*

### Hero (demo)

- Same H1 as live: `Plan any project. We line up the vendors.`
- **Sub (differs from live):** `Describe what you're building, hosting, or fixing. Envoy brings your vendors, project details, and outreach together — so you can compare options and decide with confidence.`
- Inputs: project description + `Location`; button `Find vendors`
- **Example chips — the three case studies, in order:**
  1. `Outdoor wedding for 150 guests in fall`
  2. `Renovate a 1920s kitchen`
  3. `Company offsite for 40 people`

### How it works (demo)

- **H1:** `How Envoy works` — `From idea to vendor replies in three simple steps.`
- **Lead:** `Envoy does the legwork of finding, shortlisting, and contacting vendors — so you can focus on the decisions that matter.`
- CTA: `Try it free`
- **Step 1 — `Describe your project`:** `Tell Envoy what you're planning in plain language — a wedding, a renovation, an offsite. No forms, no categories to hunt through.` · `Works for any project type` · `Add your location for local matches`
- **Step 2 — `Get an instant vendor lineup`:** `Envoy figures out exactly which vendors you need and surfaces a curated shortlist in seconds — ranked, rated, and ready.` · `Right vendor types, automatically` · `Shortlist you can fine-tune`
- **Step 3 — `Envoy reaches out for you`:** `Approve your lineup and Envoy sends personalized outreach in your voice, then tracks every reply in one organized place.` · `Outreach sent in your tone` · `All replies in one inbox`

### FAQ (demo) — usable verbatim

- **`How much does it cost to start?`** → `Starting is free — you get 250 credits, no card required. Paid plans unlock automation and premium placement.`
- **`Do vendors know it's Envoy?`** → `Outreach is written in your voice and sent on your behalf. You stay in full control of tone and what gets sent.`
- **`What kinds of projects work?`** → `Anything that needs multiple vendors — weddings, events, renovations, repairs, fundraisers, company offsites, and more.`

### Closing CTA (demo)

- `Ready to line up your vendors?` — `Describe your project and get a curated shortlist in seconds. Free to start, no card needed.` → `Start your project`
- Lineup-page CTAs: **`Start this project with Envoy`** and **`Email me this lineup to finish later`** ← *the low-commitment action the live page lacks*
- Browse page: `Don't want to search manually?` — `Describe your project and Envoy assembles the perfect vendor lineup — then reaches out for you.` → `Build my lineup`

### Lineup output structure (the product's best moment)

Per project: a title (`Wedding`), `Your vendor lineup`, and a one-sentence project summary. Then per vendor category: category name, **a rationale sentence for why this project needs it**, a count badge (`13 found`), and 3 vendor cards (name, city, price band `$$`–`$$$$`, star rating), plus `See 10 more venue`. Some vendors carry an **`Envoy`** badge.

Wedding lineup categories: Venue · Caterer · Event Rental Company · Wedding Planner · Photographer.
Example rationale (verbatim): `Essential for securing a scenic Austin landscape that can accommodate 150 guests and provides a weather contingency plan.`

### Vendor / pro side (demo `/pros`)

- **`Envoy for Business`** — **`Win more work, without chasing leads.`**
- `Envoy puts your business in front of people actively planning projects — then helps you respond faster than anyone else.`
- CTAs: `Join as a pro` · `See pricing`
- `Get discovered by ready buyers` — `Show up when people describe projects that need exactly what you offer — with premium placement on higher tiers.`
- `Never miss a lead again` — `Every inquiry, follow-up, and deal-in-progress tracked in one dashboard with reminders before things slip.`
- `Let Envoy reply` — `Connect your inbox and Envoy analyzes incoming emails, drafts responses, and communicates on your behalf.`

### Pricing (demo) ⚠ *unconfirmed — do not publish figures without founder sign-off*

**Frame:** `Simple, transparent pricing` — **`Free to plan. Pay only to automate.`** — `Planning a project? Envoy is free to use. Paid plans are for vendors growing their business and teams that want automated outreach.`

*Project owners:* **Free** — 1 active project · Envoy-built vendor lineups · Reach out to vendors manually · Track every reply in one place. **Pro $96/yr** — everything in Free · Pro mode · Unlimited projects. **Agency $200/yr per user** — everything in Pro · Automated Envoy outreach · Envoy drafts replies & follow-ups in your voice · Multiple seats · Priority vendor responses.

*Vendors:* **Basic** free — business listing · leads from vendor search. **Plus $250/yr** — full dashboard · automated follow-up reminders · alerts for deals about to fall through the cracks. **Premium $750/yr** — 250 credits/month · premium placement · Envoy connects to your inbox · analyzes emails automatically · communicates on your behalf.

The frame line is safe to use on its own. The figures are not, until confirmed.

---

## Part 3 — De facto design tokens (live site)

### Colour

| Token | Hex / value | Used for |
|---|---|---|
| `--color-primary` | `#003fb3` | Button fill |
| `--color-primary-mid` | `#7191f7` | Eyebrows, focus rings, link hover |
| `--color-primary-light` | `#dde7fe` | Step numerals |
| `--color-primary-soft` | `rgba(113,145,247,.18)` | Step numeral background |
| `--color-bg` | `#061228` | Page ground |
| `--color-text` | `#dde7fe` | Body text |
| `--color-muted` | `rgba(221,231,254,.72)` | Secondary text ⚠ *fails AA over shader* |
| `--color-border` | `rgba(221,231,254,.14)` | Hairlines, card borders |
| Card fill | `rgba(6,18,40,.5–.55)` + `backdrop-filter: blur(10–12px)` | List items, notes |
| Button text | `#fff` | — |

**One hue. No warm tone, no secondary, no accent anywhere in the system.**

### Type — `Instrument Sans` (400/500/600/700), served from fonts.bunny.net

| Role | Size | Weight | Other |
|---|---|---|---|
| Headline (h1/h2) | `clamp(2rem, 6vw, 3.25rem)` → 52px max | 700 | `line-height:1.08`, `letter-spacing:-0.03em` |
| Lead | `clamp(1.05rem, 2.4vw, 1.25rem)` → 20px max | 400 | `line-height:1.65`, `max-width:52ch` |
| Eyebrow | 12px | 600 | `letter-spacing:.18em`, uppercase |
| Feature h3 | 16px | 600 | — |
| Step h3 | 17px | 600 | — |
| Body / list | 15px | 400 | `line-height:1.5–1.55` |
| Note / footer link | 14px | 400 / 500 | — |
| Footer copy | 13px | 400 | — |
| Button | 14px (large: 15px) | 600 | — |
| Scroll hint | 11px | 400 | `letter-spacing:.16em`, uppercase |
| Body base | — | — | `line-height:1.6` |

Measured in use: 9 sizes, 4 weights, 1 family.

### Spacing, radii, layout

- Panel padding: `88px clamp(20px,5vw,40px) 56px` (mobile `72px … 40px`)
- Panel: `min-height:100dvh`, `scroll-snap-align:start`, `scroll-snap-stop:always`
- Content width: `640px` default, `720px` wide, `820px` hero
- Radius: `--radius: 0.5rem` (8px) everywhere; step numerals `50%`
- Rhythm: headline→lead 20px; lead→list 32–36px; list gaps 14–20px; note top 28px
- Breakpoint: **one**, `max-width: 640px`
- Buttons: `10px 18px` (large `14px 28px`)
- Footer: fixed, `translateY(100%)` → `0` on reveal, `blur(16px)`, grid `1fr 1fr` → `1fr` at 640px

### Motion

- Reveal: `opacity 0→1`, `translateY(28px)→0`, `0.65s ease`, staggered `.05s`–`.4s` by child index, driven by IntersectionObserver at ratio ≥0.45
- Scroll hint: `bob` 2.4s infinite
- Button hover: skewed `::before` wipe, `0.4s cubic-bezier(.3,1,.8,1)`
- Footer reveal: `0.45s cubic-bezier(.22,1,.36,1)`
- `prefers-reduced-motion: reduce` — **properly handled**; all of the above disabled

### Accessibility state

- ✅ Visible focus: `2px solid #7191f7`, `outline-offset: 3px`
- ✅ `prefers-reduced-motion` respected
- ✅ `color-scheme: dark` declared
- ❌ **Contrast fails AA** — measured minima 1.00–1.57:1 against the animated shader (floor 4.5:1). See brief for the full table.
- ❌ No `<nav>`, no `<header>`; sections unlabelled
- ❌ `<h1>` announces as "project.We line up the vendors."
- ❌ Content overflows a mandatory snap point in section 03

---

## Part 4 — What does NOT exist (never invent)

- **No testimonials.** None on the live site. The demo's *"Maya R. · Event venue owner"* quote is **mock data in a mock app** and is not to be used.
- **No customer logos, press mentions, ratings, or review counts.**
- **No user, project, or vendor counts.** The demo's `48h avg. time to first reply`, `4x more qualified leads` and `250 free credits` stats are **mock**; only *250 free credits* is corroborated by the demo's own FAQ, and even that is unconfirmed for launch.
- **No named team members, founder bio, or About content.**
- **No privacy policy, terms, or security page** — notable given the product requests inbox OAuth.
- **No real vendor data.** Demo vendor names and cities are synthetic and internally inconsistent (an Austin wedding returns Asheville / Charleston / Brooklyn vendors).
- **No confirmed pricing.**
- **No real photography** of weddings, renovations or events, and no licence for any.

Anything in this list that a layout calls for renders as an explicit `[PLACEHOLDER — TBD]`, per the ground rules.

---

## Part 5 — The signed-in app (added 2026-08-25, second pass)

**This section supersedes assumptions made earlier in this file and in `00-brief/brief.md`.** The demo's *public* marketing pages are unchanged — I re-crawled and diffed them, they are identical. Everything new is behind the login, and it changes the product's shape.

Captured by driving the designer's authenticated Chrome session, read-only. Screenshots were not written to disk (the authenticated session lives only in that browser); the content below is transcribed verbatim and is the contract. **All of it is mock data** — see the integrity flags at the end.

### The product is a conversational agent, not a search tool

Route `/app`. Three-pane layout, **light theme** (confirming Part 2 §f):

- **Left rail** — `YOUR BUSINESS` mini-panel (`VIEWS 1,284 +12% wk`, `LEADS 37 +5 new`), `Dashboard`, `Contacts`, `New Project`, then `PROJECTS`: *Alaska Move · Board game store · Outdoor Wedding for 150 Guests · Test Project*. Account footer: `demo@hello-envoy.com` · `Free plan`.
- **Centre** — a chat thread with Envoy. Input placeholder: `Ask Envoy anything…` Opening message on a new project: *"Welcome! I'm Envoy, your outreach assistant. I'll help you with [project]. What would you like me to do first?"*
- **Right** — the **Canvas**.

The project list is notably broader than the three marketing chips — *Alaska Move* (shipping two vehicles to Anchorage) and *Board game store* are both live projects. This supports the horizontal positioning ruling.

### The Canvas — the single most valuable artifact on the page

For *Outdoor Wedding for 150 Guests*:

- Header: project name, `PROJECT · Active`, description, `TIMELINE June 14`, `BUDGET $$$`
- **Four-stat pipeline:** `23 TOTAL CONTACTS` · `2 NEEDS YOU` (highlighted red) · `5 REACHING OUT` · `13 HEARD BACK`
- **`WHO ENVOY IS TALKING TO`** — ten vendor categories, each with a count and a reply state:
  `Venue 3 (2 replied · 1 pending)` · `Catering 3 (2·1)` · `Photography 3 (1·2)` · `Florist 2 (2·0)` · `Music & DJ 2 (1·1)` · `Officiant 2 (2·0)` · `Rentals 2 (1·1)` · `Bar Service 2 (0·2)` · `Hair & Makeup 2 (1·1)` · `Transportation 2 (1·1)`
- **`LATEST MOVES`** — an activity feed, each entry tagged by category:
  - *Magnolia Hill Vineyards* — `Lead is asking about negotiating the Saturday rate. Needs owner intervention.` (Venue)
  - *Highland Pour Co.* — `Lead asked about liquor liability and a custom signature drink — Envoy paused for your input.` (Bar Service)
  - *Field Notes Photo Co.* — `added to outreach queue. Envoy will reach out in the next batch.` (Photography)
  - *Magnolia Hill Vineyards* — `Hi Priya, sent an email earlier — texting in case it landed in spam. Any availability for June 14?` (Venue)

**This is "Projects fail in the messy middle" rendered as an interface.** The best sentence on the current landing page has, until now, had no picture. It now has one.

### The chat transcript — capability evidence

Verbatim exchanges worth building the page around:

- **Back-planning from a constraint:** *"I want vows landing right at golden hour."* → *"Sunset that day is 6:08pm, so I'll back-plan from a 5:30pm ceremony start. I'll thread that time through the photographer, florist, and trio so everyone arrives on the right beat."*
- **Contingency held open:** *"venue has zero permanent cover"* → *"I'll get a sailcloth tent quote with sidewalls and hold it as a contingency. Looks like ~$3,200 to reserve and release T-14 if the forecast is clean. Want me to flag that line for approval?"*
- **Vendor intelligence:** *"Sarah's a dream — replies inside two hours on weekdays. She prefers Loom walkthroughs over long email threads, and she's already locked the date. Invoicing is split 50/50."*
- **Constraint discovery:** *"Heads up on Hudson: they won't staff under 100 guests and they charge a flat $400 travel fee outside Brooklyn."*
- **Voice correction — the money exchange:** *"please drop the 'Hope this finds you well' stuff in vendor emails. Feels stiff."* → *"Understood. I'll open with the ask and sign off 'Thanks so much — Maya & James.' I'll also kill the exclamation points — you mentioned they read as pushy to you."*
- **Budget guardrail:** *"We're at $78k ceiling."* → *"Florals + catering are already 54% of the total. I'll auto-flag any new vendor ask above $1,500 and won't send anything until you and James explicitly confirm. You'll see those as 'needs you' in the inbox."*

### The agent trace — the transparency artifact

After *"Can you start reaching out to florists and photographers for our October wedding?"*, the UI renders labelled steps:

| Step | Content |
|---|---|
| `REASONING` | Planning the outreach — *Deciding which vendors to contact first* |
| `MEMORY ACCESSED` | Recalled wedding details — *Date: Oct 12, 2026 · Budget: $45,000 · 150 guests* |
| `WEB SEARCH` | Searched: top-rated wedding florists near venue — *12 results · filtered to 4 with October availability* |
| `MEMORY STORED` | Saved preference — *Style: wildflower / garden-style arrangements, muted autumn palette* |
| `EMAIL DRAFTED` | Drafted email to Willow & Co. Florals — *Subject: Outdoor wedding florals — Oct 12, 150 guests* |

Expanding the last step reveals:
> **Thought:** Lead with the date and guest count so they can check availability quickly, and mention the garden-style preference.
> **Action:** `compose_email(to="Willow & Co. Florals", template="vendor_intro")`
> **Observation:** Draft ready for review — **awaiting approval before sending.**

Summary message: *"I've recalled your date and budget, found 4 florists with October availability, saved your garden-style preference, and drafted an intro email to Willow & Co. Florals. Want me to send it and draft the rest?"*

**This is the answer to the trust problem (library S1).** It doesn't claim safety, it displays the safeguard. Note the raw trace is written in developer language (`Thought/Action/Observation`, function-call syntax) — for the landing page this must be translated into human terms while keeping the structure.

### Envoy for Business — the vendor side

Opens as a full overlay from the `YOUR BUSINESS` panel. Tabs: **Listing · Reputation · Chat · Pipeline · Inbox**.

**Listing** — *"Your listing — This is what consumers see when Envoy surfaces your business. Keep it accurate."* Demo business: `Northwind Studio`, tagline `Boutique wedding & event production`, description *"A small team obsessed with seamless execution — from venue coordination to vendor management. We respond within 2 hours and quote within 24."*, Brooklyn NY, `$$$`, specialties `Weddings · Corporate events · Day-of coordination · Vendor sourcing`.

**Inbox** — a lead list with status chips (`New` · `Qualifying` · `Quoted` · `Won` · `Lost`) and handling states (`Envoy handling` · `Needs you` · `Awaiting reply` · `Replied` · `Closed`), each with a dollar value. Sample leads: *Mira Chen — Weddings · Garden wedding, 120 guests · $18,500*; *Theo Banks — Social & parties · Rooftop birthday, 60 ppl · $5,200 · Needs you*; *David Park — Corporate · Product launch dinner · Quote sent · $14,200 all-in. Awaiting reply.*; *Jordan Wells — Corporate offsite, 40 ppl · Contract signed. Deposit received. · Won · $22,000*.

The thread view carries a banner — **`ENVOY IS HANDLING THIS`** — *"Asking qualifying questions: date flexibility, guest count confirmation, dietary considerations, and rain-plan preference. Will draft a quote once answers come back."* — and then a **multi-channel** transcript, each message tagged by channel:

- `Lead · Email · 2d ago` — *"Hi! Looking for a coordinator for a 120-person garden wedding on June 14. Is that something you handle?"*
- `Envoy · Email · 2d ago` — *"Hi Mira — yes, absolutely. A few quick questions so we can put together an accurate quote…"*
- `Lead · Sms · 1d ago` — *"Quick update via text — date is firm, venue is confirmed (Brooklyn Botanic)."*
- `Envoy · Call · 1d ago` — **"Outbound call · 6 min — confirmed guest count at 118, gathered dietary needs (12 vegetarian, 2 GF)."**
- `Envoy · Email · just now` — *"Got it. Drafting a quote now including a backup tent rental option and day-of coordination. Will route to you for approval before sending."*

Controls: **`Review draft quote`** (primary) and **`Take over`** (secondary).

**Pipeline** — `WHAT ENVOY'S UP TO`: `ACTIVE 6` · `REPLIED 1` · `NEEDS YOU 2`, and channel counters `Email 3` · `SMS 1` · `Calls 1`. Then *Jobs won vs manual interventions (last 90 days)* — `34` jobs won against `8` manual interventions, `4.3× WON PER INTERVENTION`, captioned *"Envoy closed 34 jobs while only needing your input 8 times — a healthy 4.3× autonomy ratio."* Then conversations by project type (Weddings $32,400 · Corporate $36,200 · Social & parties $16,500 · Nonprofit & galas $38,000) and a deal funnel (New $10k → Qualifying $57k → Quoted $22k → Won $22k; total $110,100).

### What this changes

1. **Envoy works over email, SMS *and* phone calls.** The live landing page claims email only. This is a material, differentiating capability that is currently invisible.
2. **`Take over` and `awaiting approval before sending` are real controls**, not marketing promises — the delegation-without-losing-control spine is demonstrable.
3. **The agent learns and retains preferences** (tone, style, cc lists, budget thresholds) across a project. Nothing on the live page suggests this.
4. **The vendor side is a full second product**, not a footnote. The Checkpoint-2 ruling (one signposted band + nav link on this page) still stands for *this* page, but the founder should know the pro side likely warrants its own page.
5. **The "autonomy ratio" framing** — *jobs won per manual intervention* — is a genuinely original metric and the clearest expression of the product's value. Unusable as proof (mock), excellent as a concept.

### Integrity flags — everything in Part 5 is mock

Not usable as proof, in any direction, on the landing page:

- `1,284 views`, `37 leads`, `34 jobs won`, `8 manual interventions`, `4.3× autonomy ratio`, `$110,100 deal funnel`, all per-category dollar values
- All lead names and businesses (`Mira Chen`, `Northwind Studio`, `Magnolia Hill Vineyards`, `Willow & Co. Florals`, `Petal & Pine`, `Hudson Catering`, …)
- Internally inconsistent dates and budgets — the Canvas says `June 14` and `$$$`, the chat says `Oct 12, 2026` and `$45,000`, and the user says `$78k ceiling`; timestamps read `94d ago`
- The couple names `Maya & James`; unrelated to, but easily confused with, the mock `Maya R.` testimonial already excluded in Part 4

**Usable as illustration, clearly labelled as such:** the *structure* of the Canvas, the *shape* of the agent trace, the *kinds* of things Envoy says. Per the moodboard, these get rebuilt as honest HTML components with plainly illustrative content — never a mock screenshot presented as a live result.
