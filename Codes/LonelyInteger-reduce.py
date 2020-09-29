from functools import reduce


def find_lonely_integer(numbers):
    """Finds the number that has no twin."""
    lonely_integer = reduce(lambda x, y: x ^ y, numbers)
    return lonely_integer


if __name__ == '__main__':
    number_count = int(input())
    numbers = (int(x) for x in input().split())
    print(find_lonely_integer(numbers))