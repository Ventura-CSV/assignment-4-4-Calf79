def main():

    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    for i in range(5):
        num= int(input(f'enter value:'))
        numbers.append(num)
    minval=numbers[0]
    maxval=numbers[0]
    for num in numbers:
        if num<minval:
            minval=num
        if num>maxval:
            maxval=num
    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
