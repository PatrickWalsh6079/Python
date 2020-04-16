


# FUNCTIONS
def simple_function(number):
  
  return number * 2

times4 = simple_function(4)
times5 = simple_function(5)
times10 = simple_function(10)

# print(times4)
# print(times5)
# print(times10)

# INDEXING
name = "Bubba Fett"

list_of_names = ["R2", "BB8", "Rey", "General Grievous"]
# print(name[::-1])


# SLICING
# print(list_of_names[:3])


# .FORMAT() METHOD


# print("Hey my name is {}".format(name))
# print("My dad named me {}".format(name))
# print("And I have always been named {} my whole life".format(name))
# print("And I am the best {} there is!".format(name))


# F STRING LITERALS
# print(f"Hey my name is {name}")


# INPUT() METHOD
# my_password = input("Tell me the password, yo!\n\n")

# if my_password == "thereisnopassword":
#   print("YAY! YOu are in sir")
# else:
#   print("VIRUS DETECTED. PREPARE FOR COMPUTER SHUTDOWN MWAHAHAHAAH")


# ESCAPE CHARACTERS


print("Here is text \t Here is space \t here is \"more text\" in quotes")



# STRING METHODS   
my_string = "3.8"

print(my_string.upper())
print(my_string.lower())
print(len(my_string))
print(my_string.capitalize())
print(my_string.isalnum()) # alphanumeric, cannot have spaces
print(my_string.isalpha()) # alphabetic, cannot have spaces
print(my_string.isascii()) # alphabetic, can have spaces 
print(my_string.isdigit()) # numeric, cannot have spaces
print(my_string.isupper())
print(my_string.islower())


# LIST METHODS   

my_list = [1,2,3,"four","five","six"]

my_list.append("seven")
# my_list.clear()
my_list.pop()
my_list.remove("four")
my_list.reverse()
my_list = [1,5,8,32,6,5]
my_list.sort() # list must be either all numbers or all strings

print(my_list)