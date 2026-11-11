# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A small Python 3 running-pace calculator: given a race distance and a target time, it computes the required pace per kilometre. There are no dependencies beyond the standard library, and no build, lint, or test setup.

## Running

The project is managed with uv (`pyproject.toml`, Python >= 3.13):

```
uv run run.py
```

`run.py` is an interactive CLI. It prompts for a distance key (`5k`, `10k`, `half`, `full`) and then a time.

## Architecture

The source code lives in the `src` package, which `run.py` imports from (`from src.funcs import ...`). Inside `src`, modules use relative imports (`from . import calc`).

- `src/calc.py` is the core. It has two time classes, and both roll excess seconds and minutes over into the next unit when constructed:
  - `RaceTime(hours, mins, secs)` is a total race time. `RaceTime.from_str` parses space-separated `"H M S"` input; trailing parts are optional, so `"1 30"` means 1h 30m and `"50"` means 50 hours.
  - `TimePerKm(mins, secs)` is a pace. Its `from_str` takes exactly `"M S"`.
  - `time_per_k(race_time, dist)` returns a `TimePerKm`.
  - Input is validated with `assert`.
- `src/funcs.py` holds the distance table (`distances`, keyed by `5k`/`10k`/`half`/`full`) and the calculations. `target_and_distance(time_str, d_str)` takes the **raw time string**, parses it itself, and returns `(TimePerKm pace, RaceTime actual_time)` without printing anything. The pace is rounded down to whole seconds on purpose, so the actual time is always at or under the target; keep that guarantee if you change the maths. `pace_and_distance` is a work in progress: it currently ignores its arguments and uses a hard-coded 4m 59s pace over the full marathon.
- `run.py` collects the input, calls into `funcs`, and does all the printing.

All distances are in kilometres, and all time arithmetic goes through total seconds (`to_secs` / `from_secs`).
