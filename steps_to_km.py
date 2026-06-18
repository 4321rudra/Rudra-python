def steps_to_km(steps):
    kilometers=steps*0.75/1000
    return kilometers
my_steps=12000
distance_walked=steps_to_km(my_steps)
print(f"Today's Progress: Walked {round(distance_walked,2)} km.")