# Bilingual UI System — complete pack

Pack version: **1.1.0**. Includes four skills, a standalone project rules installer,
reference output, design assets, Persian Markdown documentation, examples and templates.

## Quick start

```bash
python3 Bilingual_UI_Rules_Installer.py --project "/path/to/project" --dry-run
python3 Bilingual_UI_Rules_Installer.py --project "/path/to/project"
```

Use `py` on Windows if appropriate. Python 3.9+ is required; no extra Python packages
are required by the standalone installer or the static guard.

Read [the installation guide](docs/03_Installation_FA.md) and
[the complete Persian index](README.md). Integrate the CSS, real licensed IranYekan
fonts, locale metadata and theme bootstrap into the actual application afterward.

## Contract

Persian: IranYekan + RTL. English: system sans-serif + LTR. Justify multi-line prose
with last-line start alignment; retain logical alignment for controls and headings.
Reuse components and semantic tokens with central radius roles. Implement separate
light/dark semantic palettes and light/dark/system preference. Verify all four
locale/theme combinations, responsive states, keyboard behavior and contrast.

## Skill source

The `skills` directory contains portable copies. Use the selected host's supported
skill import mechanism. For hosts without native skill loading, install project
rules and explicitly provide `.ai/ui-system/POLICY.md` as context.
Do not copy the entire pack into a skill directory: user documentation belongs
outside the individual skills.

The installer does not integrate application code, configure CI branch protection,
or guarantee that every AI service will load instructions. Font binaries are not
included and no font license is granted. See [verification](VERIFICATION.md).
