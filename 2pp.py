q = [None] * 100
front = 0
rear = -1

n = int(input())

for _ in range(n):
    x = input()

    if x.startswith("ARRIVE"):
        rear += 1
        q[rear] = x[7:]
        print("Arrived:", q[rear])

    elif x == "SERVE":
        if front > rear:
            print("Serving: No patients")
        else:
            print("Serving:", q[front])
            front += 1

    elif x == "QUEUE":
        if front > rear:
            print("Waiting: No patients")
        else:
            print("Waiting:", end=" ")
            for i in range(front, rear + 1):
                print(q[i], end=" ")
            print()