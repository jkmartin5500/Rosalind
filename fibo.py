import re


def parse_data(filename):
    # Get all numbers from the input data
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    input = re.compile('\d+').findall(contents)
    input = [int(i) for i in input]
    # Returned the parsed input data
    return input[0]


def fibo(fibo_dest):
    if fibo_dest < 2:
        return fibo_dest

    sequence = [0, 1]
    for i in range(fibo_dest - 1):
        sequence.append(sequence[i] + sequence[i + 1])
    return sequence[len(sequence) - 1]


def main():
    input = parse_data("sample.txt")
    answer = fibo(input)
    output = open("output.txt", 'w')
    print(answer)
    output.write(str(answer))
    output.close()


if __name__ == "__main__":
    main()
