---
name: ui-component-contract
description: Create, refactor or review reusable UI components, design tokens, visual variants, consistent border radii and responsive layouts. Use for every component or styling change, paired with bilingual-ui-system, for Persian/English and light/dark parity.
---

# UI Component Contract

Read [components.md](references/components.md). Apply the `bilingual-ui-system`
policy when available, or the project `.ai/ui-system/POLICY.md` portable copy.

1. Inventory existing primitives, component libraries and all call sites affected.
2. Map foundations -> primitives -> patterns -> domain components -> pages using
   the existing stack. Prefer composition over duplicate markup and page patches.
3. Define or reuse semantic color, spacing, type, sizing, focus and radius tokens.
   In new systems use control 8px, surface 12px, dialog 16px, full 9999px.
   Map a coherent existing scale centrally; never scatter radius literals.
4. Give variants and states an explicit API. Preserve semantic HTML, labels,
   keyboard interaction and focus behavior. Do not introduce a second UI library.
5. Check all affected shared-component uses in both languages and themes, including
   long text, loading/error/empty states, touch, 320px reflow and reduced motion.
6. Report the reused/changed components, token mapping and actual verification.
