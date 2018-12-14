from functools import reduce


def first(input, iters):
    elfone = 0
    elftwo = 1
    output = input

    for _ in range(iters + 6):
        score = output[elfone] + output[elftwo]

        if score >= 10:
            output.append(int(score / 10))
            output.append(score % 10)
        else:
            output.append(score)

        elf1 = (elfone + 1 + output[elfone]) % len(output)
        elf2 = (elftwo + 1 + output[elftwo]) % len(output)

    return reduce(lambda x, y: str(x) + str(y), output[iters:iters + 10])


print(first([3, 7], 824501))
