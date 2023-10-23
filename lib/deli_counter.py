
katz_deli = []

def line(people_in_line):
    for i in range(len(people_in_line)):
        if len(people_in_line) > 0:
            print(f"The line is currently: {i}.{people_in_line[i]}.") 
        else:
            print("The line is currently empty.") 

def take_a_number(lst, str):
    for person in lst:
        print(f"Welcome, {str}. You are number {person}.{lst} in line.")

def now_serving():
    pass

