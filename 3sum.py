import re
from datetime import datetime


def parse_data(filename):
    # Get all numbers from the input data
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    contents = re.compile('-?\d+').findall(contents)
    contents = [int(i) for i in contents]
    # Returned the parsed input data
    input = [contents[0]]
    for i in range(contents[0]):
        input.append(contents[contents[1] * i + 2 : contents[1] * (i + 1) + 2])
    return input


def three_sum(input):
    answer = []
    for i in range(input[0]):
        answer.append(three_sum_helper(input[i+1]))
    return answer


def three_sum_helper(a):
    used = set()
    for i in range(len(a)-2):
        for j in range(i+1, len(a)-1):
            if a[i]+a[j] not in used:
                used.add(a[i]+a[j])
                try:
                    k = a.index(-1 * (a[i] + a[j]))
                    return "{} {} {}".format(i+1, j+1, k+1)
                except:
                    pass
    return -1



def main():
    input = parse_data("rosalind_3sum.txt")
    answer = three_sum(input)
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + '\n')
    output.close()


if __name__ == "__main__":
    main()
