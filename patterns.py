# printing rightangle shape with *
for i in range(1,7):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# printing rightangle numbers shape where printing  numbers of colums
for row in range(0,8):
    for col in range(1,row):
        print(col,end=" ")
    print()


# printing rightangle shape numbers with row wise printing while taking input from the user.
n = int(input("enter the number of rows"))
for i in range(0,n):
    for j in range(0,i):
        print(i,end=" ")
    print()
