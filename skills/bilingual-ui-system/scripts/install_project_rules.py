#!/usr/bin/env python3
from pathlib import Path
from project_rules import install, payload
if __name__ == '__main__':
    install(payload(Path(__file__).resolve().parents[1]))
