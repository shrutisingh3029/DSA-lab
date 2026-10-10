class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
n = int(input())

for _ in range(n):
    x = input()

    if x.startswith("INSERT"):
        v = int(x[7:])
        new = Node(v)
        new.next = head
        head = new
        print("Inserted:", v)

    elif x == "DISPLAY":
        print("List:", end="")
        t = head

        if t is None:
            print(" List is empty")
        else:
            while t:
                print(" " + str(t.data), end="")
                t = t.next
            print()