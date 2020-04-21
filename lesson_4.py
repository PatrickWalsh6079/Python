# DATA TYPE CONVERSION
'''
4 + 6 <------integers (whole number)
4.200 + 6.001 <----floats (decimals)
"4" <------ string   
"this is another string" < ------ string
'''

my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
# print(my_tuple)

my_string = "this is my string"




# OBJECT ORIENTED PROGRAMMING (OOP) 
# CLASSES  


number_one1 = 5

class DogClass():

  # set attributes 
  def __init__(self, name, age, breed, gender, house_trained):
    self.name = name
    self.age = age
    self.breed = breed 
    self.gender = gender
    self.house_trained = house_trained

  # method
  def is_puppy(self):
    puppy_or_dog = ""

    if self.age > 3:
      puppy_or_dog = "dog"
    else:
      puppy_or_dog = "puppy"

    return puppy_or_dog

  # display a message
  def __str__(self):
    return "Name: {}\nAge: {}\nBreed: {}\nGender: {}\nHouse trained? {}\n".format(self.name,self.age,self.breed,self.gender,self.house_trained)

  
my_dog = DogClass("Jeff", 2, "Golden terrier", "male", True)
print(my_dog.breed)
print(my_dog)



your_dog = DogClass("Astrid", 0, "Dalmatian", "female", False)
print(your_dog.breed)
print(your_dog)



   





