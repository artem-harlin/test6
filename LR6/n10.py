motherland = {}
for i in range(int(input())):
    oblasti, *goroda_oblastei = input().split()
    for goroda in goroda_oblastei:
        motherland[goroda] = oblasti
        
for i in range(int(input())):
    print(motherland[input()])

