num = int(input("1. Square\n2.Triangle\nEnter a number: "))

if num == 1:
    edge = float(input("Enter the side length of the square: "))
    area_sq = edge*edge
    print("Area od the square is" + str(area_sq))

elif num == 2:
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area_tri = (1/2) * base * height
    print("the area of the triangle is: " + str(area_tri))

else:
    print("Invalid choice! Please try again.")