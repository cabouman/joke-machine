# Thingy Prompt: The Joke Machine

## What I Am Building

A public web page that shows a grid of topics. Click a topic and the page
tells a joke about it. Click again and it tells a different one. I wanted
something my family could open on a phone without installing anything, and
I wanted the topics to be things I actually care about rather than a generic
joke list.

## Guidelines

These are standing rules for this project. They apply to everything
you produce.

### Writing style

Write all text meant for humans — explanations, messages to me,
comments, documentation — in plain English:

- Use plain words and short sentences.
- Write complete sentences with subjects and verbs. One idea per
sentence.
- Lead with the conclusion. When reporting a problem, first say what
to do about it in one sentence; explain afterward.
- Do not use metaphors or idioms in technical statements. State the
literal fact.
- Do not use invented or undefined jargon. Standard technical terms
are fine; define any project-specific term where it first appears.
- Keep code comments short and to the point.

### Working style

- Build the simplest version that works first. Add features only
after I have seen the simple version run.
- Before making a major design decision, tell me the options and let
me choose.
- Report results plainly. If something fails, show me the actual
error message; do not guess that it worked.

## Features

Must have:

- A grid of topic buttons on a single page.
- Clicking a topic shows one joke about that topic.
- An "Another one" button that shows a different joke in the same topic.
- Every joke in a topic appears once before any of them repeats.
- The jokes live in a separate data file, not inside the HTML, so I can add
  or change jokes without touching the page code.
- A Python script rebuilds the page from that data file.
- The page is one self-contained HTML file, so it can be hosted for free
  as a static site.

Nice to have:

- The page follows the reader's light or dark setting.
- The selected topic stays visibly highlighted.
- It works on a phone screen.

## Look and Feel

Clean and quiet. A title, one line of explanation, then the topic grid.
The joke appears in a card below the grid, in larger type than the rest of
the page, so it is the thing your eye lands on. Each topic button carries a
small picture so the grid is scannable rather than a wall of words. Purdue
gold as the single accent color. No animation, no sound, no clutter.

## Platform

A web page, hosted publicly on GitHub Pages so anyone can open the link.
The page itself is HTML, CSS, and a small amount of JavaScript. The jokes
are stored in `jokes.json`, and a Python script, `build_site.py`, reads that
file and writes `docs/index.html`. I work on a Mac.

Files:

- `jokes.json` — the topics and the jokes
- `build_site.py` — reads the JSON, writes the page
- `docs/index.html` — the generated page, which is what GitHub Pages serves

## What Done Looks Like

I can send someone a link, they open it on their phone, tap "Bicycles," and
laugh or at least exhale through their nose. I can add a new joke by editing
one line of `jokes.json`, running `python3 build_site.py`, and pushing.

## Reflection

### A) Was this fun? Why or why not?

TODO — fill in after the demo.

### B) What did I learn?

TODO — fill in after the demo.

### C) What would I do differently?

TODO — fill in after the demo.
