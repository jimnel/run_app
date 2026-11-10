# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A small Python 3 running-pace calculator: given a race distance and a target time, it computes the required pace per kilometre. There are no dependencies beyond the standard library, and no build, lint, or test setup.

## Running

```
python3 run.py
```

`run.py` is an interactive CLI. It prompts for a distance key (`5k`, `10k`, `half`, `full`) and then a time.

## Architecture

- `calc.py` is the core. It has two time classes, and both roll excess seconds and minutes over into the next unit when constructed:
  - `RaceTime(hours, mins, secs)` is a total race time. `RaceTime.from_str` parses space-separated `"H M S"` input; trailing parts are optional, so `"1 30"` means 1h 30m and `"50"` means 50 hours.
  - `TimePerKm(mins, secs)` is a pace. Its `from_str` takes exactly `"M S"`.
  - `time_per_k(race_time, dist)` returns a `TimePerKm`.
  - Input is validated with `assert`.
- `funcs.py` holds the distance table (`distances`, keyed by `5k`/`10k`/`half`/`full`) and the user-facing operations, which print their results rather than returning them. `target_and_distance(time_str, d_str)` takes the **raw time string** and parses it itself. `pace_and_distance` is a work in progress: it currently ignores its arguments and uses a hard-coded 4m 59s pace over the full marathon.
- `run.py` collects the input and calls into `funcs`.
- `notebook.ipynb` is a scratchpad for trying out parsing logic. It is not imported anywhere.

All distances are in kilometres, and all time arithmetic goes through total seconds (`to_secs` / `from_secs`).
