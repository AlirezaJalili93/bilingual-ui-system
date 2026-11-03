<div dir="rtl" lang="fa">

# نمونهٔ متن توضیحی دوزبانه

این قطعه نمونهٔ ادغام است و اپلیکیشن آماده نیست. CSS اصلی باید در برنامه بارگذاری شده باشد.

```html
<!-- Persian document: <html lang="fa" dir="rtl" data-theme="light"> -->
<section lang="fa" dir="rtl" aria-labelledby="fa-heading">
  <h2 id="fa-heading">گزارش عملکرد</h2>
  <p class="ui-prose">
    این متن توضیحی در چند خط نمایش داده می‌شود و باید در دو طرف تراز باشد.
    شناسهٔ گزارش <bdi dir="ltr">REPORT-2026/1042</bdi> است.
  </p>
  <label for="report-email">ایمیل دریافت گزارش</label>
  <input id="report-email" class="ui-control" type="email" dir="ltr">
</section>

<!-- English document uses lang=en and dir=ltr on its HTML root. -->
<section lang="en" dir="ltr" aria-labelledby="en-heading">
  <h2 id="en-heading">Performance report</h2>
  <p class="ui-prose">
    This explanatory paragraph uses justified text while its last line remains
    aligned to the start edge of the English reading direction.
  </p>
</section>
```

در محصولی که یک زبان فعال دارد، ویژگی‌های root را مطابق همان زبان تنظیم کنید.
این نمونهٔ دو بخش کنار هم فقط تفاوت رفتار زبان‌ها را نشان می‌دهد.

</div>
