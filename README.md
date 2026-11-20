# Curriculum Vitae — John Marlon Pérez Niebla

**Software Engineer · Backend, ERP & Automation**

Public versions of my CV, written in LaTeX and published as PDF and Markdown.

| Language | PDF | Markdown |
| --- | --- | --- |
| English | [John_Marlon_Perez_Niebla_CV.pdf](John_Marlon_Perez_Niebla_CV.pdf) | [CV_EN.md](CV_EN.md) |
| Español | [John_Marlon_Perez_Niebla_CV_ES.pdf](John_Marlon_Perez_Niebla_CV_ES.pdf) | [CV_ES.md](CV_ES.md) |

Contact: [johnmarlonperez@icloud.com](mailto:johnmarlonperez@icloud.com) · [LinkedIn](https://www.linkedin.com/in/john-marlon-perez) · [GitHub](https://github.com/john-marlon)

---

## About these files

- One-column A4 layout, selectable text, designed to stay readable for both people and ATS parsers.
- No photo, tables, side columns or skill bars.
- Visible link text instead of bare URLs.
- The public versions omit the phone number; it is available on request.
- Work at Desoft is described in general technical terms. No client data, internal identifiers or proprietary code are included.

## Repository layout

```
.
├── cv_master_en.tex          # English CV entry point
├── cv_maestro.tex            # Spanish CV entry point
├── secciones_en/             # English sections
├── secciones/                # Spanish sections
├── compilar_markdown_en.py   # Generates CV_EN.md with Pandoc
├── compilar_markdown.py      # Generates CV_ES.md with Pandoc
├── John_Marlon_Perez_Niebla_CV.pdf
├── John_Marlon_Perez_Niebla_CV_ES.pdf
├── CV_EN.md
└── CV_ES.md
```

## Build

Requires XeLaTeX, Pandoc and the [Lato](https://fonts.google.com/specimen/Lato) font.

```bash
# PDFs
xelatex cv_master_en.tex
xelatex cv_maestro.tex

# Markdown versions
python3 compilar_markdown_en.py
python3 compilar_markdown.py
```

Both documents are two A4 pages. Sections can be toggled on or off in the preamble of each `.tex` file.

## Updating

Edit the relevant file in `secciones_en/` or `secciones/`, then rebuild the PDF and Markdown versions and commit both outputs together so the published files never drift from the sources.
