if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
b=[]
for i in arr:
    if i not in b:
        b.append(i)
print(b)

b.sort(reverse=True)
print(b)
