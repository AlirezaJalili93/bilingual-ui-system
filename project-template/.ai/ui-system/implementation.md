# Applying the portable assets

- Treat `assets/tokens.css` as a framework-neutral baseline. Import its actual
  project copy once in the app entrypoint after adapting reset scope. Consolidate
  existing tokens first. Never import a second conflicting design system.
- Its IranYekan `@font-face` paths are placeholders for licensed regular/medium/bold
  WOFF2 files under the public `/fonts` path. Adjust paths and weights to the actual
  licensed distribution; do not relabel a static font as variable.
- `assets/theme-bootstrap.js` is an early browser script example. Use an external
  render-blocking script, nonce/hash or server cookie approach according to the
  current CSP. Avoid `async`/`defer` for a bootstrap needed before first paint.
- The script exposes `window.uiTheme` to set preference and observe changes. For a
  real app, wrap it with the framework's provider/store, preserving a single source
  of truth. Do not access `window` from server components. Let the server initialize
  root attrs consistently if using cookies. Keep locale SSR-owned separately.
- Always initialize `lang` and `dir` in server HTML from supported locale routing;
  the theme bootstrap intentionally does not guess a locale from browser settings.
- For Tailwind, map semantic CSS variables to utilities; avoid raw `bg-white`,
  `text-gray-*`, `dark:bg-*` patches and arbitrary rounded values. Use logical
  spacing utilities. For component libraries, map theme and direction providers,
  portal roots, popover origins and keyboard semantics to the same contract.
- For charts, set explicit series colors per theme, label fonts per locale, number
  formatting, tooltip direction, sufficient contrast and non-color distinctions.
- Configure `guard.json` with source roots and exact token paths. Do not exclude an
  entire feature folder to hide errors. Record legitimate exceptions centrally.
- CI command: `python3 .ai/ui-system/check_ui.py --root .`. Combine it with the app's
  build, existing lint/type checks, keyboard/accessibility checks and four locale/
  theme browser projects. Make them required branch checks if the owner requests it.
- Instruction file loading varies by tool/configuration. Inspect effective loaded
  instructions, scoped rules and context limits in the selected host. For generic
  chat tools, provide POLICY.md explicitly. No text file guarantees model obedience.
