
total_steps=0
while True:
    s=input("Enter steps walked (or type 'quit' to stop): ")
    if s=='quit':
        break
    else:
        
        total_steps+=int(s)
        print("Steps added !")
print(f"Total steps : {total_steps}")
steps=total_steps

if steps>=10000:
    print("Great job! You hit your daily step goal.")
else :
    print(f"Keep moving! You need {10000-steps} more steps to hit 10,000.")
