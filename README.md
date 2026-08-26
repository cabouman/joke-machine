# The Joke Machine

A web page that shows a grid of topics. Click a topic and it tells a joke
about it. Click again for a different one.

Live: https://cabouman.github.io/joke-machine/

Built for ECE 60141 / ECE 63700 Lab 1.

## How it works

The jokes live in `jokes.json`. A Python script reads that file and writes
the page:

    python3 build_site.py

That writes `docs/index.html`, which is what GitHub Pages serves. To add a
joke, edit `jokes.json`, run the script, and push.

## Files

- `jokes.json` — the topics and the jokes
- `build_site.py` — reads the JSON, writes the page
- `docs/index.html` — the generated page
- `thingy-prompt.md` — the lab write-up
