students = {
    "count": 2,
    "data": [
        {
            "name": "Ram",
            "address": "Tinknune",
            "course": "Python Django",
            "attendance": [
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 24,
                    "absent": 1,
                    "leave": 0,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 20,
                    "absent": 2,
                    "leave": 6,
                }
            ]
        },
        {
            "name": "Hari",
            "address": "Tinknune",
            "course": "Python Django",
            "attendance": [
                {
                    "month": "January",
                    "total_working_days": 25,
                    "present": 23,
                    "absent": 1,
                    "leave": 1,
                },
                {
                    "month": "February",
                    "total_working_days": 28,
                    "present": 27,
                    "absent": 0,
                    "leave": 1,
                }
            ]
        }
    ]
}

# now printing the value
print(f"Name:{students.get('count')}")
""" data=students.get("data")
for data in data:
    for k, v in data.items():
        print(k, v.get('name'))
        print(k, v.get('address'))
        print(k, v.get('course'))
        
    
 """
""" print(students.values())
for values in students.values():
    print(values)
 """


data= students.get("data")
for data in data:
    print(f"name:{data.get('name')},address:{data.get('address')} and course:{data.get('course')}")

mydata=students.get("data")
for mydata in mydata:
    for k, v in mydata.items():
        print(v,k)
    



        



    
