
class tollbooth :

    class Vehicle :
        def __init__ (self,reg,vehicle_type):
            self.reg = reg
            self.vehicle_type = vehicle_type
    def __init__(self):
        self.amount = 0
        self.cars_count = 0
        self.Vehicles = {}
      


    def Cars_passed(self, ispaid, reg,vehicle_type):

        vehicle = self.Vehicle(reg,vehicle_type)


        if ispaid == "true":
            if vehicle.vehicle_type == "normal":
                self.amount += 100
                print("normal vehicle : Rs 100")

            elif vehicle.vehicle_type == "heavy":
                self.amount += 500
                print("heavy vehicle : Rs 500")
            self.cars_count += 1
        
        else:

            if reg in self.Vehicles:
                self.Vehicles[reg] += 1
            else:
                self.Vehicles[reg] = 1

            if self.Vehicles[reg] >= 5:
                print("Car will not pass")
                

            self.cars_count += 1
            print("vehicle passed without paying ")

        print(f"The total no. of cars {self.cars_count}")


    def Show_info(self):
        print(f"Total amount: Rs.{self.amount}")
        print(f"Total cars: {self.cars_count}")
        print(f"Unpaid records: {self.Vehicles}")

    



