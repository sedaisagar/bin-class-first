# WAP to implement


# Family members basic details get
# Name, age, job, salary, currency (USD, NPR) # Make a dict, salary_npr
# Append to list
# Ask until stop / halt is entered on prompt


# details_collect -> return dictionary
# record_family_details -> list append
# halt_checker -> ask wheter to halt or not
# smart_calculator or smart_analyzer -> 


# def normal_function(a,b,c,d,e,f,g,h,i,*args,name="",**kwargs):
#     arg_values = list(args)
#     breakpoint()


# normal_function(
#     1,2,3,4,5,6,7,8,9,"ase",
#     name="Ram Bdr."
# )



# details_collect -> return dictionary
# record_family_details -> list append
# halt_checker -> ask wheter to halt or not
# smart_calculator or smart_analyzer -> 
import tabulate

family_records = []

def details_collect():
    print("-"*10,"Collecting Details", "-"*10)
    return dict(
        name=input("Enter name: \t"),
        age = int(input("Enter age: \t")),
        salary = float(input("Enter salary: \t")),
        currency = input("Enter the currency!: \t"),
    )

def record_family_details(record:dict):
    print("-"*10,"Saving Records", "-"*10)
    family_records.append(record)

def halt_checker():
    ip = input("Do you want to halt herein??\n Type \"yes\" or \"no\"! \n").strip()
    return ip

def smart_calculator():
    for i in family_records:
        if i.get("currency") == "USD":
            # i["salary_npr"] = ""
            # i.update()
            i.setdefault("salary_npr", i["salary"]*100)

def advanced_calculator():
    age_groups = {
        "young": range(0,20),
        "youth": range(20,50),
        "old": range(50,10000),
    }

    for i in family_records:
        age = i.get("age")

        for k,v in age_groups.items():
            if age in v:
                i["age_group"] = k
                break 

def main_collector():
    while True:
        print("*"*25)
        details = details_collect()
        print("*"*25)
        record_family_details(details)
        print("*"*25)
        hc = halt_checker()
        if hc == "yes":
            break

    smart_calculator()
    advanced_calculator()
    table_data = tabulate.tabulate(family_records)
    print(table_data)
# main_collector()


# Anonymous functions (lambda)


# my_anon_func = lambda a,b,c,d,e : a + b + c == e+1 

# result = my_anon_func(1,2,3,4,5)

# print(result)


# make_full_name = lambda f_name, m_name, l_name : f"{f_name} {m_name} {l_name}"

# print(make_full_name("Ram", "Hari", "Neupane"))


# List => Operations
# Map, Filter, Sort, Reduce

# family_records.sort(key = lambda x: x["salary_npr"] if x["currency"] == "USD" else x["salary"], reverse=True)


# Nested Function
# def master(a):
    
#     def manager(b):
        
        
#         def slave(c):
#             return a+b+c
        
        
#         return slave
    
    
#     return manager


# manager = master(1)
# slave = manager(2)
# result = slave(3)

# print(f"Result : {result}")

# Decorators

# @property

# name = ""

# # This is decorator func
# def theif_checker(func):
#     check_pass = False

#     def boss_dada(*args,**kwargs):
#         first_name, middle_name, last_name = args
#         if last_name == "Thapa Badal":
#             last_name = "Chor Neta"
#         nonlocal check_pass
#         check_pass = True
#         global name
#         name = "Ushan Thapa"
#         return cde(*args,**kwargs), check_pass
#         return "Condition Unsatisfied"

#         # return func(first_name,middle_name,last_name,**kwargs)

#     def cde(*args, **kwargs):
#         return "CDE"

#     return boss_dada

# @theif_checker # this is being decorated
# def print_name(first_name, middle_name, last_name): # this is decorted function
#     return "{} {} {}".format(first_name, middle_name, last_name)


# print(print_name("Ram","Bahadur", "Thapa Badal"), name)


# WAP to 
# Ask name input from terminal
# Push to list
# At least 5
# If following keys are in occerance of the names , modify the name with "You are a <special_chars[i]>"
# special_characters = ["Kansha", "Rakshesh", "Thief", "Daku"]
# Print the modified list
# Use a main function and a decorator function to acheive the task



special_characters = ["Kansha", "Rakshesh", "Thief", "Daku"]
# List Comprehension
special_characters = [i.lower() for i in special_characters]

def character_modifier(func):
    def inner(name): # Ram Bdr Daku
        # splitted_name = name.split(" ") 
        name = name.lower()
        # any, all

        if any(i in name for i in special_characters): # any(True, False, False, False) -> True
            character = next(i for i in special_characters if i in name)
            name = f"You are a {character}"
        return func(name)

    return inner


@character_modifier
def main_func(name):
    return name


names = ["Sagar Sedai", "Ushan Thapa", "Kiran Pandey", "Ratnakar Daku", "Krishna Ko Mama Kansha", "Ram Thief"]
mod_names = [main_func(i) for i in names]

print(mod_names)




names = ["ram","shyam","ram","rita","shyam","sita","gita","gita"]

{
    "ram":[0,2],
    "shyam":[1,4], 
}



# (i for i in range(5) if i < 2) # -> (0,1)


# Text File Operations:

# Reading & writing text files
# Modes of file (r, w, a, rb, wb)
# File path handling with the os module




# # Open a file for reading
# with open('example.txt', 'r') as file:
#     content = file.read()  # Reads the entire content
#     print(content)

# # Read line by line
# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line.strip()) # strip() removes newline characters

# # Open a file for writing (overwrites existing content)
# with open('new_file.txt', 'w') as file:
#     file.write("This is the first line.\n")
#     file.write("This is the second line.")

# # Open a file for appending (adds to the end)
# with open('new_file.txt', 'a') as file:
#     file.write("\nThis line is appended.")


# import os

# # Get the current working directory
# current_directory = os.getcwd()
# print(f"Current directory: {current_directory}")

# # Join path components intelligently
# file_path = os.path.join(current_directory, 'data', 'report.txt')
# print(f"Constructed file path: {file_path}")

# # Get the directory name from a path
# directory_name = os.path.dirname(file_path)
# print(f"Directory name: {directory_name}")

# # Get the base name (filename) from a path
# base_name = os.path.basename(file_path)
# print(f"Base name: {base_name}")

# # Check if a path exists
# if os.path.exists(file_path):
#     print(f"{file_path} exists.")
# else:
#     print(f"{file_path} does not exist.")

# # Create directories (if they don't exist)
# os.makedirs(os.path.join(current_directory, 'temp_data'), exist_ok=True)
# print("temp_data directory created (if it didn't exist).")