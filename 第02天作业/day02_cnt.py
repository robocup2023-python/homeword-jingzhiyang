words = input("Enter something: ")
print(f"Character:{len([i for i in words if i.isalpha()])}"
      f"\nNumber:{len([i for i in words if i.isdigit()])}"
      f"\nSpace:{len([i for i in words if i.isspace()])}")

num,times = map(int,input("Enter a & times: ").split())
print(sum([int(str(num) * i) for i in range(1,times+1)]))


height = 100
times = 10
ans = 0
for i in range(1,times+1):
    ans += height
    height /= 2
    ans += height
    
print(ans)
print(height / 2)


print([i for i in range(100,1000) if i == sum([int(j) ** 3 for j in str(i)])])


print([i for i in range(101,201) if all([i % j != 0 for j in range(2,int(i ** 0.5)+1)])])


