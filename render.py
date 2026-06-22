#!/usr/bin/env python3
"""Render the plantain FO guide HTML to PDF using WeasyPrint."""
import sys
from pathlib import Path
from weasyprint import HTML, CSS

GUIDE_DIR = Path("/home/hermes/plantain-fo-guide")
HTML_FILE = GUIDE_DIR / "guide.html"
PDF_FILE = GUIDE_DIR / "plantain-fo-guide.pdf"

if not HTML_FILE.exists():
    print(f"ERROR: {HTML_FILE} not found", file=sys.stderr)
    sys.exit(1)

print(f"Rendering {HTML_FILE} → {PDF_FILE} ...")
HTML(filename=str(HTML_FILE), base_url=str(GUIDE_DIR)).write_pdf(str(PDF_FILE))
size = PDF_FILE.stat().st_size
print(f"✓ Done. {PDF_FILE} ({size:,} bytes, {size/1024:.1f} KB)")