#!/usr/bin/env python3
"""Generate cv_master_en.md from the English LaTeX CV using Pandoc."""

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parent
source = subprocess.run(
    ["pandoc", "cv_master_en.tex", "--from=latex", "--to=gfm", "--wrap=none"],
    cwd=ROOT,
    check=True,
    capture_output=True,
    text=True,
).stdout

source = source.replace('<div class="samepage">\n\n', "").replace("\n</div>", "")
source = source.replace("**John Marlon Pérez Niebla**", "# John Marlon Pérez Niebla", 1)
source = source.replace("\n# ", "\n## ").replace("\\|", "|")
source = source.replace(
    "Matanzas, Cuba | <johnmarlonperez@icloud.com>",
    "Matanzas, Cuba | [johnmarlonperez@icloud.com](mailto:johnmarlonperez@icloud.com)",
)

replacements = {
    "**Desoft, Matanzas DivisionMatanzas, Cuba**": "**Desoft, Matanzas Division** | Matanzas, Cuba",
    "**Software Developer***Jan 2026 – Present · Hybrid*": "**Software Developer**  \n*Jan 2026 – Present · Hybrid*",
    "**Independent Freelance WorkRemote**": "**Independent Freelance Work** | Remote",
    "**Automation and Bot Developer***Feb 2022 – Present*": "**Automation and Bot Developer**  \n*Feb 2022 – Present*",
    "**After-Sales Support Management System (SOPOS)***Computer Engineering Thesis*": "**After-Sales Support Management System (SOPOS)**  \n*Computer Engineering Thesis*",
    "**PROVEA — Business Entities and B2B Opportunities Platform***Oct 2026 – Present*": "**PROVEA — Business Entities and B2B Opportunities Platform**  \n*Oct 2026 – Present*",
    "**University of MatanzasMatanzas, Cuba**": "**University of Matanzas** | Matanzas, Cuba",
    "**Computer Engineering***Feb 2022 – Jul 2026*": "**Computer Engineering**  \n*Feb 2022 – Jul 2026*",
}
for old, new in replacements.items():
    source = source.replace(old, new)

source = source.replace("**Languages and APIs:**", "- **Languages and APIs:**")
source = source.replace("; **", "\n- **")
(ROOT / "CV_EN.md").write_text(source.strip() + "\n", encoding="utf-8")
