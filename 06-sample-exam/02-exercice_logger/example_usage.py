from starter_code import *

# Some methods to easily showcase activities
def print_run(r):
    print(f"Run on {r.date}: distance={r.distance} km, duration={r.duration} min, "
          f"elevation={r.elevation} %, factor={r.calories_factor:.2f}, "
          f"calories={r.calories}")

def print_swim(s):
    print(f"Swim on {s.date}: distance={s.distance} km, duration={s.duration} min, "
          f"factor={s.calories_factor}, calories={s.calories}")

def print_ride(d):
    print(f"Ride on {d.date}: distance={d.distance} km, duration={d.duration} min, "
          f"elevation={d.elevation} %, factor={d.calories_factor:.2f}, "
          f"calories={d.calories}")

# Valid Run
run1 = Run(date="2025-05-20", distance=10, duration=50, elevation=5)
print_run(run1)
# → Run on 2025-05-20: distance=10 km, duration=50 min, elevation=5 %, factor=10.50, calories=1260

# Invalid Run date
try:
    Run(date="20-05-2025", distance=5, duration=30, elevation=0)
except ValueError as e:
    print(f"Caught error creating Run: {e}")
# → Caught error creating Run: Invalid date format. Use YYYY-MM-DD.


# Valid Swim
swim1 = Swim(date="2025-05-19", distance=1.5, duration=40)
print_swim(swim1)
# → Swim on 2025-05-19: distance=1.5 km, duration=40 min, factor=40, calories=135


# Valid Ride
ride1 = Ride(date="2025-05-18", distance=20, duration=60, elevation=10)
print_ride(ride1)
# → Ride on 2025-05-18: distance=20 km, duration=60 min, elevation=10 %, factor=2.20, calories=880


# Aggregate with ExerciseLog
log = ExerciseLog()
log.add(run1)
log.add(swim1)
log.add(ride1)
total = log.total_calories_burnt()
print(f"Total calories burned across all activities: {total}")
# → Total calories burned across all activities: 2275
