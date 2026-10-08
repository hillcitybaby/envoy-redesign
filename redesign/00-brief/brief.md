# Research brief — Envoy landing page

**Page under review:** https://hello-envoy.com/
**Captured:** 2026-08-25 (full source saved at `01-current-state/source-original.html`; screenshots at 1440/768/375 in `01-current-state/`)
**Method:** live page fetched and instrumented via Chrome DevTools Protocol (headless Chrome), plus web research on the competitive set. All numbers below are measured, not estimated.

---

## What it does

Envoy is a planning hub for projects that require hiring multiple outside vendors. You describe a project and a location; it surfaces relevant service providers across every trade the project needs; it keeps the project's scope, timeline, budget and contacts in one place; it helps you sharpen the brief before you contact anyone; and it drafts and sends outreach **from your own connected Gmail or Microsoft inbox**, so replies come back to you rather than into a marketplace relay. It is currently pre-launch — the only action available is a waitlist signup.

Two things are worth separating out, because the page treats them as equals when they aren't:

The **structural bet** is anti-marketplace. Every incumbent in this space (Thumbtack, Angi, Houzz, The Knot's vendor marketplace) monetises by intermediating the conversation: you post, they route, pros bid, the platform owns the thread. Envoy's model is that you own the relationship from the first email. That's a real, defensible, differentiating idea and the page does say it — "Contacts reply to you — not a marketplace relay," "Not post-and-wait." This is the sharpest thinking on the page.

The **emotional bet** is that the hard part of a multi-vendor project isn't deciding to do it, it's the eight weeks of chasing in the middle. The page also says this — "Projects fail in the messy middle" is the best line on the site.

**The gap between what it does and how it markets itself.** You told me the main use case is wedding planning. The page does not know that. Measured: the word "wedding" appears **twice** on the entire page, both times below the fold, in the fourth bullet of the sixth section. "Couples and wedding planners" are listed *after* homeowners, small business owners, and project coordinators. Meanwhile the page's actual vocabulary is `vendors` (7×), `providers`, `trades`, `outreach`, `commercial build-outs`, `AV`, `project hub`, `multi-vendor project`. That is procurement language. It describes a wedding accurately and makes it sound like a facilities contract.

This gap is the redesign's core problem, and it's also the mechanical answer to your friend's complaint. "Too masculine and technical" is usually read as a visual problem — the electric-blue WebGL shader, the hard geometric mark, the near-black field. Those contribute. But the *vocabulary* is doing at least as much of the work as the palette, and a warmer palette bolted onto "commercial build-outs" and "every trade and category" will not fix it. Both have to move together.

## Who it's for

**Who the page says it's for:** four audiences, given equal weight, in one list — homeowners running their own renovation, small business owners opening a location, project coordinators, and couples/wedding planners. That is not a target; that's a hedge.

**Who it's evidently for**, reading the product's actual mechanics: someone running a **high-stakes, deadline-fixed, multi-category project for the first and probably only time**, without a professional coordinator, who is therefore doing vendor research as an amateur and feeling the cost of that. Weddings are the purest instance of this — fixed immovable date, 8–14 vendor categories, no prior experience, enormous emotional load, and a research process that genuinely does happen across forty browser tabs and a spreadsheet. A renovating homeowner is the same shape with a softer date. A small business owner opening a location is a different person entirely — more repeat-buyer, more procurement-minded, and much more likely to already have a contractor.

**Sophistication level:** moderate-to-low tooling sophistication, high stakes. This person is not evaluating a SaaS product; they are trying to stop feeling behind. They will not read a feature list charitably.

**The job they're hiring it for:** not "find vendors" — Google finds vendors. The job is *"stop me from losing track, and make me feel like I'm running this instead of drowning in it."* The page's own problem section understands this perfectly and then the rest of the page reverts to feature-speak.

**How they arrive:** almost certainly a friend's link, a founder's LinkedIn post, or a DM right now — there is no organic search surface (measured: `robots.txt` 404s, `sitemap.xml` 404s, one page, no content). That matters more than it sounds. A referred visitor arrives with *zero* context and *some* borrowed trust, which means the page's job is disambiguation, not persuasion — and the page currently spends its first screen on a logo rather than on telling you what this is.

**Two audiences at once — a finding.** The page is aimed simultaneously at consumers running one emotional project and at businesses running operational ones. These want opposite pages. The consumer page needs warmth, reassurance, and a picture of the thing. The business page needs efficiency, control, and integration proof. Trying to hold both is why the copy lands in a neutral register that reads as neither warm nor authoritative — it reads as *technical*, which is the default when you refuse to choose.

## Market context

Five competitors and adjacents, all landing pages reviewed 2026-08-25.

**The Knot** — *"Your wedding team and everything in between,"* subhead *"A new way to wedding plan, now with AI."* Positions as the incumbent all-in-one with an AI layer freshly bolted on. **Does well:** puts a real couple's testimonial above the fold and leads directly with vendor-category imagery — you see photographers, venues, cakes, DJs as *pictures*, so the category is legible in two seconds. **Does badly:** enormous, cluttered, monetisation-dense; the AI claim is a banner, not a demonstrated capability. Envoy's opening is precisely the gap between The Knot's promise and its experience.

**Zola** — *"Wedding planning starts here."* Registry-first business dressed as a planning platform; CTA is *"Let's do this!"* **Does well:** tone. The copy is warm, plural, first-person-adjacent, and the visual system is soft and confident without being twee — this is the closest reference for the register your friend is asking for. **Does badly:** the hero is a mission statement, not a mechanism; you don't learn what the product *does* until several screens down.

**Joy (withjoy.com)** — *"Create a wedding website and registry that is uniquely yours."* **Does well:** specificity in the hero — it names the two artifacts you get, so the offer is unambiguous, and the aesthetic is modern and inclusive rather than traditional-bridal. **Does badly:** narrow. It's a website-and-registry tool, which leaves the actual *vendor coordination* problem — Envoy's territory — almost entirely unserved.

**Thumbtack** — *"For everything home could be,"* with a **project-description text field as the hero element** and a "Find a pro" button. **Does well:** two things worth stealing outright. First, the hero *is* the product's first input — you start using it before you sign up, which is exactly the promise Envoy already makes in copy ("Start before you sign up") and does not deliver in the layout. Second, hard proof immediately below: 4.9 from 15M+ reviews, 300K+ pros, 100M+ projects. **Does badly:** it is a post-and-wait marketplace, which is the thing Envoy is defined against. Its landing page is also generically "home services," which is the trap Envoy is currently in one level up.

**Houzz** — now leading with *"Powerful AI software for construction and design"* — i.e. it has pivoted its front door to the **pro** side. **Does well:** unambiguous audience choice. **Does badly (for us):** it vacated the consumer coordination position. Worth noting as evidence that the consumer-side multi-vendor coordination space is *emptying*, not filling.

**Emerging, category-relevant:** a set of AI-native wedding tools (Wedify, BridalIntel, ItsaYes and similar) are being written about as of 2026 doing "AI vendor matching plus automated outreach" — the same mechanism as Envoy. I have not audited their pages and won't claim anything about their execution, but the category signal is real: **the mechanism is no longer novel by itself, so the positioning has to carry the weight.**

**The white space.** Nobody in the wedding set owns *vendor coordination as the product*. The Knot and Zola treat vendors as a directory adjacent to registry and website revenue; Joy skips it; Thumbtack and Houzz own the home-services version but with a marketplace model and no emotional register. The open position is: **the tool for the person coordinating many vendors for one irreplaceable date, that keeps them in control of every conversation.** Envoy's product is already that. Its page isn't.

**Table stakes the page ignores:** every one of the five shows you the product or its output above the fold, in pictures. Every one has at least one piece of real proof on the page. Envoy has neither — measured, the page contains **zero `<img>` elements** and zero proof of any kind.

---

## Where it breaks down

Structure: seven full-viewport scroll-snapped panels (`min-height: 100dvh`, `scroll-snap-type: y mandatory`, `scroll-snap-stop: always`) plus a fixed footer that slides up at the end. Order: Hero → The Problem → What is Envoy → How it Works → Why Envoy → Who It's For → Join the waitlist.

### First five seconds

Above the fold at 1440×900 the visitor gets: a large wordmark, `Plan any project. We line up the vendors.`, a 28-word supporting paragraph, a `SCROLL` prompt, and a floating `Join the waitlist` button. Nothing else — no image, no product, no navigation.

*What is this?* Ambiguous in a specific and damaging way. "Plan any project. **We line up the vendors**" most naturally reads as *a service* — as if a team does the lining-up for you. It is in fact software that surfaces contacts and drafts your emails, which you approve and send yourself. The hero oversells agency and undersells the product's actual and better promise (you stay in control).

*Who is it for?* Unanswerable. "Any project" is a claim of universality, which a cold visitor reads as "not specifically for me."

*Why should I care?* Not addressed above the fold at all. The reason to care — the messy middle — is on screen two, which the scroll-snap makes a deliberate, committed action to reach.

The single strongest asset on the page, the phrase *"Projects fail in the messy middle,"* is buried one full screen down.

### Narrative structure

The page does have an argument, and its skeleton is correct: problem → what it is → how it works → why not the alternative → who it's for → act. That's better than most pre-launch pages, and it should survive the redesign.

Where it loses the thread: **sections 3, 4 and 5 are the same content three times.** "What is Envoy" lists Discover / Organize / Plan / Send outreach. "How it works" lists Discover / Organize / Plan / Reach out. "Why Envoy" re-argues the same three benefits as differentiators. Three full screens, one idea, no new information, no escalation. A reader who scrolls past screen three learns essentially nothing until the CTA.

The deeper structural problem: **the argument is entirely assertive.** Every claim is a sentence promising something. Nothing on the page is *shown*. In a category where the mechanism is no longer novel (see market context), assertion alone can't carry it.

### Hierarchy & scanning

Size and weight are internally consistent — 9 font sizes, 4 weights, one family, which is disciplined. But hierarchy is *flat across sections*: every section is an eyebrow, a `clamp(2rem, 6vw, 3.25rem)` headline, a lead paragraph, and a list. Every section therefore claims exactly the same importance. Nothing is the most important thing on the page.

An F-pattern scan is impossible by construction. Mandatory scroll-snap with `scroll-snap-stop: always` forbids skimming — you cannot flick down the page to see what's here; you are forced through seven discrete stops in order. That is a fine choice for a narrative art piece and a poor one for a page whose visitor arrived from a friend's link and wants to know what this is in ten seconds.

At 1440×1024 the content column is 640–720px in a 1440px viewport, left-aligned, leaving the entire left half of the screen empty — not as considered negative space but as unresolved layout.

**Measured layout defect:** the "What is Envoy" panel is **929px tall in an 805px viewport** at 1440×900. It overflows its own snap point, so the `You're in control. Every message sends from your address only after you approve it.` reassurance — the single most trust-critical sentence on the page, and the one that most directly answers "why would I connect my Gmail to a startup I've never heard of" — is cut off below the fold and is easy to never see. Same defect at 375px (screenshot: `01-current-state/mobile/03-what-is-envoy.png`).

### Calls to action

Measured: **four** interactive elements on the entire page. Three are the identical button `Join the waitlist`; the fourth is a LinkedIn link in the footer.

They don't compete — the opposite problem. There is exactly one thing to do, it is the highest-commitment thing available, and it is offered before the visitor has been given a reason. And it is **high-friction**: `window.open(WAITLIST_URL, "_blank")` sends the visitor off-site to a third-party Fillout form in a new tab. That is a hard context switch at the exact moment of intent, it is exposed to popup blocking, and the form is not styled as Envoy.

What's missing is any low-commitment action — the page's own best line is "Start before you sign up," and there is nothing on the page you can start.

### Trust & proof

Measured: none. Zero testimonials, zero logos, zero counts, zero press, zero named humans, zero screenshots, no About, no privacy policy link, no company detail beyond `© 2026 Envoy` and a LinkedIn URL.

I am not proposing to invent any of this. But the *absence* is a specific problem here rather than a generic one, because the product's central ask is **OAuth access to the visitor's personal email account**. That is one of the most sensitive permissions a consumer product can request. The page's entire answer to it is a single sentence — the good one, "You're in control. Every message sends from your address only after you approve it" — which, per the finding above, is *rendered below the fold in an overflowing panel*. The most important trust sentence on the page is the one most likely to go unread.

### Copy quality

Better than average, and salvageable — this is real material, not filler. Sentences are short and readable. Two lines are genuinely good and should survive into any direction: *"Projects fail in the messy middle"* and *"Not post-and-wait."*

Weaknesses:
- **Register mismatch.** `commercial build-outs`, `every trade and category`, `AV`, `providers`, `multi-vendor project`, `project hub`. Accurate; cold. This is the largest single contributor to "masculine and technical."
- **Universality that reads as vagueness.** `Plan any project`, `Anyone running a multi-vendor project`, `any multi-vendor project`. Three claims of everything.
- **Feature-speak in the middle third.** "Discover contacts," "Organize your project," "Send outreach" are labels for UI, not outcomes for a person.
- **The hero misrepresents the mechanism** ("*We* line up the vendors" — you do, with help).
- **Nothing is concrete.** Not one specific vendor category appears above the fold; no number, no timeframe, no example project anywhere on the page.

### Visual craft

Type is the strongest part: one family (Instrument Sans), 9 sizes, 4 weights, consistent `-0.03em` display tracking. Spacing is systematic (`clamp()`-based padding, a single `0.5rem` radius). This is a competently built page.

The problems are in colour and imagery:
- **The palette is one hue.** `#003fb3` primary, `#7191f7` mid, `#dde7fe` text, `#061228` ground. All blue, all cold, high-saturation electric. There is no warm tone anywhere, no secondary, no accent. Combined with the grain and the near-black field, this reads as developer-tool/crypto/aerospace — which is precisely the "masculine and technical" note.
- **There are no images at all.** Zero `<img>` elements. The only visual content on the page is an animated WebGL gradient and a logo rendered as a CSS mask. For a product whose subject matter is *weddings, renovations and events* — three of the most visually rich domains that exist — this is a remarkable omission and probably the single biggest missed opportunity on the page.
- **The decorative background is the heaviest thing on the site.** Measured: `assets/shader-bg.js` is **1.54 MB uncompressed / 353 KB gzipped**, and it bundles **React** to render a background gradient on an otherwise static page. It is ~55% of total page weight and 100% decorative.
- **Buttons have a skew-transform hover wipe** that is fussy against otherwise restrained typography.

### Mobile experience

At 375px nothing breaks catastrophically — the layout reflows, type scales via `clamp()`, the footer grid collapses to one column. Real issues:

- The **"What is Envoy" panel overflows the snapped viewport** (as at desktop), cutting the "You're in control" note. Screenshot: `01-current-state/mobile/03-what-is-envoy.png`.
- **Mandatory scroll-snap is materially worse on touch.** Seven forced full-screen stops with `scroll-snap-stop: always` means seven deliberate swipes minimum with no ability to overscroll or skim, on the device where skimming matters most.
- The **floating "Join the waitlist" button sits fixed over content** at the top-right for the entire scroll, overlapping the eyebrow row on several panels at 375px.
- `100dvh` panels plus mobile browser chrome means the first panel's content sits high with a large dead zone below.

### Performance & basics

- **Total transfer: 643 KB over 14 requests.** `shader-bg.js` at 353 KB gzipped is the majority of it. HTML is 26 KB. DOMContentLoaded 570 ms on a fast connection — fine, but the shader is the payload most at risk on a phone on cellular, and it is decorative.
- **`og-image.png` is 5.44 MB.** This is a genuine bug, not a nitpick: it's a 2400×1260 PNG, and at 5.4 MB it sits at or above the size ceiling several platforms enforce for link unfurls. For a product whose only distribution channel right now is people sharing a link, a share image that may silently fail to render is expensive. Should be a compressed JPEG/WebP well under 1 MB.
- **`robots.txt` and `sitemap.xml` both 404.** Meta description, OG and Twitter card tags are all present and well-written.
- **No console errors.** Clean.
- **No `<nav>` and no `<header>`** anywhere in the document — the only landmarks are `main`, seven unlabelled `section`s, and `footer`. Sections have no accessible names.
- The `<h1>` renders as `Plan any project.We line up the vendors.` to assistive tech — a `<br/>` with no surrounding whitespace, so screen readers announce "project.We".
- **Text contrast fails WCAG AA, measurably.** I sampled the actual rendered background beneath each text run (text hidden, background captured, per-pixel contrast computed against the real composited text colour). Worst-case ratios found:

  | Text run | Colour | Worst | Average |
  |---|---|---|---|
  | Hero lead paragraph, 20px | `rgba(221,231,254,.72)` | **1.40:1** | 6.08 |
  | "What is Envoy" lead, 20px | `rgba(221,231,254,.72)` | **1.26:1** | 5.97 |
  | Feature body copy, 15px | `rgba(221,231,254,.72)` | **1.41:1** | 7.18 |
  | Step body copy, 15px | `rgba(221,231,254,.72)` | **1.31:1** | 6.21 |
  | Eyebrow labels, 12px/600 | `#7191f7` | **1.00:1** | 4.48 |
  | Problem list items, 15px | `#dde7fe` | 1.57:1 | 12.97 |

  The AA floor is 4.5:1 for body text. The averages pass; the minimums fail badly, because the shader drives bright cyan and green regions (sampled: `rgb(0,196,238)`, `rgb(8,217,199)`, `rgb(1,206,3)`) directly beneath text. **And the background animates continuously**, so this is not a fixed defect at one spot — every paragraph on the page periodically sits over a region where it is effectively illegible. The existing `readability-scrim` is too weak to prevent it. Focus states and `prefers-reduced-motion` handling, to the page's credit, are properly implemented.

---

## The three problems that matter

### 1. The page is written for procurement, and the customer is planning a wedding

This is first because it is the cause of the symptom your friend actually named, and because it is upstream of every other fix. "Masculine and technical" is not primarily a colour problem — it is `commercial build-outs`, `every trade and category`, `providers`, `AV`, `multi-vendor project`. The page's most emotionally intelligent line, *"Projects fail in the messy middle,"* proves the understanding is there; the rest of the page then translates it into facilities-management English.

Meanwhile the actual lead use case is mentioned twice, below the fold, fourth in a list. The page hedges across four audiences and therefore commits to none, and the neutral register that results *is* the technical register — technical is what you sound like when you refuse to pick a person.

Fix this and three things move at once: the warmth problem, the "who is this for" problem, and the differentiation problem — because "the tool for coordinating every vendor for one irreplaceable date" is an unoccupied position, and "a project hub for multi-vendor projects" is not a position at all.

**This is the one I most want to argue with you about, because it's the one with a real cost:** committing the page to weddings narrows it. My read is that the narrowing is worth it — renovation and event language generalises *out* of a wedding page far more easily than warmth generalises *into* a procurement page, and a pre-launch product with one distribution channel needs to be unmistakably for someone. But you know the founder and I don't, so this is the first thing I want your ruling on.

### 2. The page tells; it never shows — and gives no reason to believe

Zero images. Zero product UI. Zero proof of any kind. Every claim on the page is a sentence asserting a capability, on a page asking for an email address, from a company with no visible track record, for a product whose core action is **connecting your personal inbox**.

Every competitor reviewed shows the product or its output above the fold. The mechanism Envoy describes — AI vendor matching plus assisted outreach — is, per the 2026 category coverage, no longer novel enough to sell on description alone. Two people can write the same paragraph; only one can show the thing working.

We do not have testimonials and I will not invent any. But "show" is not the same as "social proof," and most of the gap is closable with things that either exist or can exist honestly: the actual product interface, a concrete worked example (one real project, its real vendor categories, a real draft email), specificity instead of abstraction, and giving the trust sentence — *"Every message sends from your address only after you approve it"* — the prominence its importance deserves rather than burying it in an overflowing panel.

### 3. Seven full-screen slides is a format that forbids the thing visitors need to do

The scroll-snap deck is the page's most distinctive craft decision and its most costly one. It enforces a linear, one-idea-per-screen march through seven stops with `scroll-snap-stop: always`, which makes skimming structurally impossible — on a page whose typical visitor arrives cold from a friend's link and wants to know what this is in ten seconds. It flattens hierarchy, because seven identically-formatted screens all claim equal weight. It produces the redundancy in problem 2's neighbourhood — sections 3, 4 and 5 say the same thing three times because the format demanded three screens' worth of content. It creates the overflow bug that hides the trust sentence. And its animated backdrop is 55% of page weight, drives the measured AA contrast failures, and ships React to draw a gradient.

I'd rather not frame this as "the shader is bad" — the page has genuine visual presence and that's worth something, especially for a founder-shared link. The problem is that presence is currently spent *instead of* information rather than *in service of* it. The redesign should keep some of the atmosphere and stop letting it set the information architecture.

**Ranked deliberately:** #1 changes who the page is for, #2 changes whether they believe it, #3 changes whether they get far enough to do either. If only one could be fixed, fix #1.

---

## Questions for you at Checkpoint 1

1. **Wedding-first, or not?** The biggest fork in the project. Options as I see them: (a) fully wedding-led — hero, imagery, examples, vocabulary all weddings, other project types present but secondary; (b) wedding-led hero with an explicit "also renovations, events, build-outs" move early; (c) stay horizontal, fix warmth through tone and craft only. I recommend (b) — it commits hard enough to be for someone without foreclosing the founder's broader ambition. Tell me if the founder would reject (a) or (b) outright.
2. **Is "we line up the vendors" a promise the product actually keeps?** I've read the mechanism as *you* reach out, with Envoy's help. If Envoy does more autonomous outreach than I think, that changes the hero significantly.
3. **Can I get product screenshots, or app access?** Problem 2 is largely unsolvable without something real to show. If the app exists in any state, even rough, screenshots would change what's possible. If not, I'll design honest placeholders for the shape of what's needed.
4. **Is the Fillout waitlist form fixed, or can the form be inline?** Keeping people on the page at the moment of intent is a cheap, meaningful win, but it may not be ours to change.
5. **Do you accept my ranking, or reorder it?** Everything downstream hangs off these three.
6. **Two things I'd fix regardless of direction, today:** the 5.44 MB OG image, and the panel overflow hiding the "You're in control" sentence. Say the word and I'll note them as immediate fixes for your friend independent of the redesign.

---
---

# Checkpoint 1 — corrections, rulings, and new evidence

*Added 2026-08-25 after designer review. The brief above is preserved as written; this section overrides it where they conflict.*

## Rulings

**1. Wedding-led is rejected.** The page stays horizontal. Warmth and specificity get earned a different way: a **case studies section**, ordered **wedding → home improvement → a third project type**, plus a wholesale change of register.

This is a better answer than mine and it changes the shape of Problem 1 without weakening it. My diagnosis — that the page is written in procurement English and hedges across four audiences — stands. My proposed fix was to narrow the audience; the ruling is to **stay broad but stop being abstract about it.** Those are different moves. Abstraction, not breadth, is what makes the page cold: "Anyone running a multi-vendor project" is abstract, whereas "an outdoor wedding for 150 in the fall / a 1920s kitchen renovation / a company offsite for 40" is broad *and* concrete, and it lets a visitor self-identify in one second without the page ever having to pick a winner.

So **Problem 1 is re-stated as:** *the page is abstract where it should be concrete, and written in procurement English.* The fix is register plus worked examples, not narrowing. Weddings lead the case studies because that's the strongest use case — they carry the emotional register the whole page needs — but the hero stays for everyone.

Usefully, the demo app has already reached the same conclusion independently: its hero offers exactly three example chips — *Outdoor wedding for 150 guests in fall*, *Renovate a 1920s kitchen*, *Company offsite for 40 people*. Same three slots, same order. The third case study should be the offsite/event unless you'd rather it were something else.

**2. The hero does not overpromise — and the live page actually UNDERSELLS.** Correction to my reading. Envoy finds the vendors, drafts the message, **and communicates with them on your behalf.** "We line up the vendors" is accurate, and it is if anything modest.

This inverts a finding in the audit above. I flagged *"the hero oversells agency and undersells the product's actual promise"* — wrong, and the error runs the other way. The live page's own description, "Draft, review, and send from your connected Gmail or Microsoft inbox," reads as a **manual** compose-and-send tool with AI assistance. That is a materially smaller product than the real one. The most differentiated thing Envoy does — it handles the correspondence for you, in your voice, and the replies come back to you — is described on the live page in language that makes it sound like a mail merge.

The demo says it far better, and this is sanctioned copy: *"Envoy reaches out for you"*, *"Outreach is written in your voice and sent on your behalf. You stay in full control of tone and what gets sent"*, *"Delegate outreach without losing your voice"*, and the tagline *"Your digital representative for outreach."*

**Consequence for the redesign:** "delegation without loss of control" becomes the spine of the page. It is the only claim here that no competitor can make — Thumbtack and The Knot route your request into a marketplace; Envoy acts as *your* representative from *your* inbox. Note that the name finally makes sense in this framing, which the current page never lets it do.

**3. Ranking accepted** — with Problem 1 re-stated per the ruling above.

## New evidence: the demo app (mockvoy.lovable.app)

Publicly browsable without login: `/`, `/how-it-works`, `/vendors`, `/pricing`, `/pros`, `/login`. All captured to `01-current-state/product/`. Signed-in views pending.

**a. The demo's own meta description is sharper than the live site's**, and names weddings first:

> "Describe your project and Envoy lines up the right vendors, then handles outreach for you. Plan weddings, renovations, and events faster."

**b. The demo hero is search-first.** A plain-language project field plus a location field plus three example chips — you use the product before you sign up. The live site *claims* "Start before you sign up" in body copy and delivers nothing you can start. The demo delivers it. **The redesigned landing page should adopt this hero.** It is simultaneously the fix for Problem 2 (show, don't tell), the fix for the CTA problem (a low-commitment first action), and the strongest possible demonstration of the mechanism.

**c. The lineup output is the product's best moment and the page has never shown it.** Describing a project returns a reasoned, category-by-category vendor lineup — Venue, Caterer, Event Rental, Wedding Planner, Photographer — each with a count ("13 found"), ranked vendor cards with location, price band and rating, and, critically, **a sentence explaining why that category is needed for this specific project**: *"Essential for securing a scenic Austin landscape that can accommodate 150 guests and provides a weather contingency plan."* That is the visible artifact of the thinking, and it is the single most persuasive thing Envoy has. It belongs above the fold.

**d. There is already a perfect low-commitment CTA in the demo:** *"Email me this lineup to finish later."* Value first, email second. This is far better than the live site's only option — leaving for an off-site Fillout form before you've been given a reason.

**e. Envoy is two-sided, which the live page never mentions.** There is a whole vendor/pro side: *"Envoy for Business — Win more work, without chasing leads,"* a pro dashboard, lead tracking, and Envoy replying on the vendor's behalf too. The live landing page's only acknowledgement is one sentence buried in the footer. Whether the redesigned page should surface this is a real scope question — see below.

**f. The product is LIGHT-themed.** The signed-in app and the login screen are white/soft-blue and distinctly friendlier than the marketing site's near-black shader. The current landing page is therefore not just cold in the abstract — **it misrepresents the product's own aesthetic.** Every visitor who converts experiences a jarring switch. This is a strong, non-taste-based argument for warming the page: it makes the site more faithful, not less.

**g. Real pricing exists** — Free / Pro $96 yr / Agency $200 yr per seat for planners; Basic free / Plus $250 yr / Premium $750 yr for vendors; "250 free credits, no card required." Framed as *"Free to plan. Pay only to automate."*

## Two content-integrity flags

**The demo contains a testimonial I will not reuse.** `/pros` carries *"Envoy replies to inquiries before I even open my laptop. We've booked three events this month from leads I would have missed." — Maya R., Event venue owner*, alongside stats *48h avg. time to first reply*, *4x more qualified leads*. This is a **mock app**; I am treating all of it as placeholder, not as real social proof, and none of it will appear on the redesigned page. If any of it is real, tell me and I'll use it verbatim. Otherwise it stays `[TESTIMONIAL — TBD]`.

**Demo vendor data is synthetic and visibly so** — an Austin wedding returns venues in Asheville NC, Charleston SC and Brooklyn NY, and vendor names are generated ("Iron Venue Union", "Lark Caterer Atelier"). Product screenshots therefore can't be dropped in raw as evidence. I'll handle this by rebuilding the lineup UI as a faithful, honest in-page component with plausible-but-clearly-illustrative content, labelled as such — never as a screenshot passed off as a live result.

**Pricing is from a mock app.** I won't put specific dollar figures on the landing page without your confirmation that they're the real intended numbers. *"Free to plan. Pay only to automate."* is safe and strong regardless.

## Questions carried to Checkpoint 2

1. **Third case study:** company offsite / corporate event, to match the demo's own three? Or something else — fundraiser, restaurant opening, milestone party?
2. **Does the vendor/pro side belong on this page?** It's a second audience with an opposite motivation, and putting it in the hero would re-create the exact hedging problem we're fixing. My recommendation: one clearly-signposted band low on the page ("Are you a vendor?") and nothing more. Say if the founder wants it weighted more heavily — it changes the page's structure.
3. **Is the demo pricing real?** If yes I can use it; if not, "Free to plan. Pay only to automate." stands alone.
4. **Is the Maya R. testimonial, or any of those stats, real?**
