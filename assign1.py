
class Student :
    def __init__ (self , student_name , father_name , roll_no , GPA , department) :
        self.student_name = student_name
        self.father_name = father_name
        self.roll_no = roll_no
        self.GPA = GPA
        self.department = department

    def ShowInfo(self) : #function 1
        print("Student Name : ", self.student_name)
        print("Father Name : ", self.father_name)
        print("Roll No : ", self.roll_no)
        print("GPA : ", self.GPA)
        print("Department : ", self.department)

    def CalculatePercentage(self ) : #function 2 (my choice)
    

        self.maths = int(input("Enter your marks for maths : "))
        self.physics = int(input("Enter your marks for physics : "))
        self.chemistry = int(input("Enter your marks for chemistry : "))
        self.english = int(input("Enter your marks for english : "))
        
        total_marks = self.maths + self.physics + self.chemistry + self.english

        percentage = (total_marks / 400) * 100
        print("Your total marks are : ", total_marks)
        print("Your attendance percentage is : ", percentage)
        if (percentage >= 75) :
            print("You are allowed to sit in the exam")
        else :
            print("You are not allowed to sit in the exam")


Showinfo = Student("Ali" , "Ahmed" , 123 , 3.5 , "Computer Science")
print("Ali got", Showinfo.GPA , "GPA")
Showinfo.CalculatePercentage()

print("Maths Marks : ", Showinfo.maths)