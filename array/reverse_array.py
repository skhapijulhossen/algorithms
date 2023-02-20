# array reversal

def by_loop(array: list) -> list:
    reversed = []
    for idx in range(len(array)-1, -1, -1):
        reversed.append(array[idx])
    return reversed

by_lambda = lambda array: array[::-1]


if __name__ == '__main__':
    array = list(map(int, input('Elements: ').split(' ')))
    print(by_loop(array))
    print(by_lambda(array))
