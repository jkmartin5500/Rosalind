import re


def parse_data(filename):
    # Get all numbers from the input data
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    contents = re.compile('-?\d+').findall(contents)
    contents = [int(i) for i in contents]
    # Returned the parsed input data
    input = [0]*(contents[1]+1)
    input[0] = contents[2:2 + contents[0]]
    input[1:] = contents[2 + contents[0]:]
    return input


def bins(a, keys):
    answer = []
    for key in keys:
        answer.append(binary_search(a, 0, len(a)-1, key))
    return answer

def binary_search(a, start, end, key):
    middle = (end - start) // 2 + start
    if end < start:
        return -1
    elif a[middle] == key:
        return middle + 1 # Rosalind is 1 indexed
    elif a[middle] > key:
        return binary_search(a, start, middle-1, key)
    else:
        return binary_search(a, middle+1, end, key)

def main():
    input = parse_data("rosalind_bins.txt")
    answer = bins(input[0], input[1:])
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + ' ')
    output.close()


if __name__ == "__main__":
    main()
