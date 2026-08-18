
class tollbooth :
    def __init__(self):
        self.amount = 0
        self.cars_count = 0
        self.collection = []
      


    def Cars_passed(self, ispaid, reg):
        if ispaid == "true":


            self.amount += 100
            self.cars_count += 1
            print("Amount is paid")


        else:
            cnt = 0

            self.cars_count += 1
            print("car passed without paying")

            for i in self.collection:
                if i == reg:
                    cnt += 1
                print (cnt)

            if cnt == 5:
                print("Car will not pass")
            else:
                self.collection.append(reg)

            print(f"The total no. of cars {self.cars_count}")

    def Show_info(self):
        print (f"Record : {self.collection}")

    



