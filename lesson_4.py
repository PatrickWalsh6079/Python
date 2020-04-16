

# DATA TYPE CONVERSION





# OBJECT ORIENTED PROGRAMMING (OOP) 
# CLASSES   

# naming the class
class Dog():

  # initiate the class instance
  # define the class attributes
  def __init__(self, name, age, house_trained):

    self.name = name
    self.age = age
    self.house_trained = house_trained

  # create a method 
  def is_puppy(self):

    puppy_or_dog = ""

    if self.age > 3:
      puppy_or_dog = "dog"

    else:
      puppy_or_dog = "puppy"

    return puppy_or_dog

  # display a message using __str__ method  
  def __str__(self):

    # use RETURN never Print()   
    return f"Dog: {self.name}\nAge: {self.age}\nHouse trained? {self.house_trained}\nIs puppy or dog? {self.is_puppy()}\n"
  

  
my_dog = Dog("Daisy", 2, True)
# print(my_dog.house_trained)
print(my_dog)


your_dog = Dog("Fido", 6, False)
print(your_dog)





