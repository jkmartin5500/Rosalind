import re


def parse_data(filename):
    # Get all numbers from the input data
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    contents = re.compile('-?\d+').findall(contents)
    contents = [int(i) for i in contents]
    # Returned the parsed input data
    return contents[1:]


def ins(a):
    answer = 0
    for i in range(2, len(a)):
        k = i
        while k > 0 and a[k] < a[k-1]:
            a[k], a[k-1] = a[k-1], a[k]
            k -= 1
            answer += 1
    return answer


def main():
    input = parse_data("rosalind_ins.txt")
    answer = ins(input)
    output = open("output.txt", 'w')
    print(answer)
    output.write(str(answer))
    output.close()


if __name__ == "__main__":
    main()
