import numpy as np

# Matrix structure: 3 companies (rows), 3 metrics (columns)
sector_data = np.array([
    [360.5, 18.2, 1.5],   # Company A
    [1450.0, 25.4, 0.8],  # Company B
    [420.2, 12.1, 3.2]    # Company C
])
arr=sector_data[:,1]
print(arr)
print(np.round(np.mean(arr),2))
arr2=sector_data[1,:]
print(arr2)
unique=sector_data[1,0]/sector_data[1,1]
print(round(unique,2))
users ={
    'Rudra':{
        'first':'Rudra',
        'last':'Chauhan',
        'location':'Chandigarh',
    },
    'Tanu':{
        'first':'Divya',
        'last':'Chauhan',
        'location':'Delhi',
    },
}
for un,u in users.items():
    print(f"Username : {un}")
    full_name=u['first'] +" "+ u['last']
    print(f"Name : {full_name}")
    print(f"Location : {u['location']}")