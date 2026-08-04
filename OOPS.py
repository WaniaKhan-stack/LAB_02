
class Book :
    def __init__(self, name , author , publisher , edition , price , year , language , genre ,for_sale):
        self.name = name
        self.author = author 
        self.publisher = publisher 
        self.edition = edition 
        self.price = price
        self.year = year
        self.language = language
        self.genre = genre
        self.display_for_sale = for_sale

    def for_sale(self):
        print (self.display_for_sale)

    def Show_info(self):
        print("Name : " , self.name)
        print("Author : " , self.author)
        print("publisher : " , self.publisher)
        print("edition : " , self.edition)
        print("price : " , self.price)
        print ("year :" ,self.year)
        print("language : " , self.language)
        print("genre : " , self.genre)
        print("display_for_sale : " , self.display_for_sale)

    def Converter(self):
        print( self.price / 278.31) 
        

B1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Scribner", "1st", 1099, 1925, "English", "Novel" , True)
B2 = Book("To Kill a Mockingbird", "Harper Lee", "J.B. Lippincott & Co.", "1st", 7.99, 1960, "English", "Novel" , False)

print(B1.name)
print("in Rupees : " ,B1.price)
print(B1.Converter())
B1.for_sale()

