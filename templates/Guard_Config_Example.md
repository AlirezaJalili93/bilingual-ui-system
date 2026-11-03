<div dir="rtl" lang="fa">

# نمونهٔ تنظیم اسکنر

این فقط نمونهٔ پیکربندی است؛ مسیرها را با محصول خود تطبیق دهید.
کل پوشهٔ قابلیت را برای رفع ظاهری خطا کنار نگذارید.

```json
{
  "include": ["src"],
  "exclude": ["node_modules", ".git", "dist", "build", "coverage", ".next", "vendor", ".ai"],
  "token_files": ["src/styles/tokens.css"],
  "exceptions": [
    {
      "path": "src/charts/ThirdPartyBridge.css",
      "rule": "physical-css",
      "reason": "استثنای محدود برای API فیزیکی کتابخانه؛ با بررسی RTL تأیید شود"
    }
  ]
}
```

استثنا در این نسخه تمام یافته‌های همان rule در مسیر منطبق را کنار می‌گذارد.
اگر فایل نمونه در پروژه وجود ندارد، آن را بی‌دلیل به تنظیم واقعی اضافه نکنید.

```bash
python3 .ai/ui-system/check_ui.py --root . --config .ai/ui-system/guard.json
```

</div>
