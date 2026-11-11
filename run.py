from src.funcs import target_and_distance

print("Enter a distance: 5k, 10k, half, full")
dist = input("> ")  # Python 3
print(f"Distance: {dist}")

print("Enter a time:")
time = input("> ")  # Python 3
print("Target Time:", time)

tpk, true_time = target_and_distance(time, dist)

print(f"Time per k: {tpk}")
print("Actual Time:", true_time)