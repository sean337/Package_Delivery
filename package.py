import datetime


class Package:
    def __init__(self, id, address, city, state, postal_code, delivery_deadline, weight, delivery_status):
        self.id = int(id)
        self.weight = int(weight)
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code

        if delivery_deadline != 'EOD':
            self.delivery_deadline = datetime.datetime.strptime(delivery_deadline.strip(), '%I:%M %p').time()
        else:
            self.delivery_deadline = datetime.datetime.strptime('17:00', '%H:%M').time()
        self.delivery_status = delivery_status

        self.departure_time = datetime.timedelta()
        self.delivery_time = datetime.timedelta()

    def update_status(self, current_time):
        if self.delivery_time and self.delivery_time < current_time:
            self.delivery_status = "Delivered"
        elif self.departure_time and self.delivery_time < current_time:
            self.delivery_status = "En Route"
        else:
            self.delivery_status = "At Hub"

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id, self.weight, self.address, self.city, self.state, self.postal_code, self.delivery_deadline,
            self.delivery_status)
