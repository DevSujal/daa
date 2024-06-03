def find1(a):
    if par1[a] < 0:
        return a
    par1[a] = find1(par1[a])
    return par1[a]

def merge1(a, b):
    par1[a] = b

def find2(a):
    if par2[a] < 0:
        return a
    par2[a] = find2(par2[a])
    return par2[a]

def merge2(a, b):
    par2[a] = b


n, m = map(int, input().split())

val = [0] * (n + 1)
par1 = [-1] * (n + 1)
par2 = [-1] * (n + 1)
adj = [[] for _ in range(1001)]

p = []

for i in range(m):
    u, v, w = map(int, input().split())
    p.append((w, (u, v)))
    adj[u].append((v, w))
    adj[v].append((u, w))

p.sort(reverse=True)

cnt, cnt1, cnt2 = 0, 0, 0

for i in range(m):
    if p[i][0] == 3:
        a, b = p[i][1]
        x, y = find1(a), find1(b)

        if x != y:
            cnt += 1
            merge1(x, y)

        x, y = find2(a), find2(b)

        if x != y:
            cnt += 1
            merge2(x, y)

    elif p[i][0] == 2:
        a, b = p[i][1]
        x, y = find2(a), find2(b)

        if x != y:
            cnt2 += 1
            merge2(x, y)

    else:
        a, b = p[i][1]
        x, y = find1(a), find1(b)

        if x != y:
            cnt1 += 1
            merge1(x, y)

if cnt // 2 + cnt1 == n - 1 and cnt // 2 + cnt2 == n - 1:
    print(m - cnt // 2 - cnt1 - cnt2)
else:
    print("-1")