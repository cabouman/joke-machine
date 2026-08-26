# The Joke Machine

A web page that shows a grid of topics. Click a topic and it tells a joke
about it. Click again for a different one. Jokes are read out loud using the
browser's built-in speech synthesis; a button turns the sound off.

Live: https://cabouman.github.io/joke-machine/

Built for ECE 60141 / ECE 63700 Lab 1.

## How it works

The jokes live in `jokes.json`. A Python script reads that file and writes
the page:

    python3 build_site.py

That writes `docs/index.html`, which is what GitHub Pages serves. To add a
joke, edit `jokes.json`, run the script, and push.

The logo and the link-preview card are drawn by a second script:

    python3 make_preview.py

Run that first if you change the look, then run `build_site.py`.

## Files

- `jokes.json` — the topics, the jokes, and the site title and address
- `build_site.py` — reads the JSON, writes the page
- `make_preview.py` — draws the logo and the link-preview card
- `docs/index.html` — the generated page
- `docs/preview.png` — the picture messaging apps show for the link
- `docs/favicon.png` — the tab and home-screen icon
- `thingy-prompt.md` — the lab write-up
