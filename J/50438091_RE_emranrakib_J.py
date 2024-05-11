def is_correct_spelling(s):
    return 'T' in s and s.lower().count('i') >= 1 and s.lower().count('m') >= 1 and s.lower().count('u') >= 1 and s.lower().count('r') >= 1

def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().strip()
        if is_correct_spelling(s):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
