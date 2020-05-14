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


def maj(input):
    answer = []
    for i in range(input[0]):
        answer.append(majority_element(input[i+1]))
    return answer

def majority_element(a):
    majors = {}
    for i in a:
        if i not in majors:
            majors[i] = 1
        else:
            majors[i] += 1
    major = max(majors, key=majors.get)
    if a.count(major) > len(a) // 2:
        return major
    else:
        return -1


def main():
    input = parse_data("rosalind_maj.txt")
    answer = maj(input)
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + ' ')
    output.close()


if __name__ == "__main__":
    main()
