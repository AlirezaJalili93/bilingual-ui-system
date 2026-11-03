---
name: ui-light-dark
description: Create, edit or audit explicit light and dark UI themes, semantic color tokens, system preference, persistence, first-paint behavior, accessible contrast and component states. Use for any visual UI change, theme switcher, dark mode issue, charts, overlays or theme provider integration.
---

# Light and Dark UI

Read [themes.md](references/themes.md). Apply the `bilingual-ui-system` policy
when available, or the project `.ai/ui-system/POLICY.md` portable copy.

1. Inventory semantic tokens, theme providers, portal mounts and initial rendering.
2. Define the same complete semantic token set explicitly for light and dark.
   Use component token references only; never invert the page or patch per screen.
3. Separate preference `light|dark|system` from resolved `light|dark`. Persist
   preference, respond to system changes only in system mode, and handle storage
   failures and unsupported values. Keep locale and theme independent.
4. Resolve theme before paint using a CSP-compatible bootstrap or server cookie.
   Handle SSR/hydration coherently; set native `color-scheme` correctly.
5. Check all interaction states, native controls, portals, tables and charts in
   both locales. Measure actual contrast; do not infer it from token names.
6. Verify refresh, preference changes, system changes, blocked storage and focused
   controls. Report measured checks and any pending browser verification.
