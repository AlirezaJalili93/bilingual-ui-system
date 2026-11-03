# Component decisions and checks

## Responsibilities

| Layer | Responsibilities | Exclude |
| --- | --- | --- |
| Foundations | tokens, typography, direction, theme | business requests |
| Primitives | button, field, label, menu, dialog | domain fetch logic |
| Patterns | form field, toolbar, pagination, data table | route-specific policy |
| Domain | market event row, user permissions editor | duplicated primitives |
| Pages | routing, data orchestration, page composition | one-off primitive styling |

Use the host framework's conventions; this is not a required folder tree.
Keep server/client boundaries and avoid turning an entire page client-side for one toggle.

## Required API behavior

- Buttons: native button type, variant/size, loading name, disabled interaction,
  visible focus, predictable icon spacing and submit behavior.
- Fields: stable id/label, description/error linkage, invalid state, required state,
  locale-aware text with LTR/auto exceptions, read-only vs disabled.
- Menus/popovers: positioning by logical start/end, correct keyboard semantics,
  outside dismissal, escape, focus restoration and portal providers.
- Dialogs: labelled modal, focus trap, Escape behavior, scroll containment, restored
  focus; long content remains reachable in both directions.
- Tables: semantic headers/cells, accessible sorting state, intentional logical
  alignment, loading/empty/error behavior, local horizontal scrolling on small screens.
- Toasts: localized meaningful message, appropriate live region, dismiss target,
  adequate duration for action, theme tokens and inherited direction/font.

Prefer variants such as `variant=primary|secondary|danger`, `size=sm|md|lg` and a
separate loading state over many conflicting boolean props. Adapt to existing APIs.
Use accessible library behavior rather than rewriting complex widgets casually.

## Geometry contract

Control=8px; card/menu/popover=12px; dialog/drawer=16px; pill/avatar=full; flush=0;
small inner detail=4px. Put these roles in tokens, preserve geometry across themes
and languages, and ensure adjoining pieces and nested surfaces align. Allow only
explicit centrally recorded exceptions. No arbitrary rounded utility values.

## Acceptance

Inspect visual variants and hover/active/focus/disabled/loading/invalid states in
all four locale/theme combinations. Use real Persian strings and long English
strings; check icon/text wrapping, line height and focus rings at component bounds.
Extend existing stories/examples when useful. Run the existing app checks and
meaningful shared behavior tests; do not create tests that merely repeat constants.
