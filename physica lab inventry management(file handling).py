import os

# Function to add new equipment
def add_equipment(data):
    name = input("Enter equipment: ")
    quantity = int(input("Enter quantity: "))
    print("Adding equipment:", name, "Quantity:", quantity)  
    if name in data:
        data[name] += quantity
    else:
        data[name] = quantity
    return data

# Function to remove equipment
def remove_equipment(data):
    name = input("Enter equipment: ")
    if name in data:
        quantity = int(input("Enter quantity to remove: "))
        if data[name] >= quantity:
            data[name] -= quantity
            if data[name] == 0:
                del data[name]
        else:
            print("Insufficient quantity!")
    else:
        print("Equipment not found!")
    return data

# Function to display all equipment
def display_equipments(data):
    print("List of all equipments:")
    total = 0
    for name, quantity in data.items():
        print(name, "\nQuantity:", quantity)
        total += quantity

# Main function
def main():
    file_name = "Physics_Lab_Equipment.txt"
    data = {}

    # Load data if the file exists
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                name, quantity = line.strip().split(',')
                data[name] = int(quantity)

    while True:
        print("\n===== Physics Lab Equipment Management =====")
        print("1. Add Equipment")
        print("2. Remove Equipment")
        print("3. Display All Equipment")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            data = add_equipment(data)  
        elif choice == '2':
            data = remove_equipment(data)  
        elif choice == '3':
            display_equipments(data)
        elif choice == '4':
            print("Saving data and exiting...")
            # Save data to the file before exiting
            try:
                with open(file_name, 'w') as file:
                    for name, quantity in data.items():
                        file.write(f"{name},{quantity}\n")
                print("Data saved successfully.")
            except Exception as e:
                print("Error occurred while saving data:", e)
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
