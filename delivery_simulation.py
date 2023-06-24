import csv
import datetime

from hash_map import HashMap
from package import Package
from truck import Truck


# This class handles the simulation of the delivery system
class SimulateDelivery:
    def __init__(self):
        self.package_map = HashMap()
        self.load_package_map()
        self.addresses, self.indexes, self.distances = self.generate_lists()
        self.distance_matrix = self.generate_distance_matrix()
        self.delivered_packages = []

        # Creates Truck Object 1
        self.truck1 = Truck(16, 0, 18, 0, '4001 South 700 East', datetime.timedelta(hours=8),
                            datetime.timedelta())
        # Creates Truck Object 2
        self.truck2 = Truck(16, 0, 18, 0, '4001 South 700 East', datetime.timedelta(hours=10, minutes=20),
                            datetime.timedelta())
        # Creates Truck Object 3
        self.truck3 = Truck(16, 0, 18, 0, '4001 South 700 East', datetime.timedelta(hours=9, minutes=5),
                            datetime.timedelta())

        # List of ID's to manually load in each truck
        self.package_id_truck1 = [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
        self.package_id_truck2 = [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
        self.package_id_truck3 = [2, 4, 5, 7, 8, 9, 10, 11, 25, 28, 32, 33]

        self.load_truck(self.truck1, self.package_id_truck1)
        self.load_truck(self.truck2, self.package_id_truck2)
        self.load_truck(self.truck3, self.package_id_truck3)

        self.deliver_packages(self.truck1)
        self.deliver_packages(self.truck2)
        self.truck3.departure_time = min(self.truck1.total_travel_time, self.truck2.total_travel_time)
        self.deliver_packages(self.truck3)

    # Opens a csv file and creates a list based on the information in the file.
    def csv_to_list(self, file_name):
        with open(file_name) as csv_file:
            csv_object = csv.reader(csv_file)
            return list(csv_object)

    # Creates a hashmap with the package id being the key and value being the package details
    def load_package_map(self):
        package_info = self.csv_to_list("csv_files/packages.csv")
        for list_item in package_info:
            package = Package(list_item[0], list_item[1], list_item[2], list_item[3], list_item[4], list_item[5],
                              list_item[6])
            package.delivery_status = "At the hub"
            self.package_map.insert(package.id, package)

    # Generates a list for addresses, their indexes as well as the distances based on the provided CSV files
    def generate_lists(self):
        address_info = self.csv_to_list("csv_files/addresses.csv")
        address_list = []
        address_indexes = {}
        for i, item in enumerate(address_info):
            address_list.append(item)
            address_indexes[i] = item[0]
        distance_info = self.csv_to_list("csv_files/distances.csv")
        distance_list = []
        for item in distance_info:
            distance_list.append(item)
        return address_list, address_indexes, distance_list

    # Generates symmetrical distance matrix for each address and distance
    def generate_distance_matrix(self):
        address_distance_list = []
        for i in range(len(self.addresses)):
            address_distance_list.append([self.addresses[i][0], self.distances[i]])
        return address_distance_list

    # Returns the distance between 2 addresses of 2 specific packages
    def find_distance(self, address1, address2):
        address1_index = None
        address2_index = None

        for index1, entry1 in enumerate(self.addresses):
            if entry1[1] == address1:
                address1_index = index1
                break
        for index2, entry2 in enumerate(self.addresses):
            if entry2[1] == address2:
                address2_index = index2
                break

        distance = self.distances[address1_index][address2_index]
        if distance == '':
            distance = self.distances[address2_index][address1_index]

        return float(distance)

    # Take a group of package IDs to manually load on the truck. Loads the truck in the properly sorted order
    def load_truck(self, truck, package_id_group):
        for package_ID in package_id_group:
            package = self.package_map.lookup(int(package_ID))
            truck.load_packages(package)

    # Finds the shortest route to the next package destination and updates truck and package times.
    def deliver_packages(self, truck):
        # Takes all the packages out of the truck and into another list to prepare for sorting
        for package in truck.packages:
            truck.package_sorting_list.append(package)
        truck.packages.clear()
        # Adds the nearest neighbor back to the truck
        while len(truck.package_sorting_list) > 0:
            next_distance = float("inf")
            next_package = None
            for package in truck.package_sorting_list:
                if self.find_distance(truck.address, package.address) < next_distance:
                    next_distance = self.find_distance(truck.address, package.address)
                    next_package = package

            truck.packages.append(next_package)
            # Allows trucks to move to the next address given the next packages address and distance
            truck.move_to(next_package.address, next_distance)
            # Calculates the time it will take to get to the next address based on the truck speed
            time_traveled = datetime.timedelta(hours=next_distance / truck.speed)
            truck.package_sorting_list.remove(next_package)
            # Delivers Next Package and adds the information to a delivered package list for each truck
            truck.deliver_package(next_package)
            truck.delivered_packages.append(next_package)
            # Updates the trucks current time at the Package delivery and updates the total travel time
            truck.current_time += time_traveled
            truck.total_travel_time += time_traveled
            # Updates the package delivery and departure time based on the trucks time tracking
            next_package.delivery_time = truck.current_time
            next_package.departure_time = truck.departure_time
