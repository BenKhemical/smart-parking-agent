class SensorAgent:

    def __init__(self, parking_lot):
        self.parking_lot = parking_lot

    def detect_free_space(self):

        for space, status in self.parking_lot.spaces.items():

            if status == "Free":
                return space

        return None