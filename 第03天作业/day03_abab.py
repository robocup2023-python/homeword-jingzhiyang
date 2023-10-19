import datetime
import random

ans = 1
for i in range(9):
    ans *= 2
    ans += 1
print(ans)

for t in range(1, 14, 2):
    print(("*" * min(t, 14 - t)).center(7))

num = random.randint(0, 10000)
print(len(str(num)))
print(num)
print(str(num)[::-1])

t1 = 123321
print((t1) == str(t1)[::-1])


#
year = random.randint(1000, 4000)
print(f"Year {year} is run: ", (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)))



time = input("输入日期:格式(YYYY-MM-DD)(eg:2022-02-22)::")
# time = "2022-02-22"
print(datetime.datetime.strptime(time, "%Y-%m-%d") - datetime.datetime(int(time[:4]), 1, 1))


