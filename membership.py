member_database=[]
while True:
    name=input("Enter member name (or type 'quit' to exit) : ")
    if name=='quit':
        break
    age=int(input("Enter member's age : "))
    tpe=input("Enter Membership type : ")
    member_profile={"Member":name,"Age":age,"Membership_Type":tpe}
    member_database.append(member_profile)
    print(f"Member {name} successfully registered!")

for member in member_database:
    print(f"Member: {member['Member']}, Age: {member['Age']}, Status: {member['Membership_Type']}")