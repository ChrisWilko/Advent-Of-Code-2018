from collections import Counter


def first():
    two = 0
    three = 0

    with open('input.txt', 'r') as file:
        for line in file:
            freq = Counter(line)
            if 2 in freq.values():
                two += 1
            if 3 in freq.values():
                three += 1
    print(two, three)
    print(two*three)


def second():
    with open('input.txt', 'r') as file:
        lines = [line.rstrip() for line in file]
        for i, one in enumerate(lines):
            for two in lines[i+1:]:
                same = []
                for l1, l2 in zip(one, two):
                    if l1 == l2:
                        same.append(l1)
                if len(two)-len(same) == 1:
                    return ''.join(same)


first()
print(second())
