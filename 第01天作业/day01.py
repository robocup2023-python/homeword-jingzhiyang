from itertools import permutations

# no1
print(*["".join([str(x) for x in i]) for i in permutations(range(1,5),3)])

# no2
print(*sorted([int(i) for i in input("Enter 3 num: ").split()]))

# no3
a,b = 0,1
for i in range(20):
    print(a,end=' ')
    a,b = b,a+b
print()
    
# no4
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=' ')
    print()




