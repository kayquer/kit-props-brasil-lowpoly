# CLAUDE.md

Kit of light low poly Brazilian props (CC0), one Blender Python script per model. Blender 4.5 LTS: "C:/Program Files/Blender Foundation/Blender 4.5/blender.exe".

## Commands

- `blender -b --factory-startup --python src/<cat>/<id>.py` — one model → `models/<cat>/<id>.glb` (prints `MODELO {tris, kb}`)
- `blender -b --factory-startup --python src/gerar_todos.py [-- cat ...]` — regenerate + rewrite `models/catalogo.json`
- `blender -b --factory-startup --python src/vitrine.py -- tudo|<cat> [--cada]` — `previews/<cat>.jpg` (+ `previews/<cat>/<id>.jpg`); `-- todos` → `previews/todos.jpg`, renamed to `previews/capa.jpg`
- `py -3 tools/atualizar_readme.py` — rebuild the catalog in `README.md` (English, primary), `README.pt-BR.md` and `llms.txt` (between `<!-- catalogo:... -->`) from `catalogo.json`; every new model needs its English name in `tools/nomes_en.json` (the script fails otherwise)
- After adding/changing models: gerar_todos → vitrine → atualizar_readme, then commit.

## Conventions

- Categories: natureza, fauna, rua, rural, rio, tecnologia, poluicao (≤ 150 tris each, no bevel/chanfro) and detalhados, arvores (≤ 1,500 tris). Every file ≤ 150 KB.
- Author with the front toward Blender -Y (+X side also visible); `lib.exportar` rotates 180°, so the glTF front is -Z. Only `lib.PALETA` colors, flat.
- Toy scale for a 2 × 2-unit lot (hydrant ≈ 0.3 tall). Land props on z = 0; water props on the surface (z = 0, slightly sunk). `rio/trapiche` juts 1.4 forward (-Y) from its base; `poluicao/manilha_esgoto` and `poluicao/cano_pvc` pour forward; `poluicao/barranco_erodido`, `rio/covo` and `rio/pescaria` face the water with their front.
- Props must stay small and simple: never look like a building (that is what the Low Poly City Kit is for).
- Docstrings in pt-BR (the first sentence becomes the README description); no text/letters/real brands/logos; no gore; nothing third-party.
- `src/lib.py` came from ../kit-cidade-lowpoly (own copy, extra colors at the end of PALETA). Never touch or push the Guardião da Água repo from kit work.

## Gotchas

- A `.glb` re-imported into Blender comes back rotated 180°.
- Never run `gerar_todos.py` in parallel (one shared `catalogo.json`).
- Previews are JPEG. To view a render, convert with `ffmpeg -vf scale=1280:-1 -q:v 8` (the RTK hook blocks large images).
- Create scripts with Write, not a bash heredoc (an apostrophe breaks it).
- Triangle costs (lib): box 12; cylinder of n sides 4n−4; cone 2n−2; icosphere sub=1 20; ring (anel) 8n.
