class Employee:
    # Class object variable
    company = "ABC Corporation"

    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Company: {Employee.company}")


# Create instances of the Employee class
emp1 = Employee("John Doe", 30)
emp2 = Employee("Jane Doe", 25)

# Access class object variable using the class name
print("Company:", Employee.company)

# Access class object variable using an instance
print("Company:", emp1.company)

# Modify the class object variable
Employee.company = "XYZ Corporation"

# Print the updated company name
print("Updated Company:", Employee.company)
print("Updated Company:", emp1.company)
print("Updated Company:", emp2.company)

# Call the display_details method
emp1.display_details()
emp2.display_details()
