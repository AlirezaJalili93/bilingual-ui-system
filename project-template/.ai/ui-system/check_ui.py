#!/usr/bin/env python3
"""Limited lexical UI guard. Not an AST parser or runtime accessibility check."""
import argparse
import fnmatch
import json
import re
from pathlib import Path

SUFFIXES = {'.css', '.scss', '.sass', '.less', '.html', '.jsx', '.tsx', '.vue', '.svelte'}
RULES = {
    'literal-color': re.compile(r'(?<![\w-])#[0-9a-fA-F]{3,8}\b|\b(?:rgb|rgba|hsl|hsla|oklch|oklab|lab|lch|color)\s*\('),
    'literal-radius': re.compile(r'''(?:border-radius|border-(?:top|bottom)-(?:left|right)-radius|border-(?:start|end)-(?:start|end)-radius|borderRadius|border(?:Top|Bottom)(?:Left|Right)Radius)\s*:\s*["']?(?:\d|\.\d)''', re.I),
    'physical-css': re.compile(r'\b(?:margin|padding|border)-(?:left|right)(?:-\w+)?\s*:|\b(?:left|right)\s*:\s*[-\d]|\btext-align\s*:\s*(?:left|right)\b'),
    'raw-radius-utility': re.compile(r'(?<![\w-])rounded(?:-(?:none|sm|md|lg|xl|2xl|3xl|full|\[[^\]]+\]))?(?![\w-])'),
    'raw-color-utility': re.compile(r'(?<![\w-])(?:bg|text|border|ring|fill|stroke)-(?:white|black|(?:slate|gray|zinc|neutral|stone|red|orange|amber|yellow|lime|green|emerald|teal|cyan|sky|blue|indigo|violet|purple|fuchsia|pink|rose)-\d{2,3}|\[#[^\]]+\])(?![\w-])'),
    'named-css-color': re.compile(r'\b(?:color|background(?:-color)?|border-color|outline-color)\s*:\s*(?:white|black|red|blue|green|gray|grey|yellow|orange|purple)\b', re.I),
}

def matches(path, patterns):
    return any(fnmatch.fnmatchcase(path, p) or path == p or path.startswith(p.rstrip('/') + '/') for p in patterns)

def scan(root, config):
    findings=[]; scanned=0; seen=set()
    for entry in config['include']:
        base=root/entry
        if base.is_symlink():
            continue
        candidates=[base] if base.is_file() else sorted(base.rglob('*')) if base.is_dir() else []
        for path in candidates:
            if path.is_symlink() or not path.is_file() or path.suffix not in SUFFIXES:
                continue
            # Skip symlinked ancestors, including glob-discovered external files.
            if any(parent.is_symlink() for parent in path.parents if parent != root):
                continue
            rel=path.relative_to(root).as_posix()
            if rel in seen or matches(rel, config.get('exclude', [])) or any(part in config.get('exclude',[]) for part in path.relative_to(root).parts):
                continue
            seen.add(rel)
            if rel in config.get('token_files', []):
                continue
            scanned+=1
            source=path.read_text(encoding='utf-8')
            # Mask block/HTML comments while preserving newlines and offsets.
            def blank(m):
                return ''.join('\n' if c=='\n' else ' ' for c in m.group())
            source=re.sub(r'/\*[\s\S]*?\*/|<!--[\s\S]*?-->',blank,source)
            for rule,pattern in RULES.items():
                for hit in pattern.finditer(source):
                    if any(e['rule']==rule and fnmatch.fnmatchcase(rel,e['path']) for e in config.get('exceptions', [])):
                        continue
                    findings.append({'path':rel,'line':source.count('\n',0,hit.start())+1,'rule':rule,'match':hit.group()})
    return scanned,findings

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path('.'))
    parser.add_argument('--config',type=Path)
    args=parser.parse_args();root=args.root.resolve()
    config_path=args.config or root/'.ai/ui-system/guard.json'
    try:
        config=json.loads(config_path.read_text())
        if not isinstance(config.get('include'),list) or not config['include']:
            raise ValueError('include must be a non-empty array')
        for entry in config['include']:
            p=Path(entry)
            if p.is_absolute() or '..' in p.parts:
                raise ValueError('include paths must stay within the project')
        for exception in config.get('exceptions',[]):
            if not all(exception.get(k) for k in ('path','rule','reason')) or exception['rule'] not in RULES:
                raise ValueError('exceptions require path, known rule and reason')
        count,findings=scan(root,config)
    except (OSError,ValueError,TypeError,KeyError) as exc:
        parser.exit(2,f'Guard configuration/read error: {exc}\n')
    for item in findings:
        print(f"{item['path']}:{item['line']}: {item['rule']}: {item['match']}")
    print(f'Scanned {count} UI files; {len(findings)} findings. Runtime/visual checks remain required.')
    if count==0:
        parser.exit(2,'No UI files scanned. Configure include paths; this is not a passing check.\n')
    raise SystemExit(1 if findings else 0)
if __name__=='__main__':
    main()
