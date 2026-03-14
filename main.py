from parking_lot import ParkingLot
from sensor_agent import SensorAgent
from parking_agent import ParkingManagementAgent


def main():

    parking_lot = ParkingLot(5)

    sensor = SensorAgent(parking_lot)

    agent = ParkingManagementAgent(parking_lot, sensor)

    parking_lot.show_status()

    agent.request_parking("Car1")
    agent.request_parking("Car2")
    agent.request_parking("Car3")

    parking_lot.show_status()

    agent.car_leaves("P2")

    parking_lot.show_status()

    agent.request_parking("Car4")

    parking_lot.show_status()


if __name__ == "__main__":
    main()