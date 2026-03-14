class ParkingManagementAgent:

    def __init__(self, parking_lot, sensor):
        self.parking_lot = parking_lot
        self.sensor = sensor

    def request_parking(self, car):

        print(f"\n{car} requesting parking...")

        space = self.sensor.detect_free_space()

        if space:

            self.parking_lot.spaces[space] = "Occupied"

            print(f"{car} assigned to {space}")

        else:

            print("Parking Full")

    def car_leaves(self, space):

        print(f"\nCar leaving {space}")

        if space in self.parking_lot.spaces:

            self.parking_lot.spaces[space] = "Free"

            print(f"{space} is now available")