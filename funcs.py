import calc

def target_and_distance(time, d_str):
    d_str = "half"
    time = calc.Time(1, 45 , 0)
    print(f"Distance: {d_str}")
    print("Target Time:", time)
    tpk = calc.time_per_k(time, calc.distances[d_str])
    print(f"Time per k: {tpk}")
    time = calc.from_secs(tpk.to_secs() * calc.distances[d_str])
    print("Actual Time:", time)


def pace_and_distance(time, d_str):
    time = calc.Time(0, 4 , 59)
    d_str = "full"
    print(f"Distance: {d_str}")
    print(f"Time per k: {time}")
    time = calc.from_secs(time.to_secs() * calc.distances[d_str])
    print("Time:", time)