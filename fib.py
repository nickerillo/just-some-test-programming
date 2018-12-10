print("1, 1, 2, 3, 5, 8, 13, 21 this should be the outcome")

n = 8
x = 1
y = 1
count = 1

if(n<1):
    print("you wont get a single diget if u dont change n")
elif(n==1):
    print("of course the outcome is one u dummy")
else:
    while(count < n):
        print(x, end=", ")
        nth = x + y
        x = y
        y = nth
        count = count + 1
    while(count == n):
        print(x)
        count = count + 1
