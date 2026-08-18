from tollbooth import tollbooth

toll1 =tollbooth()
while True :
    user = int (input ("Enter from the option : 1.Cars passed 2.Show info 3.Exit"))
    
    if user == 1 :
        ispaid = input("Enter if the payment is done or not")
        reg = str(input("Enter the registration number :"))
        toll1.Cars_passed(ispaid , reg)

    elif user == 2 :
        toll1.Show_info()
    elif user == 3 :
        print("Thank you ")
        break
        
    else:
        print("invalid input")