
student_grads = {}

def add(name, grade):
    student_grads[name] = grade
    print("Name added")

def update(name, grade):
    if name in student_grads:
        student_grads[name] = grade
        print("Name updated")
    else:
        print("Student not found")

def delete(name):
    if name in student_grads:
        del student_grads[name]
        print("Name is deleted")
    else:
        print("Student not found")

def display():
    if student_grads:
        for name, grade in student_grads.items():
            print(f"{name}: {grade}")
    else:
        print("No student found")

def main():
    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. Display students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add(name, grade)

        elif choice == 2:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            update(name, grade)

        elif choice == 3:
            name = input("Enter student name: ")
            delete(name)

        elif choice == 4:
            display()

        elif choice == 5:
            print("Exiting program.")
            break

        else:
            print("Invalid choice")

# Run the main function
if __name__ == "__main__":
    main()
