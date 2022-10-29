n = int(input())
d = {}
for i in range(n):
    a = input().split()
    for b in a:
        d[b] = d.get(b, 0) + 1
m = max(d.values())
l = set()
for key in d:
    if d[key] == m:
        l.add(key)
print (sorted(l)[0])