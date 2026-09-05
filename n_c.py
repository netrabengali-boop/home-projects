print("welcome to holiday planner")

print("step 1: Pick your holiday type")
print("1,Beach Holiday,2,Mountain Holiday")
print()

choice= int(input("enter 1 or 2:"))

if choice == 1:
    print("step 2: Pick your beach activity")
    print("1,swimming,2,sand castle building")
    print()

    beach_activity = int(input("enter 1 or 2:"))

    if beach_activity == 1:
        print("you picked swimming")
        print("best time: morning")
        print("remember to carry: sunscreen and water")
    else:
        print("you picked sandcastle building")
        print("best time: evening")
        print("remember to carry: bucket and spade")


elif choice == 2:
    print("step 2: Pick your mountain activity")
    print("1,hiking,2,camping")
    print()
    mountain_activity = int(input("enter 1 or 2:"))

    if mountain_activity == 1:
        print("you picked hiking")
        print("best time: morning")
        print("remember to carry: water and snacks")
    elif mountain_activity == 2:
        print("you picked camping")
        print("best time: afternoon")
        print("remember to carry: tent and flashlight")
else:
    print("invalid choice")