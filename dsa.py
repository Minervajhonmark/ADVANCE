import json

students = {
    1: {"name": "John", "age": 19, "srCode": "24-43298"},
    2: {"name": "Jane", "age": 20, "srCode": "24-43299"},
    3: {"name": "Jack", "age": 21, "srCode": "24-43331"},
}

def add_student():
    sid = max(students.keys(), default=0) + 1
    name = input("Enter student name: ")
    while True:
        age_input = input("Enter student age: ")
        if age_input.isdigit():
            age = int(age_input)
            break
        print("Invalid age, enter a number.")
    sr_code = input("Enter student SR code: ")
    students[sid] = {"name": name, "age": age, "srCode": sr_code}
    print(f"✅ Student '{name}' added!\n")

def display_students():
    if not students:
        print("No students found.\n")
        return
    print("\n--- Student List ---")
    for sid, info in students.items():
        print(f"ID:{sid} | Name:{info['name']} | Age:{info['age']} | SR Code:{info['srCode']}")
    print("-------------------\n")

def save_students():
    with open("studentData.json", "w") as f:
        json.dump(students, f, indent=4)
    print("💾 Data saved!\n")

def search_by_name():
    name_query = input("Enter the name to search: ").strip().lower()
    found = [info for info in students.values() if info['name'].lower() == name_query]
    if found:
        print("\n--- Search Results ---")
        for s in found:
            print(f"Name: {s['name']} | Age: {s['age']} | SR Code: {s['srCode']}")
        print("---------------------\n")
    else:
        print("No student found with that name.\n")

menu = {
    "1": add_student,
    "2": display_students,
    "3": save_students,
    "4": search_by_name
}

while True:
    print("1: Add Student  2: Display Students  3: Save Students  4: Search by Name  5: Exit")
    choice = input("Enter your choice: ")

    if choice in menu:
        menu[choice]()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.\n")

