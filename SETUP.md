# Install your profile

1. Create a public GitHub repository named `vigoroth`, owned by `vigoroth`. If it already exists, use it.
2. Extract this ZIP on your computer.
3. Upload `README.md` and the complete `assets` folder to the repository root. In GitHub, use **Add file → Upload files**, then drag in both items. Keep the `assets` folder structure intact.
4. Commit the changes and open https://github.com/vigoroth.
5. Use **Customize your pins** on your profile to feature Argus, Support Ticket Triage, AI Data Analysis Agent, CT Image Segmentation and Basketball Tracking.

The root should contain `README.md` alongside `assets/header.gif`, `assets/header-static.png`, `assets/stack.svg` and four project-card SVGs.

## Motion and appearance

The header loops every seven seconds. It combines an emerald Matrix-style character rain with a typing effect for Data Scientist. Your name stays visible throughout. The static version shows the full role.

The README uses a GIF for broad image compatibility. A `<picture>` source requests the static PNG for viewers who prefer reduced motion, where that preference is honored by the renderer. The banner and cards use charcoal (#111111) and emerald (#34D399), taken from the portfolio source. They carry their own dark background and remain readable in either GitHub theme.

All visual assets are included. There are no external widget servers, API keys, tracking counters or scheduled workflows. Motion does not require JavaScript. The GIF, PNG and SVG files should be committed as files, not pasted into README text.

## Customize

- Edit the prose and project links in `README.md` directly.
- The `generate_assets.py` source is included if you want to change the design. It requires Python 3.10+ and Pillow (`python -m pip install Pillow`). Run it in any directory; assets are written alongside that script.
- For a static header, replace the whole `<picture>...</picture>` block with `![Nick Kantiotis — Data Scientist](./assets/header-static.png)`.
- Portfolio, LinkedIn and thesis links come from your portfolio repository. Its configured homepage is included; the live deployment could not be loaded during preparation, so confirm that destination before publishing. LinkedIn and thesis links were read from the Hero component. No CV download is linked because the filename in that source is dated 2025.
- This is a prepared profile package. It has not been published to your GitHub account.

## Portfolio design reference

The source files in https://github.com/vigoroth/my-portfolio provided the charcoal background, emerald accent, typing treatment, Matrix animation, professional introduction, and public links. The live deployment could not be loaded during this update; the design is based on the repository source.

- `src/components/Hero.js`: #111111, #34D399, typing animation, LinkedIn and thesis links.
- `src/components/MatrixEffect.js`: emerald character rain.
- `src/components/About.js`: Statistics & Insurance Science and Computer Science background.
- Configured repository homepage: https://my-portfolio-umber-eight-91.vercel.app

## Design inspiration

Inspired by the banner, concise introduction, skills and featured-project structure in Braydon Coyer's article, with original visual assets and copy adapted for Nick:
https://www.braydoncoyer.dev/blog/creating-a-killer-github-profile-readme-part-1

GitHub image and picture-element documentation:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
