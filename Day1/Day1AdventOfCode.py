total = 0
file = open('input.txt', 'r')
for line in file:
        num = float(line)
        total += num
print(total)

count = 0
seen = set()
found = 0

while found == 0:
    file = open('input.txt', 'r')
    for x in file:
        number = float(x)
        count += number
        if count in seen:
            print(count)
            found = 1
            exit()
        else:
            seen.add(count)
