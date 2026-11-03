# Theme implementation and acceptance

## Resolution

| Preference | System | Resolved |
| --- | --- | --- |
| light | either | light |
| dark | either | dark |
| system | light | light |
| system | dark | dark |

Reject invalid persisted values and fall back to system. Do not overwrite system
preference with the resolved value. Subscribe to system changes only as needed;
remove listeners on teardown. Synchronize other tabs if the product supports it.
Never reset locale, inputs, data filters or scroll while switching theme.

## Required semantic families

Canvas/surface/elevated; text/muted/link; border/control-border; primary/on-primary/
hover/active; success/warning/danger/info foreground/background; focus; selection;
overlay; disabled foreground/background; skeleton; chart series and tooltip.
Map both themes explicitly. Reuse structure, density and radii between themes.
Use borders/elevation appropriate to each theme, rather than pure black/white swap.
Differentiate state with text/icons/pattern as well as color, especially charts.

## First paint and server rendering

Choose server cookie rendering, a pre-paint bootstrap or the established framework
provider. Record which owns theme. Respect CSP nonce/hash/external-script policy;
do not weaken CSP to run a theme script. Keep server markup and client hydration
consistent. Do not broadly suppress hydration warnings to hide unrelated errors.
Use `color-scheme` for native input controls; inspect autofill and date/select UI.

## Checks

- Measure normal text >=4.5:1; large text >=3:1; required non-text UI >=3:1.
  Include muted text, action text, focus, invalid fields, badges, chart labels and
  hover/active states. Distinguish decorative borders from essential boundaries.
- Verify selected and disabled states are still understandable, even where disabled
  elements are exempt from contrast requirements. Do not depend on opacity alone.
- Open dialogs/tooltips/toasts in each theme; verify overlays and stacking.
- Refresh direct links with light/dark/system choices; emulate OS changes in each
  preference, blocked localStorage, invalid persisted data and another-tab updates.
- Check four locale/theme combinations, 320px reflow, 200% zoom, reduced motion,
  keyboard focus and forced-colors behavior. Inspect screenshots before claiming pass.
