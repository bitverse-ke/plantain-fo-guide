#!/usr/bin/env python3
"""Render the 1-page poster HTML to PDF using WeasyPrint."""
import sys
from pathlib import Path
from weasyprint import HTML

GUIDE_DIR = Path("/home/hermes/plantain-fo-guide")
HTML_FILE = GUIDE_DIR / "onepager.html"
PDF_FILE = GUIDE_DIR / "plantain-fo-onepager.pdf"

if not HTML_FILE.exists():
    print(f"ERROR: {HTML_FILE} not found", file=sys.stderr)
    sys.exit(1)

print(f"Rendering {HTML_FILE} -> {PDF_FILE} ...")
HTML(filename=str(HTML_FILE), base_url=str(GUIDE_DIR)).write_pdf(str(PDF_FILE))
size = PDF_FILE.stat().st_size
print(f"OK. {PDF_FILE} ({size:,} bytes, {size/1024:.1f} KB)")
