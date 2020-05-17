import re


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


def two_sum(input):
    answer = []
    for i in range(input[0]):
        answer.append(two_sum_helper(input[i+1]))
    return answer

def two_sum_helper(a):
    pair = {}
    for i in range(len(a)):
        if -1 * a[i] in pair:
            return "{} {}".format(pair[-1 * a[i]]+1, i+1)
        else:
            pair[a[i]] = i
    return -1


def main():
    input = parse_data("rosalind_2sum.txt")
    answer = two_sum(input)
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + '\n')
    output.close()


if __name__ == "__main__":
    main()
