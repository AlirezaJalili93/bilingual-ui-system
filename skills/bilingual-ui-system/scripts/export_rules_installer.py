#!/usr/bin/env python3
import argparse
from pathlib import Path
from project_rules import standalone
if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='Export a portable UI project rules installer (no skill directories).')
    parser.add_argument('--output',required=True,type=Path)
    args=parser.parse_args()
    if args.output.exists(): parser.error('Output already exists; choose a new path')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(standalone(Path(__file__).resolve().parents[1]),encoding='utf-8')
    print(args.output)
