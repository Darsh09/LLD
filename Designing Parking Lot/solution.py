import time
from enum import Enum
from collections import defaultdict

class Fare(Enum):
    CAR = 0.05
    MOTORCYCLE = 0.01
    TRUCK = 0.1 

class Vehicle:
    def __init__(self, number_plate: str, vehicle_type: str):
        self.number_plate = number_plate
        self.vehicle_type = vehicle_type

class ParkingLot:
    available = defaultdict(dict)
    occupied = defaultdict(dict)
    def __init__(self, num_of_entry_points: int, num_of_exit_points: int):
        self.num_of_entry_points = num_of_entry_points
        self.num_of_exit_points = num_of_exit_points

    def add_level(self, config) -> None:
        new_level = max(ParkingLot.available.keys())+1 if len(ParkingLot.available.keys()) > 0 else 0
        for vehicle in config.keys():
            ParkingLot.available[vehicle][new_level] = list(range(config[vehicle]))

    def checkin(self, vehicle: Vehicle) -> tuple:
        # find the level (starting from lowest level) which has an empty spot for the input type of vehicle
        for level in ParkingLot.available[vehicle.vehicle_type].keys():
            if len(ParkingLot.available[vehicle.vehicle_type][level]) > 0:
                # make the spot unavailable 
                spot = ParkingLot.available[vehicle.vehicle_type][level].pop()
                # register the spot for the vehicle in question
                ParkingLot.occupied[vehicle.number_plate] = {'spot': (level, spot), 'time': time.time()}
                return (level, spot)
        return ()
            
    def __calc_fare(vehicle_type, checkin_time) -> float:
        checkout_time = time.time()
        total_time_in_minutes = (checkout_time - checkin_time) / 60
        if vehicle_type == 'car':
            return Fare.CAR.value*total_time_in_minutes
        elif vehicle_type == 'motorcycle':
            return Fare.MOTORCYCLE.value*total_time_in_minutes
        elif vehicle_type == 'truck':
            return Fare.TRUCK.value*total_time_in_minutes
        

    def checkout(self, vehicle: Vehicle) -> float:
        parking = ParkingLot.occupied[vehicle.number_plate] 
        checkin_time = parking['time']
        level, spot = parking['spot'] 
        vehicle_type = vehicle.vehicle_type
        # calculate fare
        fare = ParkingLot.__calc_fare(vehicle_type, checkin_time)
        # Vacate the spot
        del ParkingLot.occupied[vehicle.number_plate]
        # Make it available for use
        ParkingLot.available[vehicle_type][level].append(spot)
        return fare

if __name__ == "__main__":
    parking_lot = ParkingLot(2, 2)
    parking_lot.add_level({ 'car': 5, 'motorcycle': 3, 'truck': 2 })
    car1 = Vehicle('984AY6', 'car')
    car1_parking = parking_lot.checkin(car1)
    print('Car1 parking:', car1_parking)
    truck1 = Vehicle('84YZ6A', 'truck')
    truck2 = Vehicle('74YC6B', 'truck')
    truck2_parking = parking_lot.checkin(truck2)
    truck1_parking = parking_lot.checkin(truck1)
    truck3 = Vehicle('63DB5Z', 'truck')
    truck3_parking = parking_lot.checkin(truck3)
    print('Truck3 parking:', truck3_parking)
    truck1_fare = parking_lot.checkout(truck1)
    print('Truck1 fare at checkout:', truck1_fare)
    truck3_parking = parking_lot.checkin(truck3)
    print('Truck3 parking:', truck3_parking)
    car1_fare = parking_lot.checkout(car1)
    print('Car1 fare at checkout:', car1_fare)
