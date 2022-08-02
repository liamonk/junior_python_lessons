width = 0
height = 0
cost = 0

def num_check(question):

    valid = False
    while not valid:

        error = ("Please enter a positive value to proceed")

        try:
            response = float(input(question))

            if response > 0:
                return response

            else:
                print()
                print(error)
                print()

        except ValueError:
            print()
            print(error)
            print()


print()
print("*-* " *20, "Fence cost calculator!", "*-* " *20)
print()
print("*_* " *16, "This calculator will only work for rectangular fenced areas", "*_* " *15)

keep_going = ""
while keep_going == "":
    
    print()
    width = num_check("What is the width of the area you are fencing ")
    height = num_check("What is the height of the area you are fencing ")
    area = width * height
    print("The area is {} square units" .format(area))
    perimeter = 2*width + 2*height
    print("The perimeter is {} units" .format(perimeter))
    print()
    cost = num_check("What is the cost per meter?")
    total_cost = perimeter*cost
    print("The cost of fencing is ${}" .format(total_cost))

    keep_going = input("Press <enter> to calculate the cost of another fence or press any key to quit")

print()
print("*-* " *18, "Thanks for using this calculator", "*-* " *18)
print()

