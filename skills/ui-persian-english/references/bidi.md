# Bidirectional implementation

## Root and mixed content

```html
<html lang="fa" dir="rtl" data-theme="light">
  <body>
    <p>شناسه سفارش: <bdi dir="ltr">IFB-2026/1042</bdi></p>
    <label for="email">ایمیل</label>
    <input id="email" type="email" dir="ltr" autocomplete="email">
    <p><bdi dir="auto">user-provided content</bdi></p>
    <span lang="en" dir="ltr">Product dashboard</span>
  </body>
</html>
```

For English change the root to `lang=en dir=ltr`. Direction and language are
separate metadata: an LTR code identifier inside Persian UI need not change the
whole surrounding component's language. Use `bdi` to prevent adjacent punctuation
from jumping. Use `pre/code` isolation and local overflow for code blocks.

## Layout and behavior

Use `margin-inline-start`, `padding-inline`, `inset-inline-end`, `border-inline-start`,
`border-start-start-radius`, `inline-size` and `text-align: start/end` as appropriate.
Do not set root direction with CSS. CSS flex/grid respects document direction;
combine logical layout with tested DOM/focus order rather than double reversing.
A visually reordered layout must still have sensible keyboard and screen reader order.
Test arrow-key semantics against the chosen accessible widget library's RTL support.

Sidebar and breadcrumb direction follow locale. Align numeric/identifier columns
intentionally. Do not reverse chart time axes or table data by blanket rule.
Keep close, search, play/pause and brand icons unmirrored unless meaning demands it.
Portal content uses the same direction/theme providers or explicit root attrs.

## Prose justification

Apply the shared `.ui-prose` class directly to prose text blocks (paragraphs,
article/list prose and long descriptions), never to the HTML/body root, a page
wrapper or a whole widget. Use `text-align: justify`, `text-align-last: start`
and `text-justify: auto` in Persian and English. Root `dir` still determines
RTL/LTR and the last line's start edge. Single-line blocks must not be stretched.
Keep headings, buttons, navigation, labels, placeholders, table cells, short status
messages, identifiers and code at their appropriate logical alignment. Do not
force justification using manual spaces, letter spacing, inserted kashida or
`text-align-last: justify`. Verify Persian shaping, English word spacing and mixed
content at narrow widths and zoom in both themes. Record a scoped readability
exception if justification creates excessive gaps; never silently disable it globally.

## Typography and formatting

Use `IranYekan` for Persian, with fallback only while the actual licensed files
load or remain blocked. Do not substitute similarly named fonts or synthesize all
weights. Inspect network/font loading and computed fonts, not just CSS declarations.
Use body line-height around 1.75 in Persian and 1.5 in English, then check clipping
in buttons, fields and dense tables. Avoid Persian letter spacing and fixed line boxes.
Keep fonts in translated chart labels and canvas rendering aligned with the DOM.

Use `Intl` formatting with a recorded locale, calendar, timezone and currency.
Treat user-entered Persian/Arabic digits via explicit parsing rules if accepted;
do not mutate passwords, codes or API IDs with blanket digit conversion.
Use translation pluralization/interpolation rather than string concatenation.
Test punctuation, ZWNJ, negative amounts, percentages, dates, URLs, file names and
long translated errors. Keep accessible names in the active locale.

## Switch acceptance

Switch language on a form with unsaved data and an open dialog. Root attrs,
translations, layout, focus, portal font and current theme must remain coherent.
Repeat from each language and in both themes. Refresh/direct-route loads must
match the chosen locale without the wrong-direction first paint.
