exercise_queue = ["Bench Press", "Incline Dumbbell", "Tricep Pushdowns"]
completed_exercises = []
while exercise_queue:
    a=exercise_queue.pop()
    print(f"Performing set for : {a}")
    completed_exercises.append(a)
print(f"Workout completed ! Exercises finished : {completed_exercises}")