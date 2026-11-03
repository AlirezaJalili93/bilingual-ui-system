---
name: bilingual-ui-system
description: Mandatory user interface workflow for creating, editing or reviewing websites, apps, dashboards, forms, components, CSS and design systems. Apply component-based design, unified radius tokens, Persian IranYekan RTL, English LTR, and separate light/dark themes. Use for every UI task, including minor UI fixes; coordinate ui-component-contract, ui-persian-english and ui-light-dark.
---

# Bilingual UI System

Read [POLICY.md](references/POLICY.md) before any UI implementation or review.
Treat its requirements as the user's default project UI contract, subject to host
instruction precedence and explicit user changes. Apply it to the changed flow;
do not rewrite unrelated product screens without authorization.

1. Inspect stack, components, styling, locale/theme handling and existing instructions.
2. Record the implementation mapping and explicit exceptions in project design decisions.
3. Invoke `ui-component-contract` for component and token work, `ui-persian-english`
   for content, fonts and direction, and `ui-light-dark` for visual states and themes.
   Find them by exact frontmatter name in the host skill registry; if unavailable,
   use POLICY.md directly and state the unavailable skill only when material.
4. Reuse the app's primitives. Map centralized radii to roles: controls 8px,
   surfaces 12px, dialogs 16px, pills full; preserve a coherent existing scale via
   one documented token mapping. No component-level radius or color literals.
5. Render Persian with `lang=fa`, `dir=rtl`, licensed IranYekan; render English with
   `lang=en`, `dir=ltr` and system sans-serif. Missing font files block font acceptance.
   Justify multi-line prose in both locales, with the last line aligned to start;
   retain logical alignment for headings, controls, table cells and code.
6. Implement semantic token sets separately for light/dark, with independent
   light/dark/system preference and locale choice.
7. Verify `fa/light`, `fa/dark`, `en/light`, `en/dark` with browser evidence and
   responsive, keyboard, interaction-state and contrast checks. Report pending
   checks honestly; do not equate scanner success with complete acceptance.

## Project rules installation

When the user asks to install mandatory project rules, use
`scripts/install_project_rules.py --project ABSOLUTE_PROJECT_PATH`.
Inspect existing instructions and run with `--dry-run` first. The installer merges
marked blocks without overwriting unrelated rules and refuses unmanaged file
collisions. It writes the portable policy, CSS examples, theme bootstrap, limited
static guard and adapters for AGENTS.md, CLAUDE.md, GEMINI.md, Cursor and Copilot.
It does not import assets, alter application source, enable platform settings or
configure required branch checks. Complete these steps within the authorized scope
when the user asks for application integration.

For a portable installer file, generate it with
`python3 scripts/export_rules_installer.py --output ABSOLUTE_OUTPUT_PATH`.
Export only the portable rules bundle, not personal skill folders.

Read [implementation.md](references/implementation.md) when adapting the supplied
assets to a stack or integrating checks into CI.
