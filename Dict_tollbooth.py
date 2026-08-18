
class tollbooth :
    def __init__(self):
        self.amount = 0
        self.cars_count = 0
        self.Vehicles = {}
      


    def Cars_passed(self, ispaid, reg):


        if ispaid == "true":

            self.amount += 100
            self.cars_count += 1
            print("Amount is paid")

        else:

            self.cars_count += 1
            print("Car passed without paying")

            if reg in self.Vehicles:
                self.Vehicles[reg] += 1
            else:
                self.Vehicles[reg] = 1

            if self.Vehicles[reg] >= 5:
                print("Car will not pass")

            print(f"The total no. of cars {self.cars_count}")

    def Show_info(self):
        print (f"Record : {self.Vehicles}")

    



