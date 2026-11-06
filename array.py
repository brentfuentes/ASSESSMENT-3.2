"""Assessment 3.2 - Array (dynamic program based on Assessment 3.1)"""

array = []


def add(value):
    array.append(value)
    print(f"A[{len(array) - 1}] = '{value}'  ->  {array}")


def remove(index=0):
    if not array:
        print("Array is empty. Nothing to remove.")
        return
    if index < 0 or index >= len(array):
        print(f"Invalid index. Choose 0 to {len(array) - 1}.")
        return
    removed = array.pop(index)
    print(f"Delete index {index}  ->  Removed '{removed}', Array: {array}" +
          (" (Empty)" if not array else ""))


def main():
    while True:
        print("\n=== ARRAY ===")
        print("1. Add element (to end)")
        print("2. Remove element by index")
        print("3. Remove first element (index 0)")
        print("4. Display array")
        print("5. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            value = input("Enter value to add: ")
            for ch in value:          # each character is added one by one, like 3.1
                add(ch)
        elif choice == "2":
            try:
                remove(int(input("Enter index to delete: ")))
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            remove(0)
        elif choice == "4":
            print(f"Array: {array}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()