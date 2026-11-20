#!/usr/bin/env python3
"""Genera CV_ES.md desde el documento LaTeX y sus secciones con Pandoc."""

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parent
source = subprocess.run(
    ["pandoc", "cv_maestro.tex", "--from=latex", "--to=gfm", "--wrap=none"],
    cwd=ROOT,
    check=True,
    capture_output=True,
    text=True,
).stdout

# Pandoc representa el entorno LaTeX `samepage` como un div HTML; no aporta
# contenido al Markdown, así que se eliminan las etiquetas.
source = source.replace('<div class="samepage">\n\n', "").replace("\n</div>", "")
source = source.replace("**John Marlon Pérez Niebla**", "# John Marlon Pérez Niebla", 1)
source = source.replace("\n# ", "\n## ")
source = source.replace("\\|", "|")
source = source.replace(
    "Matanzas, Cuba | <johnmarlonperez@icloud.com>",
    "Matanzas, Cuba | [johnmarlonperez@icloud.com](mailto:johnmarlonperez@icloud.com)",
)

# Separar los campos que en LaTeX se alinean con `\\hfill`.
replacements = {
    "**Desoft, División MatanzasMatanzas, Cuba**": "**Desoft, División Matanzas** | Matanzas, Cuba",
    "**Desarrollador de Software***Enero de 2026 – Actualidad · Modalidad híbrida*": "**Desarrollador de Software**  \n*Enero de 2026 – Actualidad · Modalidad híbrida*",
    "**Trabajo freelance independienteRemoto**": "**Trabajo freelance independiente** | Remoto",
    "**Desarrollador de automatizaciones y bots***Febrero de 2022 – Actualidad*": "**Desarrollador de automatizaciones y bots**  \n*Febrero de 2022 – Actualidad*",
    "**Sistema de gestión del soporte post-venta (SOPOS)***Tesis de Ingeniería Informática*": "**Sistema de gestión del soporte post-venta (SOPOS)**  \n*Tesis de Ingeniería Informática*",
    "**PROVEA — Plataforma de actores económicos y oportunidades B2B***Octubre de 2026 – Actualidad*": "**PROVEA — Plataforma de actores económicos y oportunidades B2B**  \n*Octubre de 2026 – Actualidad*",
    "**Universidad de MatanzasMatanzas, Cuba**": "**Universidad de Matanzas** | Matanzas, Cuba",
    "**Ingeniería Informática***Febrero de 2022 – Julio de 2026*": "**Ingeniería Informática**  \n*Febrero de 2022 – Julio de 2026*",
}
for old, new in replacements.items():
    source = source.replace(old, new)

# Mostrar las competencias como categorías escaneables, no como un solo párrafo.
source = source.replace("**Lenguajes y APIs:**", "- **Lenguajes y APIs:**")
source = source.replace("; **", "\n- **")

(ROOT / "CV_ES.md").write_text(source.strip() + "\n", encoding="utf-8")
