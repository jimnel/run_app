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

- `calc.py` is the core. It holds the distance table (`distances`, in km) and the `Time` class, with helpers to convert to and from seconds. `Time.from_str` parses space-separated `"H M S"` input; trailing parts are optional, so `"1 30"` means 1h 30m. It validates with `assert`. `time_per_k(time, dist)` returns pace as a `Time`.
- `funcs.py` holds the user-facing operations, which print their results rather than returning them. `target_and_distance(time_str, d_str)` takes the **raw time string** and parses it itself. `pace_and_distance` is a work in progress: it currently ignores its arguments and uses hard-coded values.
- `run.py` collects the input and calls into `funcs`.
- `notebook.ipynb` is a scratchpad for trying out parsing logic. It is not imported anywhere.

All distances are in kilometres, and all time arithmetic goes through total seconds (`to_secs` / `from_secs`).
