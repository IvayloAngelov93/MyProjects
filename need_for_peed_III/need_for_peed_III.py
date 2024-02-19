
class NeedForSpeedIII:

    def __init__(self):
        self.dict_cars = {}

    def create_dict_with_cars_info(self, car, mileage, fuel):
        self.dict_cars[car] = [mileage, fuel]

    def drive_the_car(self,car, distance, fuel):
        if self.dict_cars[car][1] >= fuel:
            self.dict_cars[car][0] += distance
            self.dict_cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if self.dict_cars[car][0] >= 100_000:
                self.dict_cars.pop(car)
                print(f"Time to sell the {car}!")
        else:
            print("Not enough fuel to make that ride")

    def refill_tank(self, car, fuel):
        free_space = 75-self.dict_cars[car][1]
        if free_space < fuel:
            fuel = free_space
        self.dict_cars[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")

    def decrease_mileage(self, car, kilometers):
        self.dict_cars[car][0] -= kilometers
        if self.dict_cars[car][0] < 10_000:
            self.dict_cars[car][0] = 10_000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    def __repr__(self):
        result = []
        for car, value in self.dict_cars.items():
            result.append(f"{car} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
        return '\n'.join(result)

def main():
    need_for_speed_three = NeedForSpeedIII()
    number_of_cars = int(input())
    for _ in range(number_of_cars):
        car_info = input().split("|")
        car = car_info[0]
        mileage = int(car_info[1])
        fuel = int(car_info[2])
        need_for_speed_three.create_dict_with_cars_info(car, mileage, fuel)

    while True:
        commands = input().split(" : ")
        if "Stop" in commands:
            break
        car = commands[1]
        if "Drive" in commands:
            distance = int(commands[2])
            fuel = int(commands[3])
            need_for_speed_three.drive_the_car(car, distance, fuel)
        elif "Refuel" in commands:
            fuel = int(commands[2])
            need_for_speed_three.refill_tank(car, fuel)
        elif "Revert" in commands:
            kilometers = int(commands[2])
            need_for_speed_three.decrease_mileage(car, kilometers)

    print(need_for_speed_three)

if __name__ == '__main__':
    main()