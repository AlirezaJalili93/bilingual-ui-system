<div dir="rtl" lang="fa">

# نمونهٔ استفاده از API تم

پس از اجرای bootstrap و فقط در محیط مرورگر:

```javascript
const currentPreference = window.uiTheme.getPreference();
const currentTheme = window.uiTheme.getResolved();

function onThemeChanged(event) {
  const { preference, resolved } = event.detail;
  // Update the existing UI store and accessible switch label.
}

window.addEventListener('ui-theme-change', onThemeChanged);
window.uiTheme.setPreference('system');

// Remove this subscriber when the owning UI is destroyed.
window.removeEventListener('ui-theme-change', onThemeChanged);
```

متغیرهای نمونه را با store/provider واقعی محصول هماهنگ کنید.
اسکریپت تم را در کد سمت سرور اجرا نکنید. در محصولی با مدیریت تم موجود،
دو منبع state موازی نسازید؛ قرارداد را با همان راهکار ادغام کنید.

</div>
