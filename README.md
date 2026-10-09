# Nordic Research Software Engineering Conference 2027

Website for the conference at the Delta Centre in Tartu, Estonia, on **15–16 June 2027**.

Public address: [nordic-rse.org/nrse2027](https://nordic-rse.org/nrse2027/).

The site uses [Zola](https://www.getzola.org/) and is adapted from the [Academic Workshop](https://github.com/aterenin/academic-workshop) theme. It is a static site with no application server or database.

## Preview and build

Use Zola **0.21.0**, matching the deployment workflow:

```sh
zola serve --interface 127.0.0.1 --port 8877
```

Open [127.0.0.1:8877](http://127.0.0.1:8877/). Stop the preview with Ctrl+C.

On Linux x86_64, the helper can download and verify the pinned Zola binary in the ignored `.tools/` directory:

```sh
./preview.sh
```

Set `NRSE_PREVIEW_PORT` to use a different port. The helper writes preview output under `.preview/`, separately from production builds.

Build the production site with:

```sh
zola build
```

If using the helper's binary, run `.tools/zola build` instead. Output goes to the ignored `public/` directory. Building locally does not deploy the site.

## Edit the site

| File | Purpose |
| --- | --- |
| [content/_index.md](content/_index.md) | Homepage copy, title, organizer details, local contact, and sponsor entries |
| [templates/index.html](templates/index.html) | Navigation, hero, organizer banner, sponsor section, and footer |
| [sass/main.scss](sass/main.scss) | Colours, typography, and responsive layout |
| [config.toml](config.toml) | Public URL and site metadata |
| [static/nrse2027.ics](static/nrse2027.ics) | All-day calendar entry for 15–16 June 2027 |
| [static/social-card.png](static/social-card.png) | Sharing image |
| [scripts/create-social-card.py](scripts/create-social-card.py) | Sharing-image source; requires Pillow when regenerating |

Update the homepage's `contact_name` and `contact_email` fields to change the footer contact. Sponsor entries use `name`, `logo` (relative to `static/`), and an optional `url`. Organizer recognition and sponsor recognition are separate sections.

If `sponsor_logos` is empty, production builds omit the sponsor section; `zola serve` displays clearly labelled layout placeholders. Add only agreed sponsor names and assets.

Keep the page title, calendar, site metadata, and sharing image consistent when changing the event name, dates, venue, or organizer attribution. Regenerate the sharing image from the repository root with `python3 scripts/create-social-card.py`. Normal builds use the existing image and do not require Python or Pillow.

## Deployment

[The GitHub Actions workflow](.github/workflows/deploy.yml) builds with Zola 0.21.0 and deploys `public/` to GitHub Pages after a push to `main`, or a manual workflow run. GitHub Pages must be configured to use GitHub Actions and deployment must be enabled.

Before merging a website update, build it and check the affected layout, local links, calendar download, and mobile view. After deployment, check the public URL, including assets served under `/nrse2027/`.

## Assets and acknowledgements

- University of Tartu colours and typography follow the [UT stylebook](https://stiiliraamat.ut.ee/).
- The English ICS logo is from the [official UT materials library](https://stiiliraamat.ut.ee/materjalide-allalaadimine/).
- The ELIXIR Estonia logo is from [ELIXIR TeSS's official assets](https://github.com/ElixirTeSS/TeSS/blob/master/app/assets/images/nodes/logos_svg/EE.svg).
- The Nordic-RSE logo is retained from the conference scaffold. Original logo colours and proportions are preserved.
- [Rubik](https://github.com/google/fonts/tree/main/ofl/rubik) is bundled locally under the [SIL Open Font License](static/fonts/OFL.txt).
- Thanks to Jørn Dietze, Sebastian Tendstrand Iversen, and Gregor Dechristoforo for the Nordic-RSE conference 2026 page outline, and to [Academic Workshop](https://github.com/aterenin/academic-workshop) for the original theme.

The original [MIT licence](license.md) is retained.
