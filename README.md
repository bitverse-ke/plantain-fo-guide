# Plantain Procurement & Grading — Field Officer Guide

**Edition:** 1.0 · June 2026
**Audience:** Field Officers, Plantain Outgrowers Portal (POP)
**Scope:** True Horn + False Horn + Rhino Horn plantain (Musa AAB)

## Files in this directory

| File | Purpose |
|---|---|
| `plantain-fo-guide.pdf` | **Print-ready PDF** — give this to the FO |
| `guide.html` | Editable HTML source (print-CSS included) |
| `render.py` | Renders `guide.html` → PDF via WeasyPrint |
| `illustrations/` | 7 standalone SVG illustrations (swap for real photos) |

## Sections in the guide

1. Your role & the procurement mindset
2. Pre-visit preparation & the field toolkit
3. The visit — six steps from signal to transport
4. Varieties — false horn vs. true horn
5. Maturity — the single most important grade
6. Grading standard — A, B, C, Reject
7. Defect catalog — what disqualifies a bunch
8. Pricing & negotiation — the ±5% band
9. Weighing, shrinkage & records
10. Rejections, disputes & escalation
11. Quick-reference card (tear-off, last page)

## Grading thresholds (proposed)

| Grade | FH bunch wt | TH bunch wt | RH bunch wt | FH finger length | TH finger length | RH finger length |
|---|---|---|---|---|---|---|
| A | ≥ 20 kg | ≥ 12 kg | ≥ 25 kg | ≥ 20 cm | ≥ 25 cm | ≥ 30 cm |
| B | 12–20 kg | 8–12 kg | 15–25 kg | 15–20 cm | 20–25 cm | 25–30 cm |
| C | < 12 kg | < 8 kg | < 15 kg | < 15 cm | < 20 cm | < 25 cm |
| X | reject | reject | reject | — | — | — |

## How to edit and re-render

1. Open `guide.html` in any text editor.
2. Edit content (text, tables, callouts).
3. To replace illustrations with real photos: drop a photo into `illustrations/`, then update the `src` attribute in `guide.html` to the new filename.
4. Re-render:
   ```bash
   /home/hermes/.hermes/hermes-agent/venv/bin/python3 render.py
   ```

## How to print a fresh copy for an FO

The PDF is the print artifact. If you want to print from the HTML:
- Open `guide.html` in Chrome or Firefox
- File → Print → Save as PDF (or send to printer)
- The `@page` CSS in the source handles margins, page numbers, and headers

## Pricing & shrinkage defaults (locked from POP config)

- FO band: ±5% around daily reference price
- Volume bonus: ≥ 200 kg Grade A equivalent from one outgrower → +5%
- Shrinkage flag: > 5% net-weight shortfall at collection point → flag for review
- True Horn premium: +5–10% over FH reference (variety tier)
- Rhino Horn premium: +15–25% over FH reference (top-tier restaurant / export)
- Grade adjustment (within band, not stacked): B = ref −5%; C = ref −10 to −15%