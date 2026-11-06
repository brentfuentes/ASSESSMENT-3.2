"""Assessment 3.2 - Singly Linked List (dynamic program based on Assessment 3.1)"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Append '{data}'  ->  {self}")

    def delete_head(self):
        if self.head is None:
            print("List is empty. Nothing to remove.")
            return
        removed = self.head.data
        self.head = self.head.next
        print(f"Delete Head  ->  Removed '{removed}', List: {self}" +
              (" (Empty)" if self.head is None else ""))

    def __str__(self):
        parts = []
        current = self.head
        while current:
            parts.append(str(current.data))
            current = current.next
        parts.append("None")
        return " -> ".join(parts)


def main():
    sll = SinglyLinkedList()
    while True:
        print("\n=== SINGLY LINKED LIST ===")
        print("1. Append to tail")
        print("2. Delete head")
        print("3. Display list")
        print("4. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            for ch in input("Enter value to append: "):
                sll.append(ch)
        elif choice == "2":
            sll.delete_head()
        elif choice == "3":
            print(f"List: {sll}")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()