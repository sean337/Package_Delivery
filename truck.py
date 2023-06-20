class Truck:
    def __init__(self, max_size, load_size, speed, mileage, address, departure_time, total_travel_time):
        self.max_size = max_size
        self.load_size = load_size
        self.packages = []
        self.speed = speed
        self.mileage = mileage
        self.address = address
        self.departure_time = departure_time
        self.total_travel_time = total_travel_time
        self.package_sorting_list = []
        self.delivered_packages = []

    # Loads packages into the truck and adjusts the load size so that it doesn't exceed the max size for that truck
    def load_packages(self, package):
        if self.load_size < self.max_size:
            self.packages.append(package)  # Adds the package to the empty package list
            self.load_size += 1  # Increase the load size by 1

        else:
            print("Truck full! Can't load more packages!")

    # Moves truck to new address and updates the milage accordingly
    def move_to(self, new_address, distance):
        self.address = new_address
        self.mileage += distance

    # Removes Package from truck and marks the package status as delivered and marks delivery time
    def deliver_package(self, package):
        self.packages.remove(package)
        package.delivery_status = "Delivered!"
        package.delivery_time = self.departure_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % \
               (
                   self.max_size, self.load_size, self.packages, self.speed, self.mileage, self.address,
                   self.departure_time, self.total_travel_time
               )
