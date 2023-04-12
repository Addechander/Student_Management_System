"""
We are planning to develop a student management system. Using Object-Oriented Programming Paradigm we are planning
to implement the system. Student Management System keeps track of students' information and their academic
performance. You are required to create a Student Class. We are planning to keep records regarding, Roll number, Name,
Address, Contact number, email address. Also Student class should have the following methods: Constructor, getter and
setter for Address, Contact number, email address. Also, add a method to display all information of the student. Write
a program code to define a class Student to meet above-mentioned specifications. Write a program code to create an
object TestStudent of class Student. Test methods of the class Student. 

"""


class Student:

   def __init__(self, name, roll_no):  # constructor
       self.__Roll_number = roll_no
       self.__Name = name
       self.__Address = ""
       self.__Contact_number = ""
       self.__email_address = ""

   # Setters

   def SetAddress(self, address):
       self.__Address = address

   def SetContact_number(self, contact_no):
       self.__Contact_number = contact_no

   def SetEmail_address(self, emailID):
       self.__email_address = emailID

   # Getters

   def GetRoll_number(self):
       return self.__Roll_number

   def GetName(self):
       return self.__Name

   def GetAddress(self):
       return self.__Address

   def GetContact_number(self):
       return self.__Contact_number

   def GetEmail_address(self):
       return self.__email_address

   # Method to Display all the Information of the Student

   def PrintInfo(self):
       print("Student's Information")
       print("Student's Name: ", self.__Name)
       print("Student's Roll Number: ", self.__Roll_number)
       print("Student's Address: ", self.__Address)
       print("Student's Contact Number: ", self.__Contact_number)
       print("Student's Email ID: ", self.__email_address)


class UndergradStudent(Student):

   def __init__(self, name, roll_no, ProjectTitle, DefDate):
       Student.__init__(self, name, roll_no)
       self.__projectTitle = ProjectTitle
       self.__projectDefenceDate = DefDate

   def PrintInfo(self):
       Student.PrintInfo(self)
       print("Project Title: ", self.__projectTitle)
       print("Project Defence Date: ", self.__projectDefenceDate)


class GradStudent(Student):

   def __init__(self, name, roll_no, ResearchTitle):
       Student.__init__(self, name, roll_no)
       self.__researchTitle = ResearchTitle

   def PrintInfo(self):
       Student.PrintInfo(self)
       print("Research Title: ", self.__researchTitle)


def main():

   TestStudent = Student("Prateek", 82)  # Instantiating Base Class

   # Instantiating Sub Classes

   TestUndergradStudent = UndergradStudent("Ratan", 83, "Subclass Testing", "11/4/2021")
   TestGradStudent = GradStudent("Gautam", 84, "Object Oriented Programming")

   # Using Methods to set the value of attributes for class Student

   TestStudent.SetAddress("Kathmandu")
   TestStudent.SetEmail_address("prateekchand208@gmail.com")
   TestStudent.SetContact_number("98xxxxxx41")

   # Using Inheritance to set value for class UndergradStudent

   TestUndergradStudent.SetAddress("Bhairawa")
   TestUndergradStudent.SetEmail_address("ratan209@gmail.com")
   TestUndergradStudent.SetContact_number("98xxxxxx42")

   # Using Inheritance of Base Class to set value for class GradStudent

   TestGradStudent.SetAddress("Chitwan")
   TestGradStudent.SetEmail_address("gautam@210@gmail.com")
   TestGradStudent.SetContact_number("98xxxxxx43")

   # Testing Methods of class Student

   print("")
   print("Print using Methods to get value of attributes for class Student")

   print(TestStudent)  # To test Constructor
   print(TestStudent.GetName())  # To test Name getter Method
   print(TestStudent.GetRoll_number())  # To test Roll Number getter Method
   print(TestStudent.GetAddress())  # To test Address getter Method
   print(TestStudent.GetContact_number())  # To test Contact Number getter Method
   print(TestStudent.GetEmail_address())  # To test Email address getter Method

   print("")
   print('*' * 50)
   print("")
   print("Print using the Method to display all information of class Student")

   TestStudent.PrintInfo()  # To test the Method to Display all the Information of the Student

   print("")
   print('*' * 50)
   print("")

   # Testing Methods of class UndergradStudent
   print("Print using polymorphism to display all information of class UndergradStudent")

   TestUndergradStudent.PrintInfo()

   print("")
   print('*' * 50)
   print("")

   # Testing Methods of class GradStudent
   print("Print using polymorphism to display all information of class GradStudent")

   TestGradStudent.PrintInfo()

   print("")
   print('*' * 50)

main()




