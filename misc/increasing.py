def makeIncreasing(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:

            num = str(numbers[i])
            for j in range(1, len(num)):
                x = int(num[j] + num[1:j] + num[0] + num[j + 1:])
                if x > numbers[i - 1] and increasing(numbers, i + 1):
                    return True

            num = str(numbers[i - 1])
            for j in range(1, len(num)):
                x = int(num[j] + num[1:j] + num[0] + num[j + 1:])
                y = numbers[i - 2] if i - 2 >= 0 else - float('inf')
                if y < x < numbers[i] and increasing(numbers, i):
                    return True

            return False

    return True


def increasing(numbers, i):
    for j in range(i + 1, len(numbers)):
        if numbers[j] <= numbers[j - 1]:
            return False

    return True

"""
if n is small:
    brute force
else:
    split n into smaller inputs (divide)
    recursively solve them
    combine solution (conquer)
"""
