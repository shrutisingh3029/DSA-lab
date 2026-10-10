s = [None] * 100
top = -1

n = int(input())

for _ in range(n):
    x = input()

    if x.startswith("DO"):
        top += 1
        s[top] = x[3:]
        print("Done:", s[top])

    elif x == "UNDO":
        if top == -1:
            print("Undone: No actions")
        else:
            print("Undone:", s[top])
            top -= 1

    elif x == "LAST":
        if top == -1:
            print("Last: No actions")
        else:
            print("Last:", s[top])

    elif x == "ACTIONS":
        if top == -1:
            print("Actions: No actions")
        else:
            print("Actions:", end=" ")
            for i in range(top, -1, -1):
                print(s[i], end=" ")
            print()