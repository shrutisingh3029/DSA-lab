n = int(input())
a = input().split()

def inorder(i):
    if i >= n or a[i] == "-":
        return
    inorder(2*i+1)
    print(a[i], end=" ")
    inorder(2*i+2)

def postorder(i):
    if i >= n or a[i] == "-":
        return
    postorder(2*i+1)
    postorder(2*i+2)
    print(a[i], end=" ")

print("Inorder:", end=" ")
inorder(0)
print()

print("Postorder:", end=" ")
postorder(0)