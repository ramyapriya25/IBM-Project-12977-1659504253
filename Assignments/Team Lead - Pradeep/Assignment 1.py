# n = int(input())
n = 1
visited = [0] * n
# print(3%4)



res = 0
for i in range(0, n):
    res = (res + i) % n
    visited[res] = 1
    print(res)

if 0 in visited:
    print("NO")
else:
    print("YES")
