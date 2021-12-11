import random

N = 10000
RAND_LEN = 100
IMPOSSIBLE_PERCENT = 0.2

def get_and(string):
    return f'{string} and {random.randint(0, 1)}'


def get_or(string):
    return f'{string} or {random.randint(0, 1)}'


def get_bracket(string):
    if random.randint(0, 1):
        return f'({string})'
    else:
        return string


def get_not(string):
    if random.randint(0, 1):
        return f'not {string}'
    else:
        return string


def get_equals(string):
    if random.randint(0, 1):
        return f'{string} == {random.randint(0, 1)}'
    else:
        return string


def get_xor(string):
    return f'{string} ^ {random.randint(0, 1)}'


funcs = [
    get_and,
    get_or,
    get_bracket,
    get_not,
    get_equals,
    get_xor
]


def generate_bool_funcs():
    bool_funcs = []

    for i in range(N):
        bool_func = 'x'
        for j in range(random.randint(1, RAND_LEN)):
            index = random.randint(0, len(funcs) - 1)
            bool_func = funcs[index](bool_func)

        bool_funcs.append(bool_func)

    return bool_funcs


def main():
    while True:
        bool_funcs = generate_bool_funcs()
        bool_funcs_executable = []
        for b in bool_funcs:
            if eval(b.replace('x', '0')) or eval(b.replace('x', '1')):
                bool_funcs_executable.append(b)

        if len(bool_funcs) != len(bool_funcs_executable):
            break

    impossible_percent = float(len(bool_funcs) - len(bool_funcs_executable)) / float(len(bool_funcs))
    while impossible_percent <= IMPOSSIBLE_PERCENT:
        pop_func = bool_funcs_executable.pop()
        bool_funcs.remove(pop_func)
        impossible_percent = float(len(bool_funcs) - len(bool_funcs_executable)) / float(len(bool_funcs))

    with open('bool_funcs.txt', mode='w+', encoding='utf-8') as f:
        f.write('Невыполнимые функции:\n')
        for b in bool_funcs:
            if not b in bool_funcs_executable:
                f.write(f'{b}\n')
        f.write('\n')
        f.write('Выполнимые функции:\n')
        for b in bool_funcs_executable:
            f.write(f'{b}\n')


if __name__ == '__main__':
    main()