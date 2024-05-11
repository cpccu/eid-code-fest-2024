def represent_as_round_numbers(n):
    digits = []
    multiplier = 1
    while n > 0:
        digit = n % 10
        if digit != 0:
            digits.append(digit * multiplier)
        n //= 10
        multiplier *= 10
    return digits


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        round_numbers = represent_as_round_numbers(n)
        print(len(round_numbers))
        print(*round_numbers)


if __name__ == "__main__":
    main()
