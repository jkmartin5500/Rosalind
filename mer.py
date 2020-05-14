import re


def parse_data(filename):
    # Get all numbers from the input data
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    contents = re.compile('-?\d+').findall(contents)
    contents = [int(i) for i in contents]
    # Returned the parsed input data
    input = [contents[1:1+contents[0]], contents[2+contents[0]:]]
    return input


def mer(a, b):
    print(a, b)
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
    input = parse_data("rosalind_mer.txt")
    answer = mer(input[0], input[1])
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + ' ')
    output.close()


if __name__ == "__main__":
    main()
