---
name: ui-persian-english
description: Implement or review Persian and English UI localization, IranYekan font loading, strict RTL/LTR, mixed bidirectional content, logical CSS and localized formatting. Use whenever creating or editing UI text, layout, navigation, forms, tables, dialogs or locale switching.
---

# Persian and English UI

Read [bidi.md](references/bidi.md). Apply the `bilingual-ui-system` policy when
available, or the project `.ai/ui-system/POLICY.md` portable copy.

1. Determine supported locale tags and locale routing before implementation.
2. Render Persian root HTML with `lang=fa`, `dir=rtl`; render English with
   `lang=en`, `dir=ltr`. Update both on switching; preserve current user work.
3. Load licensed IranYekan regular/medium/bold with correct weight descriptors and
   verify computed fonts on all Persian surfaces. Report missing font assets as
   blocked. Use English system sans-serif for English UI, including scoped phrases.
4. Use logical CSS and DOM order. Mirror only directional affordances. Isolate
   Latin identifiers and unknown mixed content; never reverse strings or all icons.
   Justify multi-line prose in both locales with `text-align-last: start`; keep
   headings, controls, short labels, table cells and code at logical alignment.
5. Localize all visible and accessible messages. Decide display numbers, calendar,
   currency and timezone explicitly; leave stored/API identifiers unchanged.
6. Verify real Persian, long English and mixed-content flows in both themes,
   mobile/desktop, keyboard navigation and portal content.
