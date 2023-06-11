# Author: Sean Lee
import csv
import datetime
from hash_map import HashMap
from package import Package
from truck import Truck


# Opens a csv file and creates a list based on the information in the file.
def csv_to_list(file_name):
    with open(file_name) as csv_file:
        csv_object = csv.reader(csv_file)
        return list(csv_object)


def load_package_data(new_map):
    package_info = csv_to_list("csv_files/packages.csv")
    for list_item in package_info:
        package = Package(list_item[0], list_item[1], list_item[2], list_item[3], list_item[4], list_item[5],
                          list_item[6], "At Hub")
        new_map.insert(package.ID, package)


def load_address_data():
    address_info = csv_to_list("csv_files/addresses.csv")
    address_list = []
    address_indexes = {}
    for i, item in enumerate(address_info):
        address_list.append(item)
        address_indexes[i] = item[0]
    return address_list, address_indexes


def load_distance_data():
    distance_info = csv_to_list("csv_files/distances.csv")
    distance_list = []
    for item in distance_info:
        distance_list.append(item)
    return distance_list


def generate_distance_matrix():
    address_distance_list = []
    for i in range(len(addresses)):
        address_distance_list.append([addresses[i][0], distances[i]])
    return address_distance_list


# Method to find the distance between 2 addresses given the package it's associated with
def find_distance(package1, package2):
    address1 = package1.address
    address2 = package2.address
    address1_index = None
    address2_index = None
    for index1, entry1 in enumerate(addresses):
        if entry1[1] == address1:
            address1_index = index1
            break
    for index2, entry2 in enumerate(addresses):
        if entry2[1] == address2:
            address2_index = index2
            break

    distance = distances[address1_index][address2_index]
    if distance == '':
        distance = distances[address2_index][address1_index]

    return float(distance)


def deliver_packages(truck, find_distance):
    not_delivered = truck.packages

    truck.packages.clear()

    while len(not_delivered) > 0:
        next_distance = float(9000)
        next_package = None
        for package in not_delivered:
            distance = find_distance(truck.address, package.address)
            if distance <= next_distance:
                next_distance = distance
                next_package = package
        truck.packages.append(next_package)
        truck.mileage += next_distance
        truck.address = next_package.address
        truck.departure_time += datetime.timedelta(hours=next_distance / 18)
        next_package.delivery_status = "Delivered"


package_map = HashMap()
load_package_data(package_map)
distances = load_distance_data()
addresses, indexes = load_address_data()
distance_matrix = generate_distance_matrix()

truck1 = Truck(16, None,
               [package_map.lookup(package_id) for package_id in [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]], 18,
               0, '4001 South 700 East',
               datetime.timedelta(hours=8, minutes=0))
truck2 = Truck(16, None, [package_map.lookup(package_id) for package_id in
                          [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]], 18, 0, '4001 South 700 East',
               datetime.timedelta(hours=8, minutes=0))
truck3 = Truck(16, None,
               [package_map.lookup(package_id) for package_id in [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33]], 18, 0,
               '4001 South 700 East',
               datetime.timedelta(hours=8, minutes=0))

for package in truck1.packages:
    print(package)
