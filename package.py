import datetime


class Package:
    def __init__(self, id, address, city, state, postal_code, delivery_deadline, weight):
        self.id = int(id)
        self.weight = int(weight)
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.delivery_status = "Pending..."

        if delivery_deadline != 'EOD':
            self.delivery_deadline = datetime.datetime.strptime(delivery_deadline.strip(), '%I:%M %p').time()
            self.high_priority = True
        else:
            self.delivery_deadline = datetime.datetime.strptime('17:00', '%H:%M').time()
            self.high_priority = False
        self.delivery_status = None

        self.departure_time = None
        self.delivery_time = None

    def update_status(self, current_time):
        if self.delivery_time < current_time:
            self.delivery_status = "Delivered"
        elif self.departure_time > current_time > datetime.timedelta(hours=8):
            self.delivery_status = "In Transit"
        else:
            self.delivery_status = "At Hub"

    def __str__(self):
        return "Package ID: %s,Delivery Address: %s, %s, %s, %s, %s,Delivery Deadline: %s," \
               " High Priority?: %s,\nDelivery Status: %s,\nDelivery Time: %s\n" % (
                   self.id, self.weight, self.address, self.city, self.state, self.postal_code, self.delivery_deadline,
                   self.high_priority, self.delivery_status, self.delivery_time)
