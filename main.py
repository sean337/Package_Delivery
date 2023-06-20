import truck
from delivery_simulation import SimulateDelivery
import datetime

user_input = None
print("WGUPS Tracking System\n")
while user_input != "quit":
    simulation = SimulateDelivery()
    print(f"The route was completed in: "
          f"{simulation.truck1.mileage + simulation.truck2.mileage + simulation.truck3.mileage} miles.\n")
    user_input = input(
        "Enter [1] to get info for all packages at a particular time, \n"
        "Enter [2] to see the information for a single package at a particular time,\n"
        "Enter [quit] to stop running the program: ")
    if user_input == "1":
        user_input = input("Enter a time using the form H:M:S ")
        (h, m, s) = user_input.split(":")
        convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        for package_id in range(1, 40):
            package = simulation.package_map.lookup(package_id)
            package.update_status(convert_time)
            print(str(package))

    elif user_input == "2":
        user_input = input("Enter a package ID:")
        selected_package = simulation.package_map.lookup(int(user_input))
        user_input = input("Enter a time using the form H:M:S")
        (h, m, s) = user_input.split(":")
        convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        selected_package.update_status(convert_time)
        print(str(selected_package))
        print("\n")
        print("Thanks for using the program")
    elif user_input == "quit":
        print("Thanks for using the program!")
        break

    else:
        print("Enter a valid selection")
