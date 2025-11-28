# Conditional Statements (if, else, elif)
def name_checker():...
# def name_checker():
#     """
#     This is function which ask for input and prints the category of person by its name!
#     """
#     name = input("Enter your name !\n")

#     if name == "ram": # if
#         print("You're a god!")

#     elif name == "ravana": # else if
#         print("You're a demon!")

#     else: # else
#         print("You're a normal animal!")


    # """
    # if category == "animal":
    #     if name == "ram": # if
    #         print("You're a god!")

    #     elif name == "ravana": # else if
    #         print("You're a demon!")

    #     else: # else
    #         print("You're a normal animal!")
    # elif category == "vehicle":
    #     if brand == "toyota":
    #         if price < 50000:
    #             print("This is cheap vehicle")
    #         elif price > 50000 and price < 200000:
    #             print("This is normal toyota vehicle")
    #         else:
    #             print("This is luxury vehicle")
    # """

    # CTRL + / => does comment / uncomment 
    # CTRL + J => toggle terminal open / close 
    # CTRL + B => toggle sidebar open / close 
    # CTRL + R => opens recent projects selector from top 
    # CTRL + P => opens file selector within the projects or simply you can switch to files by searching and selecting it from the dropdown  
    # CTRL + Shift + P => Different functions or settings choose and perform relevant action  



# Loops (for, while)

# break , continue

# students = ["Ram", "Shyam", "Rita", "Hari", "Gita"]

# for (int i = 0; i <5; i++){
#     printf(students[i])
# }

# for i in list:
    # block start

# for i in students:
#     if i =="Rita":
#         continue
#     print(f"Name of student is {i}\n")



# # while contition :
# #     # block start


# name = ""

# while name != "ram":
#     name = input("Enter the name of person!\n")

# name = ""

# while name is not None:
#     name = input("Enter the name of person!\n")
#     if name == "ram":
#         break

# print(f"Finally got the person {name}")


# Task : WAP, ask for input from terminal (name, age), 
    # if name startswith 's' , dont ask for age,=> you're not eligible by your name
    # if age < 50 ,=> you're not eligible and continue the loop
    # if above condition pass then print the name and age using string formatting


# "".startswith("s")




# while True: # Infinite Loop

#     name = input("Enter your name\n")

#     if not name.startswith("s"):

#         age = int(input("Enter your age\n"))

#         if age > 50:
#             print(f"Hello {name}! You're the eligible one for our choice with age {age}")
#             break
        
#         print(f"{name}, You're not eligible")
#         print("*"*20)
#         continue
    
#     print("You're not eligible by your name")
#     print("*"*20)



# try:
#     age = int(input("Enter your age\n"))
# except:
#     pass



# Special For else loop
# students = ["Ram","Shyam","Umesh"]

# for i in students:
#     if i == "Umesh":
#         break
#     print(i)
# else:
#     print("Nothing") 

## WAP in python (Using Special for else loop):
    #1. Your program should iterate for maximum of 10 times
    #2. if ask for nickname, if entered nickname contains "a" or "r" or "e", then break 
    #3. So if not 1. and 2. is satisfied, then print something relavant in else block 
    


# items = range(3) # 10 
# for i in items: 
#     nickname = input("Enter your nickname\n")
#     nickname = nickname.lower()
#     if "a" in nickname or "r" in nickname or "e" in nickname:
#         print(f"We finally got you {nickname}!")
#         break
# else:
#     print("We didn't get what we searched for !")

# breakpoint()


# String slicing technique

# name = "Rohan Gautam 12 5"

# name_list = ["Rohan Gautam", "12", "5","Abc"]


# # print(name[:5], name[5:], name[6:8])

# print(name_list[-1:])

## Mutable Vs. Immutable Data Types


# Lists:

# Overview & fundamental operations
# Indexing, slicing, & negative indexing
# Looping through lists & conditions
# List methods like .insert(), .append(), .remove(), .sort(), etc.
# List comprehension with conditions


# students = [] # list
# addresses = list() # list

# for i in range(5):
#     age = input("Enter your age\n")
#     students.append(int(age))
    # if name.lower() == "ram":
        # students.remove(name)

# students.sort(reverse=True) # In place


# print("Sorted", sorted(students),"Original" ,students)


# students.remove()
# students.insert()


## Dictionary

# Example
# student = {
#     "name":"Sagar",
#     "age":10,
#     "address":"Chabahil",
#     "country":"Nepal",
# }

# student = dict()
# student = {"age":22}

# student["name"] = "Kiran Pandey"
# student["address"] = "Sankhamul, Baneshwor!"

# # student.setdefault("age",20)
# student["age"] = 20

# print(student, student["name"], student["address"], student.get("abc", "No Value"))


# students = list()
# for i in range(2):
#     name_input = input("Enter your name \n")
#     student = dict(
#         name = name_input,
#     )
#     student["age"] = int(input("Enter your age \n"))
    
#     if student["age"] < 20:
#         # age = student.pop("age")
#         # del student["age"]
#         student.update(
#             age = 0,
#             info = {
#                 "formatted_name":f"Student name is {name_input}"
#             }
#         )
#         # print(f"Skipped age is {age}")
#     students.append(student)
#     print(student.keys())
#     print(student.values())
# print(students)




# destinations = dict(
#     name = "Maldives",
#     price = "100000",
#     currency = "NPR",
#     total_days = 5,
#     total_activities = 25,
# )

# print(len(destinations.keys()))

# for index, value in enumerate(destinations.values()):
#     # print(i, type(i))
#     #  = i
#     # print(key, value)
#     print(index, value)







# # Tuple


# students = ["ram","shyam","rita","gita", "ram"]

# student_tuple = tuple(students)

# print(students, student_tuple)

# for i in student_tuple:
#     print(i)

# print(student_tuple[0:2])


# Set


# students = ["ram","shyam","rita","gita", "ram"]

# student_set = set(students)
# copied_set = set(students)[:2]

# print(students, student_set)

# for i in student_set:
#     print(i)


# breakpoint()
# print(student_set[0:2])



# Build a dictionary with keys:
# Ask input from terminal
# When user enters stop or finish your program should halt and print the dictionary
    # members : [] # Contain all family members name
    # ages : () # contain all family members age
    # job : {} # contain all family members job titles

# family_member = dict(
#     members = [],
#     ages = [],
#     job = [],
# )

# while True:
#     name = input("Enter family member name \n")
#     age = input("Enter family member age \n")
#     job = input("Enter family member job \n")

#     family_member["members"].append(name)
#     family_member["ages"].append(age)
#     family_member["job"].append(job)

#     if input("Do you want to continue or halt herein!") in  ["stop","finish"]:
#         break

# family_member.update(
#     ages = tuple(family_member["ages"]),
#     job = set(family_member["ages"])
# )
# # family_member["ages"] = 
# # family_member["job"] = 

# print(family_member)

