"""Assessment 3.2 - Doubly Linked List (dynamic program based on Assessment 3.1)"""


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            print(f"Append '{data}'  ->  [prev: None | data: '{data}' | next: None]")
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            print(f"Append '{data}'  ->  {self}")

    def delete_head(self):
        if self.head is None:
            print("List is empty. Nothing to remove.")
            return
        removed = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
            print(f"Delete from Head  ->  Removed '{removed}', remaining links updated: {self}")
        else:
            self.tail = None
            print(f"Delete from Head  ->  Removed '{removed}' -> List is empty (None).")

    def delete_tail(self):
        if self.tail is None:
            print("List is empty. Nothing to remove.")
            return
        removed = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
            print(f"Delete from Tail  ->  Removed '{removed}', remaining links updated: {self}")
        else:
            self.head = None
            print(f"Delete from Tail  ->  Removed '{removed}' -> List is empty (None).")

    def __str__(self):
        if self.head is None:
            return "None"
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return " <-> ".join(items)

    def reverse_str(self):
        items = []
        current = self.tail
        while current:
            items.append(str(current.data))
            current = current.prev
        return " <-> ".join(items) if items else "None"


def main():
    dll = DoublyLinkedList()
    while True:
        print("\n=== DOUBLY LINKED LIST ===")
        print("1. Append to tail")
        print("2. Delete from head")
        print("3. Delete from tail")
        print("4. Display forward")
        print("5. Display backward")
        print("6. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            for ch in input("Enter value to append: "):
                dll.append(ch)
        elif choice == "2":
            dll.delete_head()
        elif choice == "3":
            dll.delete_tail()
        elif choice == "4":
            print(f"Forward : {dll}")
        elif choice == "5":
            print(f"Backward: {dll.reverse_str()}")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()