# Publish to GitHub

The GitHub connector returned HTTP 403 when attempting to write to your profile repository. Nothing was published automatically.

## Option A — Git command line

```bash
git clone https://github.com/oussamamahidev/oussamamahidev.git
cd oussamamahidev
# Copy README.md and the entire assets/ folder from this downloaded package into this directory
git add README.md assets/hero.svg assets/systems.svg
git commit -m "Redesign profile with custom animated portfolio visuals"
git push origin main
```

## Option B — GitHub web UI

1. Open https://github.com/oussamamahidev/oussamamahidev
2. Replace README.md with the provided README.md.
3. Use Add file -> Upload files to upload assets/hero.svg and assets/systems.svg under the assets directory (or use Git commands for preserving paths).
4. Commit to main.

GitHub SVG animation support can vary with browser, host sanitizer, and reduced motion settings. These SVGs have static fallback graphics and do not execute JavaScript.
