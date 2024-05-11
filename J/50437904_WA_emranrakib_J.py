def is_valid_name(s):
    t_count = s.count('t') + s.count('T')
    return t_count == 1 and s[0].lower() == 't'  # Ensure there is exactly one 't' and it's the first letter


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()

        if is_valid_name(s):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
