#!/usr/bin/env python3
"""Wraps index.html (the claude.ai Artifact source) into a full standalone page at docs/index.html."""
import pathlib
root = pathlib.Path(__file__).parent
body = (root / 'index.html').read_text(encoding='utf-8')
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
        'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>\n')
out = root / 'docs' / 'index.html'
out.parent.mkdir(exist_ok=True)
out.write_text(head + body + '\n</body></html>\n', encoding='utf-8')
print('wrote', out)
