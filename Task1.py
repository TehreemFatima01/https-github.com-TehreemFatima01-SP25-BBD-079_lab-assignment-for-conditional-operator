# Program 1: Check if a number is positive, negative, or zero
def check_number():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

# Program 2: Check if a year is a leap year
def check_leap_year():
    year = int(input("Enter a year: "))
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

# Program 3: Simple calculator
def simple_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")
    
    if op == '+':
        print(f"Result: {num1 + num2}")
    elif op == '-':
        print(f"Result: {num1 - num2}")
    elif op == '*':
        print(f"Result: {num1 * num2}")
    elif op == '/':
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error: Division by zero")
    else:
        print("Invalid operator")

# Program 4: Student grade calculator
def student_grade():
    marks = float(input("Enter student's marks: "))
    if marks >= 85:
        grade = 'A'
    elif marks >= 70:
        grade = 'B'
    elif marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    print(f"Grade: {grade}")

# Main menu
def main():
    while True:
        print("\nMenu:")
        print("1. Check number (positive/negative/zero)")
        print("2. Check leap year")
        print("3. Simple calculator")
        print("4. Student grade calculator")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            check_number()
        elif choice == '2':
            check_leap_year()
        elif choice == '3':
            simple_calculator()
        elif choice == '4':
            student_grade()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()