def linear_search(n, x, nums):
    found = False
    for i in range(n):
        if x == nums[i]:
            found = True
            break

    if found:
        return 'Yes'
    else:
        return 'No'


def linear_search_without_range(x, nums):
    filtered = list(filter(lambda num: num == x, nums))
    if len(filtered) > 0:
        return 'Yes'
    else:
        return 'No'


def main():
    res1 = linear_search(5, 40, [10, 20, 30, 40, 50])
    print(res1)
    res2 = linear_search(6, 28, [30, 10, 40, 10, 50, 90])
    print(res2)

    res3 = linear_search_without_range(40, [10, 20, 30, 40, 50])
    print(res3)
    res4 = linear_search_without_range(28, [30, 10, 40, 10, 50, 90])
    print(res4)


if __name__ == "__main__":
    main()
