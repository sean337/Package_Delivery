# Author: Sean Lee
# Student ID: 010506773
# Western Governors University
# Data Structures and Algorithms II (C950)
from delivery_simulation import SimulateDelivery
import datetime

# This is the user interface
user_input = None
print("WGUPS Tracking System\n")
# This allows the user to run the simulation until they quit
while user_input != "quit":
    simulation = SimulateDelivery()
    # Prints the total mileage for all trucks then prompts for user input
    print(f"This route was completed in: "
          f"{round(simulation.truck1.mileage + simulation.truck2.mileage + simulation.truck3.mileage, 2)} miles.\n")
    user_input = input(
        "Enter [1] to get info for all packages at a particular time, \n"
        "Enter [2] to see the information for a single package at a particular time,\n"
        "Enter [quit] to stop running the program: ")
    # This will check the status of all packages at a given time and print out the details
    if user_input == "1":
        user_input = input("Enter a time using the form H:M:S ")
        (h, m, s) = user_input.split(":")
        convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        for package_id in range(1, 41):
            package = simulation.package_map.lookup(package_id)
            package.update_status(convert_time)
            print(str(package))
    # This will check the status of an individual package ID a given time
    elif user_input == "2":
        user_input = input("Enter a package ID: 1 - 40: ")
        selected_package = simulation.package_map.lookup(int(user_input))
        user_input = input("Enter a time using the form H:M:S: ")
        (h, m, s) = user_input.split(":")
        convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        selected_package.update_status(convert_time)
        print(str(selected_package))
        print("\n")
        print("Thanks for using the program")
    elif user_input == "quit":
        print("Thanks for using the program!")
        break
    # This statement makes sure that the user input met the requirements.
    else:
        print("Enter a valid selection")
