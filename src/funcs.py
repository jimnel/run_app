from . import calc

HM_DIST = 21.0975
FM_DIST = 42.195

distances = {
    "5k": 5,
    "10k": 10,
    "half": HM_DIST,
    "full": FM_DIST,
}

def target_and_distance(time, d_str):
    """Work out the pace needed to finish a race within a target time.

    Args:
        time: Target time as a `calc.RaceTime`.
        d_str: Distance key from `distances` ("5k", "10k", "half", "full").

    Returns:
        A tuple (pace, actual_time): the pace per km as a `calc.TimePerKm`,
        and the finish time from holding that pace as a `calc.RaceTime`.
        The pace is rounded down to whole seconds on purpose, so actual_time
        is always at or under the target.
    """
    assert d_str in distances.keys()

    tpk = calc.time_per_k(time, distances[d_str])
    true_time = calc.RaceTime.from_secs(tpk.to_secs() * distances[d_str])
    return tpk, true_time


def pace_and_distance(time, d_str):
    time = calc.TimePerKm(4, 59)
    d_str = "full"
    print(f"Distance: {d_str}")
    print(f"Time per k: {time}")
    time = calc.RaceTime.from_secs(time.to_secs() * distances[d_str])
    print("Time:", time)