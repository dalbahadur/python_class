a="2,4,6,d,8,9,e,4"
num=a.split(",")
numbers=filter(str.isdigit,num)
print(sum(map(int,numbers)))

mark_of_students=[
{
    "name":"Ram",
    "mark":{"math":80,"science":85,"computer":90},
},
{
    "name":"sarita",
    "mark":{"maths":87,"science":79,"computer":85},
},
{
    "name":"hari",
    "mark":{"maths":90,"science":75,"computer":88},

},  
]

for m in mark_of_students:
    print(m.get("name"))
    print(sum(m.get("mark").values()))


    

