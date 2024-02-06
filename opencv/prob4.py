total = 0

for i in range(0,6):
    num = int(input("Enter number: "))
    choice = input("Do you want to include this number(y for yes; n for no): ")
    if choice == 'y':
        total = total + num
    else: 
        continue

print("The total is : {}".format(total))