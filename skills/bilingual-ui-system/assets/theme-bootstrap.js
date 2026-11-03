/* Browser-only pre-paint reference. Integrate with your CSP and SSR strategy. */
(function () {
  'use strict';
  if (window.uiTheme) return;
  var key = 'ui.theme.preference';
  var valid = function (x) { return x === 'light' || x === 'dark' || x === 'system'; };
  var media = window.matchMedia('(prefers-color-scheme: dark)');
  var preference = 'system';
  try {
    var saved = window.localStorage.getItem(key);
    if (valid(saved)) preference = saved;
  } catch (_) { /* private mode / blocked storage: keep in-memory preference */ }
  function resolved() { return preference === 'system' ? (media.matches ? 'dark' : 'light') : preference; }
  function apply() {
    var root = document.documentElement;
    root.dataset.theme = resolved();
    root.dataset.themePreference = preference;
    root.style.colorScheme = resolved();
    window.dispatchEvent(new CustomEvent('ui-theme-change', {
      detail: { preference: preference, resolved: resolved() }
    }));
  }
  function onSystemChange() { if (preference === 'system') apply(); }
  function onStorage(event) {
    if (event.key !== key && event.key !== null) return;
    preference = valid(event.newValue) ? event.newValue : 'system';
    apply();
  }
  if (media.addEventListener) media.addEventListener('change', onSystemChange);
  else media.addListener(onSystemChange);
  window.addEventListener('storage', onStorage);
  window.uiTheme = {
    getPreference: function () { return preference; },
    getResolved: resolved,
    setPreference: function (next) {
      if (!valid(next)) throw new TypeError('Expected light, dark or system');
      preference = next;
      try { window.localStorage.setItem(key, preference); } catch (_) { /* keep memory state */ }
      apply();
    },
    destroy: function () {
      if (media.removeEventListener) media.removeEventListener('change', onSystemChange);
      else media.removeListener(onSystemChange);
      window.removeEventListener('storage', onStorage);
      delete window.uiTheme;
    }
  };
  apply();
}());
