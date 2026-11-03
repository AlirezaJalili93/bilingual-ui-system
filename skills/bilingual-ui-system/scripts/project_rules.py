"""Build portable project rules without exporting personal skill directories."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile

ADAPTER = '''# Mandatory bilingual UI workflow

For every UI task, read `.ai/ui-system/POLICY.md` before editing and follow it.
Use the `bilingual-ui-system`, `ui-component-contract`, `ui-persian-english` and
`ui-light-dark` skills when available; otherwise use the portable policy and its
component, bidi and theme references. Backend-only tasks need no UI work.

MUST: shared components and semantic tokens; one radius role mapping; Persian
`lang=fa dir=rtl` with licensed IranYekan; English `lang=en dir=ltr` with system
sans-serif; logical CSS and isolated mixed text; explicit light/dark token sets
with independent light/dark/system preference; accessible keyboard/focus states.
MUST: justify multi-line Persian and English prose with the last line aligned to
start; preserve logical alignment for headings, controls, tables and code.

MUST: inspect existing conventions, document token/locale/theme mappings, and
verify fa/light, fa/dark, en/light, en/dark for changed flows, including responsive
layout and all states. Run the configured static guard plus applicable app/browser
checks. Report actual evidence and blockers; never claim unexecuted checks passed.
Read `.ai/ui-system/POLICY.md` for exact acceptance, typography and contrast rules.
Do not complete UI work with failed mandatory checks or silently bypass this policy.
Follow host instruction precedence and explicit user changes; document exceptions.
'''
BEGIN='<!-- bilingual-ui-system:begin -->'
END='<!-- bilingual-ui-system:end -->'
ENGINE=r'''
def install(payload):
    parser=argparse.ArgumentParser(description='نصب قواعد رابط کاربری فارسی/انگلیسی در پروژه؛ فایل‌های نامرتبط حفظ می‌شوند.')
    parser.add_argument('--project',required=True,type=Path,help='Existing project directory / پوشه پروژه')
    parser.add_argument('--dry-run',action='store_true',help='Show changes without writing files')
    args=parser.parse_args();root=args.project.resolve()
    if not root.is_dir():
        parser.error('Project must be an existing directory')
    def safe_path(rel):
        path=root/rel
        if any(p.is_symlink() for p in [path,*path.parents] if p != root and root in p.parents):
            raise ValueError('Refusing symlink destination: '+rel)
        if any(p.exists() and not p.is_dir() for p in path.parents if p != root and root in p.parents):
            raise ValueError('Parent is not a directory: '+rel)
        return path
    def digest(value):
        return hashlib.sha256(value.encode('utf-8')).hexdigest()
    def merge(old,block):
        if old.count(BEGIN)!=old.count(END) or old.count(BEGIN)>1:
            raise ValueError('Malformed managed instruction block')
        new=BEGIN+'\n'+block.strip()+'\n'+END
        if BEGIN in old:
            a=old.index(BEGIN);b=old.index(END)
            if b<a: raise ValueError('Malformed instruction marker order')
            return old[:a]+new+old[b+len(END):]
        return old+('' if not old else '\n\n')+new+'\n'
    writes={}
    try:
        mp=safe_path('.ai/ui-system/manifest.json')
        manifest=json.loads(mp.read_text(encoding='utf-8')) if mp.exists() else {}
        if not isinstance(manifest,dict) or not isinstance(manifest.get('files',{}),dict):
            raise ValueError('Invalid existing manifest')
        for rel,content in payload.items():
            p=safe_path(rel)
            if p.exists():
                old=p.read_text(encoding='utf-8')
                if old!=content and digest(old)!=manifest.get('files',{}).get(rel):
                    raise ValueError('Unmanaged or locally modified file; merge manually: '+rel)
            writes[rel]=content
        for rel in ['AGENTS.md','CLAUDE.md','GEMINI.md','.github/copilot-instructions.md']:
            p=safe_path(rel);old=p.read_text(encoding='utf-8') if p.exists() else ''
            writes[rel]=merge(old,ADAPTER)
        rel='.cursor/rules/bilingual-ui.mdc';p=safe_path(rel)
        header='---\ndescription: Mandatory bilingual component-based UI contract\nalwaysApply: true\n---\n\n'
        old=p.read_text(encoding='utf-8') if p.exists() else header
        if p.exists() and BEGIN not in old:
            raise ValueError('Existing Cursor file is unmanaged: '+rel)
        if p.exists() and not old.startswith(header):
            raise ValueError('Cursor metadata was modified; merge manually: '+rel)
        writes[rel]=merge(old,ADAPTER)
        writes['.ai/ui-system/manifest.json']=json.dumps({'version':1,'files':{k:digest(v) for k,v in payload.items()}},ensure_ascii=False,indent=2)+'\n'
        changes=[]
        for rel,content in writes.items():
            p=safe_path(rel)
            if not p.exists() or p.read_text(encoding='utf-8')!=content:
                changes.append((p,content))
    except (OSError,ValueError,TypeError,UnicodeError) as exc:
        parser.exit(2,f'Installation preflight failed: {exc}\nNo files were written.\n')
    for p,content in changes:
        print(('PLAN ' if args.dry_run else 'WRITE ')+p.relative_to(root).as_posix())
        if args.dry_run: continue
        p.parent.mkdir(parents=True,exist_ok=True)
        mode=p.stat().st_mode & 0o777 if p.exists() else 0o644
        fd,tmp=tempfile.mkstemp(prefix='.ui-rules-',dir=p.parent)
        try:
            with os.fdopen(fd,'w',encoding='utf-8',newline='\n') as out: out.write(content)
            os.chmod(tmp,mode);os.replace(tmp,p)
        finally:
            if os.path.exists(tmp): os.unlink(tmp)
    print(f'{len(changes)} file(s) '+('planned.' if args.dry_run else 'updated.'))
    print('Next: read .ai/ui-system/USAGE_FA.md, integrate assets and configure guard source paths.')
'''

def payload(skill_dir):
    data={'.ai/ui-system/'+p.name:p.read_text(encoding='utf-8') for p in (skill_dir/'assets').iterdir() if p.is_file()}
    data['.ai/ui-system/POLICY.md']=(skill_dir/'references/POLICY.md').read_text()
    data['.ai/ui-system/implementation.md']=(skill_dir/'references/implementation.md').read_text()
    for folder,ref in [('ui-component-contract','components.md'),('ui-persian-english','bidi.md'),('ui-light-dark','themes.md')]:
        # Reconciled personal-skill folder names are opaque; resolve by frontmatter name.
        candidates=[p for p in skill_dir.parent.iterdir() if p.is_dir() and (p/'SKILL.md').is_file() and f'name: {folder}\n' in (p/'SKILL.md').read_text()]
        if len(candidates)!=1: raise ValueError('Could not resolve companion skill: '+folder)
        data['.ai/ui-system/'+ref]=(candidates[0]/'references'/ref).read_text()
    data['.ai/ui-system/USAGE_FA.md']='''# راهنمای قواعد رابط کاربری

این بسته، قواعد پروژه برای طراحی کامپوننتی فارسی و انگلیسی و دو تم مستقل است.
نصب قواعد، به‌تنهایی کد برنامه را تغییر نمی‌دهد. عامل توسعه باید POLICY.md را بخواند
و قرارداد را با ساختار فعلی برنامه ادغام کند.

## استفاده

1. فایل installer را خارج از پوشه‌های کد رابط نگه دارید.
2. پیش‌نمایش نصب: `python3 Bilingual_UI_Rules_Installer.py --project /path/to/project --dry-run`
3. نصب: همان دستور بدون `--dry-run`.
   در ویندوز می‌توانید از `py` به جای `python3` و مسیر داخل کوتیشن استفاده کنید.
4. در ابزار انتخابی، بررسی کنید قواعد پروژه فعال و بارگذاری شده‌اند.
5. از عامل بخواهید POLICY.md را اعمال کند، کامپوننت‌ها را بازاستفاده کند، CSS و
   bootstrap را مطابق معماری و CSP ادغام کند و ماتریس چهارحالته را بررسی کند.
6. فایل‌های واقعی و دارای مجوز ایران‌یکان را در مسیر فونت پروژه قرار دهید؛ فایل
   فونت در این بسته نیست. مسیرهای CSS نمونه‌اند و باید با فایل‌های واقعی منطبق شوند.
7. مسیرهای include و token_files در guard.json را برای پروژه تنظیم کنید.
   سپس `python3 .ai/ui-system/check_ui.py --root .` را اجرا کنید.
8. برای الزام در ادغام کد، این بررسی و تست‌های مرورگر را به CI اضافه کنید و
   در تنظیمات مخزن، آن‌ها را required کنید. نصب‌کننده این تنظیمات را تغییر نمی‌دهد.

## فایل‌ها و پشتیبانی

| ابزار | فایل قواعد |
| --- | --- |
| Codex و ابزارهای سازگار | AGENTS.md |
| Claude Code | CLAUDE.md |
| Gemini CLI | GEMINI.md |
| Cursor | .cursor/rules/bilingual-ui.mdc با alwaysApply |
| GitHub Copilot | .github/copilot-instructions.md |
| سایر ابزارها | ارائه مستقیم .ai/ui-system/POLICY.md |

این قواعد در سطح پروژه درخواست الزام می‌کنند؛ هیچ فایلی تمام مدل‌ها و سرویس‌های
هوش مصنوعی را مستقل از تنظیمات و سلسله‌مراتب دستورات آن‌ها مجبور نمی‌کند.
قواعد موجود با بلوک مدیریت‌شده حفظ می‌شوند. نصب مجدد تکراری نیست. فایل‌های سیاست
که دستی تغییر کرده‌اند، برای جلوگیری از از دست رفتن تغییرات خودکار بازنویسی نمی‌شوند.
قبل از نصب، دستورهای متعارض یا قواعد نزدیک‌تر به فایل‌های هدف را بررسی و اصلاح کنید.

## معیار پذیرش

متن‌های چندخطی فارسی و انگلیسی با کلاس مشترک ui-prose جاستیفای می‌شوند؛ خط آخر
هم‌جهت زبان است. عنوان، دکمه، برچسب، جدول و کد تراز مناسب خود را حفظ می‌کنند.

فارسی روشن، فارسی تاریک، انگلیسی روشن، انگلیسی تاریک؛ جهت سند و پنجره‌ها، فونت
واقعی، حالت‌های تعامل، خطا/بارگذاری/خالی، کنتراست، صفحه‌کلید، موبایل و بزرگ‌نمایی.
بررسی خودکار متنی محدود است و صحت کامل ظاهری یا دسترس‌پذیری را تأیید نمی‌کند.
اگر مسیر کدی پیدا نشود، اسکن خطا می‌دهد و به‌عنوان قبولی گزارش نمی‌شود.
'''
    return data

def standalone(skill_dir):
    body='#!/usr/bin/env python3\n# Portable project UI rules installer. Python 3.9+; no dependencies.\n'
    body+='import argparse, hashlib, json, os, tempfile\nfrom pathlib import Path\n'
    body+=f'ADAPTER={ADAPTER!r}\nBEGIN={BEGIN!r}\nEND={END!r}\n'
    body+=f'PAYLOAD=json.loads({json.dumps(payload(skill_dir),ensure_ascii=False)!r})\n'
    return body+ENGINE+"\nif __name__ == '__main__':\n    install(PAYLOAD)\n"

# Bind engine without running an install on import.
exec(ENGINE)
