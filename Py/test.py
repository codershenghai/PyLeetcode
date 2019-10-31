
num = 20

for i in (2, 3, 5):
    while num % i == 0:
        num /= i
print(num)