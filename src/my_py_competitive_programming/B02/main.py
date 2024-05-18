
def get_divisors_of_100_in_range(A, B):
    divided = False
    for i in range(A, B + 1):
        if 100 % A == 0 and 100 % B == 0:
            divided = True
            break
    if divided:
        return 'Yes'
    else:
        return 'No'


def main():
    res1 = get_divisors_of_100_in_range(10, 25)
    res2 = get_divisors_of_100_in_range(13, 55)

    print(res1)
    print(res2)


if __name__ == '__main__':
    main()
