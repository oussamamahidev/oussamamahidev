#!/usr/bin/env python3
"""Validate all local SVG images used by GitHub profile README; stdlib only."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

root=Path(__file__).resolve().parents[1]
readme=(root/'README.md').read_text(encoding='utf-8')
images=re.findall(r'src=["\'](\.\/asset\/[^"\']+\.svg)["\']',readme)
if not images:
    sys.exit('FAIL: README.md has no asset references')
errors=[]
for image in images:
    path=root/image
    if not path.is_file():
        errors.append(f'Missing image: {image}')
        continue
    data=path.read_text(encoding='utf-8')
    if '<script' in data.lower() or '<foreignObject' in data:
        errors.append(f'Potentially unsafe SVG content: {image}')
    try:
        svg=ET.fromstring(data)
        if not svg.tag.endswith('svg'):
            errors.append(f'Unexpected SVG root: {image}')
    except ET.ParseError as exc:
        errors.append(f'Invalid SVG XML in {image}: {exc}')
    if 'prefers-reduced-motion' not in data:
        errors.append(f'Missing reduced-motion support: {image}')
    if '@keyframes' not in data:
        errors.append(f'No animation found: {image}')
    print(f'{"OK" if not errors else "CHECK"} {image} ({len(data)} chars)')
if errors:
    sys.exit('FAIL:\n'+'\n'.join(errors))
print(f'SUCCESS: {len(images)} SVG images have valid XML, animation styles, and reduced-motion fallback.')
