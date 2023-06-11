class Package:
    def __init__(self, ID, address, city, state, postal_code, delivery_deadline, weight, delivery_status):
        self.ID = ID
        self.weight = int(weight)
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.delivery_deadline = delivery_deadline
        self.delivery_status = delivery_status

        self.departure_time = None
        self.delivery_time = None

    def update_status(self, current_time):
        if self.delivery_time and self.delivery_time < current_time:
            self.delivery_status = "Delivered"
        elif self.departure_time and self.departure_time < current_time:
            self.delivery_status = "En Route"
        else:
            self.delivery_status = "At Hub"

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.weight, self.address, self.city, self.state, self.postal_code, self.delivery_deadline,
            self.delivery_status)
