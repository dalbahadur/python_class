""" def welcome():
    print("welcome to everyone of function class")

welcome()
welcome()
# taking 15 integer value in our list then in main all value in mainlist
# talking even value from main list and other in odd value from main list
# taking duplicat value from main value then store the duplicate value in duplicate listd


 """
main=[]
even=[]
odd=[]
duplicate=[]
for i in range(15):
    num=int(input("enter any number:"))
    if num in main:
        duplicate.append(num)
    else:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    main.append(num)

print(main)
print(even)
print(odd)
print(duplicate)


