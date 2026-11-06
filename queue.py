"""Assessment 3.2 - Queue, FIFO (dynamic program based on Assessment 3.1)"""

from collections import deque

queue = deque()


def enqueue(value):
    queue.append(value)
    print(f"append('{value}')  ->  Queue: {list(queue)}")


def dequeue():
    if not queue:
        print("Queue is empty. Nothing to remove.")
        return
    removed = queue.popleft()
    print(f"popleft()  ->  Output: '{removed}', Queue: {list(queue)}" +
          (" (Empty)" if not queue else ""))


def main():
    while True:
        print("\n=== QUEUE (FIFO) ===")
        print("1. Enqueue / append")
        print("2. Dequeue / popleft")
        print("3. Peek (front element)")
        print("4. Display queue")
        print("5. Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            for ch in input("Enter value to enqueue: "):
                enqueue(ch)
        elif choice == "2":
            dequeue()
        elif choice == "3":
            print(f"Front: '{queue[0]}'" if queue else "Queue is empty.")
        elif choice == "4":
            print(f"Queue: {list(queue)}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()