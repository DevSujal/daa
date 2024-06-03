# 5 7
# 1 2 3
# 2 3 3
# 3 4 3
# 5 3 2
# 5 4 1
# 5 2 2
# 1 5 1


string = """5 10
1 4 1
3 1 2
2 5 2
4 3 1
2 3 1
2 1 1
5 1 2
4 5 2
4 2 2
5 3 1"""
string = string.split("\n")
n = int(string[0].split()[0])
m = int(string[0].split()[1])
vertex_list = []
for x in range(1, m + 1):
    vertex_list.append([int(i) for i in string[x].split()])

print(vertex_list, n, m)
both = []
only_men = []
only_women = []
for x in range(m):
    if vertex_list[x][2] == 3:
        both.append(vertex_list[x])
    elif vertex_list[x][2] == 1:
        only_men.append(vertex_list[x])
    else:
        only_women.append(vertex_list[x])

print(both, only_men, only_women)
vertex_set = set()
for x in both:
    vertex_set.add(x[0])
    vertex_set.add(x[1])
temp = set(x for x in vertex_set)
men_count = 0
women_count = 0

for x in only_men:
    if x[0] in vertex_set:
        if x[1] not in vertex_set:
            vertex_set.add(x[1])
    if x[1] in vertex_set:
        if x[0] not in vertex_set:
            vertex_set.add(x[0])

    if x[0] not in vertex_set:
        if x[1] not in vertex_set:
            vertex_set.add(x[0])
            vertex_set.add(x[1])

    if len(vertex_set) == n:
        vertex_set = temp
        men_count += 1

print(vertex_set)
for x in only_women:
    if x[0] in vertex_set:
        if x[1] not in vertex_set:
            vertex_set.add(x[1])
    if x[1] in vertex_set:
        if x[0] not in vertex_set:
            vertex_set.add(x[0])

    if x[0] not in vertex_set:
        if x[1] not in vertex_set:
            vertex_set.add(x[0])
            vertex_set.add(x[1])

    if len(vertex_set) == n:
        vertex_set = temp
        women_count += 1

print((men_count + women_count) // 2)
