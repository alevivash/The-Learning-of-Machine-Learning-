def arithmetic_arranger(problems, show_answers=False):
    results = 0

    print(len(problems))
    print('\n')

    for i in range(len(problems)):
        print(problems[i])

    print('\n')

    parte = problems[0]
    print(parte)
    partes = parte.split('+')

    return problems


# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

parte = problems[0]

print(parte)

partes = parte.split('+')

up, down = partes[0].strip(), partes[1].strip()

print(up)
print(down)

max_len = max(len(up), len(down))

up_aligned = up.rjust(max_len)
down_aligned = down.rjust(max_len)

print(up_aligned)
print(down_aligned)