#a****
#*b***

name = input("enter name: ")

lenght = len(name)

'''
for i in range(0,lenght):
    print("* " * i ,name[i], "* " * (lenght-i-1))
'''
for i in range(0,lenght):
    for j in range(lenght):
        if (j==i):
            print(name[j],end=' ')
        else:
            print("*",end=" ")
    print()
