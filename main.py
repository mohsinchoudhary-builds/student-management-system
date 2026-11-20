class Student:
    """Represent a single student."""

    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print("-" * 40)
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Course     : {self.course}")
        print("-" * 40)


def main():
    students = []

    print("=" * 40)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)

    while True:
        print("\n1. Add Student")
        print("2. View All Students")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print("\n--- Add New Student ---")
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            age = input("Enter student age: ").strip()
            course = input("Enter course name: ").strip()

            if not student_id or not name or not age or not course:
                print("\nAll fields are required. Please try again.")
                continue

            if not age.isdigit():
                print("\nAge must be a whole number. Please try again.")
                continue

            student = Student(student_id, name, int(age), course)
            students.append(student)
            print(f"\nStudent '{name}' added successfully!")

        elif choice == "2":
            print("\n--- Student Records ---")
            if not students:
                print("No student records found.")
            else:
                for student in students:
                    student.display_info()

        elif choice == "3":
            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
