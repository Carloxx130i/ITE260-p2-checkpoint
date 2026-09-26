Stotal = int(input("How many students? "))
print()

for i in range(Stotal):
    print("Student", i + 1)

    name = input("Enter name: ")

    act1 = int(input("Activity 1: "))
    act2 = int(input("Activity 2: "))
    act3 = int(input("Activity 3: "))
    totals = act1 + act2 + act3
    averages = totals / 3

    print("Average:", averages)

    if averages >= 90:
        print("Status: Excellent")
    elif averages >= 80:
        print("Status: Very Good")
    elif averages >= 75:
        print("Status: Passed")
else:
        print("Status: Failed")

    print()