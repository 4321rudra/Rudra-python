
# with open('steps.txt', 'r') as file_object:
#     # Loop through each line one by one
#     for line in file_object:
#         # Each 'line' is a string. We strip whitespace and convert to int for math.
#         step_count = int(line.strip())
#         print(f"Logged Day: {step_count} steps.")
with open('steps.txt','a') as f_object:
    f_object.write("11294\n")
with open('steps.txt','r') as file_object:
    total_steps=0
    for line in file_object:
        total_steps+=int(line.strip())

    print (f"Total steps : {total_steps}")
    # print(type(content))