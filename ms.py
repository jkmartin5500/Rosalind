import re


def parse_data(filename):
    # Get all numbers from the input data
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    contents = re.compile('-?\d+').findall(contents)
    contents = [int(i) for i in contents]
    # Returned the parsed input data
    input = [contents[0], contents[1:]]
    return input


def ms(a, low, high):
    if high - low <= 1:
        return [a[low]]
    else:
        middle = (high - low) // 2 + low
        left = ms(a, low, middle)
        right = ms(a, middle, high)
        return mer(left, right)


def mer(a, b):
    answer = []
    i, j = 0, 0
    while i < len(a) or j < len(b):
        if i >= len(a):
            answer.append(b[j])
            j += 1
        elif j >= len(b) or a[i] < b[j]:
            answer.append(a[i])
            i += 1
        else:
            answer.append(b[j])
            j += 1
    return answer


def main():
    input = parse_data("rosalind_ms.txt")
    answer = ms(input[1], 0, input[0])
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + ' ')
    output.close()



if __name__ == "__main__":
    main()
