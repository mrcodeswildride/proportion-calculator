print()

num_boys = int(input("How many boys are in the class? "))
num_girls = int(input("How many girls are in the class? "))
num_students = num_boys + num_girls

decimal = num_boys / num_students
boys_percent = decimal * 100

decimal = num_girls / num_students
girls_percent = decimal * 100

print(f"\nThe class is {boys_percent:.2f}% boys and {girls_percent:.2f}% girls.")
