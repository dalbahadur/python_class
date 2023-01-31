 # map, filter
# lambda: syantax: a=lambda x,y: x+y
a=[1,2,3,4,5,6,7]


# map syantax: map(fnc,iteratble object)

# m=lambda x,y:x*y
# print(m(3,5))

def increase_by(x):
    return x+2

result=map(increase_by,a)
print(list(result))
output=map(lambda n:n+1,a)
print(list(output))
  
name_list=["ram","shyam","sita","meera","hari"]

result=map(lambda name:name.capitalize(),name_list)
result1=map(str.capitalize,name_list) # plassing the references of the captitalizse()

print(list(result))
print(list(result1))

# filter (func, literable_object)
 # this function should always return the boolean  value
a=[1,2,3,4,5,6,7,8,9,10]
result=filter(lambda x:x%==0,a)
print(list(result))

