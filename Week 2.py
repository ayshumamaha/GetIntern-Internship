import json
import os
from datetime import datetime

DATABASE = "database.json"


# ---------------- LOAD DATABASE ---------------- #

def load_database():
    if not os.path.exists(DATABASE):
        with open(DATABASE, "w") as file:
            json.dump([], file)

    try:
        with open(DATABASE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


# ---------------- SAVE DATABASE ---------------- #

def save_database(records):
    with open(DATABASE, "w") as file:
        json.dump(records, file, indent=4)


# ---------------- MENU ---------------- #

def show_menu():
    print("\n========== INVENTORY / TASK MANAGEMENT ENGINE ==========")
    print("1. Add Record")
    print("2. View Records")
    print("3. Update Record")
    print("4. Delete Record")
    print("5. Exit")


# ---------------- ADD RECORD ---------------- #

def add_record(records):

    print("\n----- Add New Record -----")

    name = input("Enter Name: ").strip()

    while True:
        try:
            quantity = int(input("Enter Quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    record = {
        "ID": len(records) + 1,
        "Name": name.title(),
        "Quantity": quantity,
        "Created": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    records.append(record)
    save_database(records)

    print("Record Added Successfully!")


# ---------------- VIEW RECORDS ---------------- #

def view_records(records):

    if not records:
        print("\nNo Records Found.")
        return

    print("\n------------- RECORDS -------------")

    for record in records:
        print(f"ID        : {record['ID']}")
        print(f"Name      : {record['Name']}")
        print(f"Quantity  : {record['Quantity']}")
        print(f"Created   : {record['Created']}")
        print("-" * 35)


# ---------------- UPDATE RECORD ---------------- #

def update_record(records):

    if not records:
        print("\nNo Records Available.")
        return

    view_records(records)

    try:
        record_id = int(input("Enter Record ID to Update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for record in records:

        if record["ID"] == record_id:

            new_name = input("Enter New Name: ").strip()

            while True:
                try:
                    new_quantity = int(input("Enter New Quantity: "))
                    if new_quantity < 0:
                        print("Quantity cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("Please enter a valid number.")

            record["Name"] = new_name.title()
            record["Quantity"] = new_quantity

            save_database(records)

            print("Record Updated Successfully!")

            return

    print("Record Not Found.")


# ---------------- DELETE RECORD ---------------- #

def delete_record(records):

    if not records:
        print("\nNo Records Available.")
        return

    view_records(records)

    try:
        record_id = int(input("Enter Record ID to Delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for record in records:

        if record["ID"] == record_id:

            records.remove(record)

            # Reassign IDs
            for index, item in enumerate(records, start=1):
                item["ID"] = index

            save_database(records)

            print("Record Deleted Successfully!")

            return

    print("Record Not Found.")


# ---------------- MAIN PROGRAM ---------------- #

def main():

    records = load_database()

    while True:

        show_menu()

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_record(records)

        elif choice == "2":
            view_records(records)

        elif choice == "3":
            update_record(records)

        elif choice == "4":
            delete_record(records)

        elif choice == "5":
            print("\nThank you for using the Inventory/Task Management Engine.")
            break

        else:
            print("Invalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()
