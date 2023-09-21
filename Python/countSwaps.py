def countSwaps(a, count=0):
    if sorted(a) == a:
        print(f"Array is sorted in {count} swaps.")
        print(f"First Element: {a[0]}")
        print(f"Last Element: {a[-1]}")
        return
    for i in range(0, len(a)):
        x = i
        j = x + 1
        num = a[i]
        while j < len(a) and num > a[j]:
            a[x], a[j] = a[j], a[x]
            count += 1
            j += 1
            x += 1
    countSwaps(a, count)


a = [4, 2, 3, 1]


countSwaps(a)
