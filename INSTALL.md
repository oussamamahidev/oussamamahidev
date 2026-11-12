# Publish your Terminal OS GitHub profile

## 1. previews the package

- Start by opening **`previews/profile-previews.html`** in your browser (or open `asset/hero.svg` directly).
- The profile itself is defined in `README.md`. The 5 SVG designs are in `asset/`.
- All source code for all 5 designs is in `scripts/generate_asset.py`.

## 2. Publish it to your GitHub profile

Your existing account, based on the supplied README: **`oussamamahidev`**.

The profile repository URL should be:

https://github.com/oussamamahidev/oussamamahidev

GitHub profile README requirements: the repository must be **public**, its name must match your username, and it must contain `README.md` in the root.

### Option A — Command line (recommended)

```bash
# If the special profile repository already exists:
git clone https://github.com/oussamamahidev/oussamamahidev.git
cd oussamamahidev

# Make a backup of the original README before copying these files.
# Copy README.md and asset/ from this ZIP folder to this cloned repo.

python3 scripts/validate_profile.py  # only after also copying the included scripts/ folder
git add README.md asset/ scripts/ INSTALL.md .github/
git commit -m "Build animated Terminal OS engineering profile"
git push origin main
```

If your branch is named something other than `main`, push to that branch. If the profile repo does not exist, create a **public** repository named `oussamamahidev` first.

### Option B — GitHub website

1. Open the profile repository.
2. Edit and replace the root `README.md` with the new one.
3. Upload the **full `asset/` directory**, preserving each path (`asset/hero.svg`, `asset/skills-terminal.svg`, `asset/systems-map.svg`, `asset/projects-terminal.svg`, `asset/footer.svg`).
4. Commit changes and visit your GitHub profile page.

**Important:** Your account has not been changed by creating this ZIP. Uploading/pushing is a separate step.

## 3. Customize your skills and wording

Open `scripts/generate_asset.py` and edit the `cards` data inside `make_skills()`. Modify the hero in `make_hero()` and projects in `make_projects()`.

Then run:

```bash
python3 scripts/generate_asset.py
python3 scripts/validate_profile.py
```

Edit `README.md` to keep the searchable text version synchronized.

## 4. Layout, animation and accessibility notes

- All 5 asset are vector SVG: crisp at any resolution.
- Animations use SVG CSS keyframes: node pulses, dashed data flows, rotating orbits, terminal cursor, cards and subtle motion.
- No JavaScript, no `<foreignObject>`, no remote fonts, no external image hosts or API tokens.
- A `prefers-reduced-motion` media query disables animations for visitors who request reduced motion.
- Animated SVG rendering is browser-dependent. If motion is unavailable, the underlying content remains visible.
- This is **GitHub README animation**, not a functioning shell or a clickable custom app. Links are normal README links below the visuals.

## 5. Run the included checks

```bash
python3 scripts/validate_profile.py
```

All images must be listed in README and readable as XML.

## 6. Theme colors

| Token | Hex |
|---|---|
| Background | `#070d1c` |
| Text | `#f3f9ff` |
| Teal | `#55ffe1` |
| Electric blue | `#76b8ff` |
| Soft violet | `#b391ff` |

## Sources and design rationale

The GitHub docs explain the special profile-repo name and relative asset paths:
- https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes

Every visual was generated specifically for this profile, using code supplied in this package. No third-party animated badge generator is required.

## 7. Optional: launch a real interactive terminal website (extra)

The ZIP also contains `docs/index.html`: a separate **working, keyboard-driven terminal** with `help`, `whoami`, `skills`, `projects`, `architecture`, `focus`, `contact`, `open 1`, `open 2`, etc.

To try it locally, open `docs/index.html` in a browser. It runs client-side without dependencies. It is **not** the README itself.

To publish via GitHub Pages after uploading the whole package:

1. Open your profile repository **Settings → Pages**.
2. Under Build and deployment, select **Deploy from a branch**.
3. Select your default branch (often `main`) and the folder **`/docs`**.
4. Save, and visit your Pages URL once GitHub reports that it is deployed.
5. Optionally add the Pages URL to your profile README as a normal link labeled **Open Interactive Terminal**.

Do **not** add a Pages URL until GitHub Pages has been enabled and the site exists.
