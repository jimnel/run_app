# Race Pace Calculator

Work out the pace per kilometre you need to hit a target race time.

**Try it:** https://jimnel.github.io/run_app/

Pick a distance (5k, 10k, half marathon or marathon) and a target time, and the calculator gives you the pace per km. The pace is rounded down to whole seconds, so holding it gets you in at or under your target.

## Run it locally

### Command line

Requires [uv](https://docs.astral.sh/uv/) and Python 3.13+.

```
uv run run.py
```

Enter a distance (`5k`, `10k`, `half`, `full`), then a time as space-separated hours, minutes and seconds, for example `1 30` for 1h 30m.

### Web page

The web page runs the same Python in your browser using [PyScript](https://pyscript.net/). Serve the repo root with any static server and open it:

```
python3 -m http.server
```

Then go to http://localhost:8000.

## Project layout

- `src/calc.py`: the time classes (`RaceTime`, `TimePerKm`) and pace maths
- `src/funcs.py`: the distance table and the calculations
- `run.py`: the command-line interface
- `index.html`: the web page

## Deployment

Every push to `main` deploys the site to GitHub Pages through `.github/workflows/pages.yml`. Only `index.html` and the `src` modules are published.
