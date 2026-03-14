class ParkingLot:

    def __init__(self, total_spaces):
        self.spaces = {}

        for i in range(1, total_spaces + 1):
            self.spaces[f"P{i}"] = "Free"

    def show_status(self):
        print("\nParking Lot Status")
        print("------------------")

        for space, status in self.spaces.items():
            print(f"{space} : {status}")