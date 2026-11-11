# TERMINAL OS × AI COMMAND CENTER — design system

## Concept

This is an engineered identity, not a collection of logos. A series of five coherent terminal/HUD panels tells a story: **identity → capability → architecture → evidence → principle**.

The goal is *professional visual differentiation*, not to misrepresent the author's level. The descriptions are careful about ongoing projects and the learning stack.

### Motion principles

1. Motion conveys a system state: terminal cursor / pulsing signal.
2. Motion conveys data movement: animated dash offsets on service boundaries.
3. Motion conveys attention hierarchy: restrained lighting and orbit.
4. Motion is non-essential: the design remains legible with CSS animations disabled.
5. Avoid distracting stats/badges that do not communicate engineering value.

## Editing

The generator is in `scripts/generate_assets.py` and uses only Python stdlib. All colors, positions and copy are editable. Run `python3 scripts/generate_assets.py`, then validate using `python3 scripts/validate_profile.py`.

## Content boundaries

A beautifully designed GitHub README does not require senior status. The visual is deliberately sophisticated without claiming unverified production accomplishments or fake system metrics.

Skill entries include concepts and technologies being learned or practiced, not a statement of mastery.

## File inventory

- `assets/hero.svg`: boot console + AI orbit + identity
- `assets/skills-terminal.svg`: six-card terminal skills matrix
- `assets/systems-map.svg`: request-to-controlled-action flow
- `assets/projects-terminal.svg`: 4 terminal repository windows
- `assets/footer.svg`: closing terminal banner
- `README.md`: publishable GitHub profile Markdown
- `docs/index.html`: optional real, keyboard-driven terminal web app for GitHub Pages
- `preview/profile-preview.html`: optional full visual preview, not required by GitHub
- `scripts/generate_assets.py`: generator source for every animated SVG
- `scripts/validate_profile.py`: XML and reference validator
- `.github/workflows/profile-check.yml`: validation on change

- `backup-previous-version/`: copy of the files you originally supplied, for easy comparison or rollback.
