import calc

HM_DIST = 21.0975
FM_DIST = 42.195

distances = {
    "5k": 5,
    "10k": 10,
    "half": HM_DIST,
    "full": FM_DIST,
}

def target_and_distance(time_str, d_str):
    assert d_str in distances.keys()
    print(f"Distance: {d_str}")

    time = calc.Time.from_str(time_str)
    print("Target Time:", time)

    tpk = calc.time_per_k(time, calc.distances[d_str])
    print(f"Time per k: {tpk}")

    time = calc.Time.from_secs(tpk.to_secs() * calc.distances[d_str])
    print("Actual Time:", time)


def pace_and_distance(time, d_str):
    time = calc.Time(0, 4 , 59)
    d_str = "full"
    print(f"Distance: {d_str}")
    print(f"Time per k: {time}")
    time = calc.Time.from_secs(time.to_secs() * distances[d_str])
    print("Time:", time)