# row = 4
# for i in range(1 , row + 1):
#     #for spaces
#     for j in range(i):
#         print(" " ,end = "")
#     #for stars
#     for k in range(row + 1 - i ):
#         print("*" , end = "")
    
#     for l in range (row - i) : 
#         print("*" , end="")
    
    
#     print()


class PatternBuilder :
    def __init__ (self , symbol , size):
        self.symbol = symbol
        self.size = size


        

    def firstTriangle(self):
        for i in range (1,self.size + 1):
            for j in range(i):
                print(self.symbol ,end = "")
            
            for k in range(self.size + 1 - i ):
                print(k+1, end = "")

            for l in range(self.size - i , 0 , -1):
                print (l , end="")

            print()

    def HollowSquare(self):
        for i in range(1 , self.size+1):
            for j in range (self.size ):
                if i==1 or i == 4 or j==1 or j == self.size - 1 :

                    print(self.symbol , end="" )
                else :
                    print(" " ,end="")
            print()

hollow = PatternBuilder("*" , 4)
hollow.HollowSquare()

# NumberPattern = PatternBuilder(" " , 4)
# NumberPattern.firstTriangle()