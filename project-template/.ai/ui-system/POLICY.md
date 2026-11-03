# Bilingual UI contract — version 1.0

Contents: [Scope](#mandatory-scope-and-precedence) · [Workflow](#required-workflow) ·
[Languages](#languages-fonts-and-direction) · [Components](#components-and-geometry) ·
[Themes](#light-and-dark-themes) · [Accessibility](#accessibility-and-responsive-behavior) ·
[Acceptance](#acceptance-matrix-and-evidence) · [Sources](#documentation-references)

## Mandatory scope and precedence

Apply this contract to every first-party user interface: new screens, edits, components,
styles, forms, dashboards, navigation, responsive behavior, and UI reviews.
Before coding, read this policy and the relevant references. Use the installed
`bilingual-ui-system`, `ui-component-contract`, `ui-persian-english`, and `ui-light-dark`
skills when available. The portable policy covers the same requirements if the host
cannot load skills. Do not silently skip the requirements for small UI edits.
Backend-only work does not require UI implementation. Follow host instruction
precedence; these project rules do not override system instructions or explicit
user changes. Record explicit user exceptions in the project design decisions.

## Required workflow

1. Inspect the existing stack, design system, component inventory, CSS entrypoints,
   locale routing, theme handling, tests, and applicable nested instruction files.
2. Create or update `.ai/ui-system/DECISIONS.md`: component locations, token locations,
   typography assets, locale strategy, theme preference/resolution, and exceptions.
   Use existing equivalents rather than creating a second design system.
3. Use shared components and central semantic tokens. Adapt the supplied examples
   to the stack; installing this policy does not import CSS into an application.
4. Implement both locales and themes for the changed flow, including all states.
5. Verify the acceptance matrix. Report completed checks, exact evidence and blockers.
   Never describe unexecuted browser checks, font checks or accessibility checks as passed.

## Languages, fonts and direction

| Context | Root locale | Root direction | Font |
| --- | --- | --- | --- |
| Persian | `fa` or `fa-IR` | `rtl` | licensed IranYekan, family `IranYekan` |
| English | `en` or approved English tag | `ltr` | system sans-serif by default |

- Set both `lang` and `dir` on the HTML root in the server-rendered document.
  Update both on locale changes, including layout and portal content.
- Never simulate RTL using text alignment, CSS `direction` alone, transforms, or
  an unconditional `row-reverse`. Use logical margin/padding/inset/border properties,
  `text-align: start` for UI controls, logical table alignment and sensible
  DOM/focus order. Apply the prose justification rule below to running text.
- Justify multi-line prose in both Persian and English (`text-align: justify`),
  with `text-align-last: start` so the last line follows RTL/LTR. Apply a shared
  prose class to explanatory text, paragraphs, article/list prose and long dialog
  descriptions, not to the document root or every UI element. Keep headings,
  buttons, labels, navigation, placeholders, short messages, table cells and code
  at their appropriate logical alignment. Never add manual spaces, letter spacing
  or kashida characters to force justification. Inspect narrow layouts, mixed
  content and both themes for excessive gaps or clipped text; record a scoped
  readability exception if justification becomes unreadable.
- Use IranYekan for every Persian UI surface: forms, buttons, dialogs, toasts,
  tooltips, tables and chart labels. Do not silently substitute Vazirmatn.
  Load actual licensed self-hosted files with correct weight descriptors.
  Missing files are a font acceptance blocker; use a temporary fallback only while
  reporting that blocker. Do not obtain or redistribute proprietary font files.
- Set Latin phrases with explicit English language metadata when appropriate.
  Isolate identifiers, email addresses, URLs, phone numbers, code and file paths
  with `dir="ltr"` and `bdi`/isolating containers. Render unknown user text with
  `dir="auto"`/`bdi`. Do not force all inputs to RTL.
- Mirror directional navigation icons and placement (previous/next, breadcrumbs,
  sidebar docking) by meaning; do not mirror logos, media controls, charts, digits,
  photos or non-directional icons indiscriminately.
- Keep readable source and focus order. Localize table columns and keyboard
  behavior intentionally. A dialog rendered in a portal must inherit or receive
  the active locale, direction and theme.
- Keep complete message dictionaries, including errors, placeholders, tooltips,
  accessible names and empty states. No concatenated translated fragments.
- Format presentation values via `Intl.NumberFormat` / `Intl.DateTimeFormat` with
  explicit locale, timezone, calendar and currency decisions. Persian UI numerals
  may be Persian, but API/storage identifiers remain canonical and unmodified.
  Never assume Persian language alone determines calendar or backend timezone.
- Preserve route, data, field values, focus and scroll as appropriate when changing
  language. Persist supported locale preference independently from theme.

## Components and geometry

- Separate foundations (tokens, typography, locale/theme) from UI primitives,
  composed patterns, domain components and pages. Keep existing stack conventions.
- Reuse or extend existing primitives first. Do not duplicate button/input/dialog
  markup and styling per page or introduce a parallel UI library without need.
- Use explicit, typed APIs for `variant`, `size`, `state` and meaningful content.
  Avoid contradictory booleans, overloaded components and arbitrary page CSS patches.
- Every interactive primitive specifies default, hover, active, focus-visible,
  disabled and loading behavior. Inputs also specify invalid, read-only and help
  text states. Patterns specify empty, loading, error, success and long-content states.
- Use a single radius scale and role mapping. In new systems use:

| Token | Value | Role |
| --- | --- | --- |
| `--radius-none` | `0` | flush structural surfaces |
| `--radius-sm` | `4px` | small inner details |
| `--radius-control` | `8px` | buttons, inputs, selects |
| `--radius-surface` | `12px` | cards, menus, popovers |
| `--radius-dialog` | `16px` | dialogs, drawers |
| `--radius-full` | `9999px` | badges, circular avatars |

- Existing coherent design tokens may be mapped to these roles once in the central
  contract. Do not introduce new radius literals in components. Consistency means
  a shared role mapping, not one radius for every object. Nested shapes must not clip
  focus rings or leave mismatched corners. Themes and languages share geometry.
- Define spacing, type, control heights, shadows, borders, focus, layering and
  breakpoints centrally. Use responsive layouts rather than fixed desktop widths.
  Start from 4px spacing units, 16px body text, and 40/44/48px control heights;
  keep legitimate existing product density with a recorded mapping.
- Scope app styling and reset rules. Do not override arbitrary third-party DOM with
  global selectors. Integrate library tokens/themes and document necessary exceptions.

## Light and dark themes

- Support independent preference `light | dark | system` and resolved theme
  `light | dark`. Persist the preference, never the system-resolved result.
- Define every semantic color token explicitly in both themes: canvas, surface,
  elevated surface, text, muted text, border, control border, primary, on-primary,
  primary hover/active, success/warning/danger/info pairs, focus, overlay, disabled,
  selection, links and chart series. No missing-theme fallback hidden by inheritance.
- Share token names across themes. Components consume semantic tokens; forbid raw
  color values, palette utility colors and theme-specific page patches in first-party
  UI files outside designated token assets. Do not use filter inversion for dark mode.
- Resolve initial theme before first paint using a server cookie or an approved
  bootstrap compatible with the product CSP. Avoid a flash of the wrong theme and
  hydration mismatches. Set `color-scheme` to match native controls.
- Honor system changes only when preference is `system`; explicit choices override
  system settings. Handle blocked storage, invalid stored values and cleanup of
  media listeners. In SSR, do not access browser APIs during server rendering.
- Theme must cover native controls, autofill, disabled states, scrollbars where
  supported, portals, tooltips, tables, charts, skeletons, dialogs and toasts.
- Theme and language are independent; toggling either must not reset the other or
  clear user data. Keep focus on the switch after a change and announce its state.

## Accessibility and responsive behavior

- Target WCAG 2.2 AA. Normal text contrast >= 4.5:1; large text >= 3:1.
  Essential control boundaries, state indicators and focus indicators must reach
  >= 3:1 against adjacent colors where required. Measure actual pairs per theme
  and interaction state; a token sample is not an accessibility certification.
- Use semantic HTML, visible labels, associated error text, keyboard operation,
  focus-visible treatment, accessible names, and dialogs with focus management.
  Do not convey status by color alone. Distinguish read-only and disabled controls.
- Use at least 24x24 CSS px targets or adequate spacing under WCAG exceptions;
  prefer 44x44 for touch. Support reduced motion and forced-colors modes.
- Check at 360, 768 and 1440 CSS px and at 200% zoom. Also verify reflow at
  320 CSS px (or equivalent 400% zoom). Allow intentional table/code scrolling;
  avoid horizontal scrolling of the entire page.
- Accommodate Persian line height, diacritics, long English text, 2-line controls,
  large numbers and bidirectional mixed content without clipping.

## Acceptance matrix and evidence

| Locale/theme | Required verification |
| --- | --- |
| `fa / light` | root attrs, computed IranYekan, RTL geometry, states, keyboard |
| `fa / dark` | same checks plus semantic contrast and overlay/chart behavior |
| `en / light` | LTR, English font, full translations, responsive behavior |
| `en / dark` | same checks plus semantic contrast and overlay/chart behavior |

For each changed flow inspect short/long text, missing data, validation errors,
loading, empty/error/success, disabled controls, focus and keyboard operation.
Capture screenshots in all four combinations at relevant viewports, inspect them,
and record routes, browser, viewport, checks, results and outstanding issues in the
project QA record. Use the host-approved browser/testing tool. Add meaningful tests
for theme preference resolution, locale switching and shared component behavior
where appropriate; do not claim these follow from a static scanner.

Run `python3 .ai/ui-system/check_ui.py --root .` as a limited static guard. Its scope
is literal colors, literal radii, selected physical CSS properties and common utility
classes in configured UI paths. It cannot certify computed layout, runtime themes,
translations, focus or accessibility. Configure `guard.json` for actual UI folders,
central token files, vendor/generated assets and documented exceptions.
Do not mark UI work complete with failed mandatory checks. If environment or font
assets prevent a check, deliver work with the exact blocker and pending checks.

## Documentation references

- Codex instructions: https://developers.openai.com/codex/guides/agents-md/
- Cursor project rules: https://cursor.com/docs/rules
- Claude project memory: https://code.claude.com/docs/en/memory
- Gemini CLI context: https://geminicli.com/docs/cli/gemini-md/
- Copilot instructions: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
- HTML direction: https://www.w3.org/International/questions/qa-html-dir
- Contrast: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html

Instruction adapters request compliance within each supporting host. They cannot
force an arbitrary AI service to load files or override its instruction hierarchy.
For merge enforcement, connect the guard and actual browser tests to the project's
CI, then configure required branch checks through the repository owner.
