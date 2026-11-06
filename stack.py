"""Assessment 3.2 - Stack, LIFO (dynamic program based on Assessment 3.1)"""

stack = []


def push(value):
    stack.append(value)
    print(f"append('{value}')  ->  Stack: {stack}")


def pop():
    if not stack:
        print("Stack is empty. Nothing to pop.")
        return
    removed = stack.pop()
    print(f"pop()  ->  Output: '{removed}', Stack: {stack}" +
          (" (Empty)" if not stack else ""))


def main():
    while True:
        print("\n=== STACK (LIFO) ===")
        print("1. Push / append")
        print("2. Pop")
        print("3. Peek (top element)")
        print("4. Display stack")
        print("5. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            for ch in input("Enter value to push: "):
                push(ch)
        elif choice == "2":
            pop()
        elif choice == "3":
            print(f"Top: '{stack[-1]}'" if stack else "Stack is empty.")
        elif choice == "4":
            print(f"Stack: {stack}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()