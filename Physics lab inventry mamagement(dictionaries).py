data={}
# Function to add new equipment
def add_equipment():
   global data  
   name = input("Enter equipment ")
   quantity = int(input("Enter quantity: "))
   if name in data:
    data[name] = data[name]+ quantity
   

# Function to remove equipment
def remove_equipment():
    global data
    name = input("Enter equipmen ")
    if name in data:
        quantity = int(input("Enter quantity to remove: "))
        if data[name] >= quantity:
            data[name] = data[name] - quantity
            if data[name] == 0:
                del data[name]
        else:
            print("Insufficient quantity!")
    else:
        print("Equipment not found!")

# Function to display all equipment
def display_equipments():

    for name in data :
      print(name)


def main():
    while True:
        print("\n===== Physics Lab Equipment Management =====")
        print("1. Add Equipment")
        print("2. Remove Equipment")
        print("3. Display All Equipment")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_equipment()
        elif choice == '2':
            remove_equipment()
        elif choice == '3':
            display_equipments()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
