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


def hea(a):
    heap = []
    for i in range(len(a)):
        insert(heap, a[i])
    return heap


def insert(a, x):
    a.append(x)
    i = len(a) - 1
    while i > 0 and a[i] > a[(i-1)//2]:
        a[i], a[(i-1)//2] = a[(i-1)//2], a[i]
        i = (i-1) // 2


def main():
    input = parse_data("rosalind_hea.txt")
    answer = hea(input[1])
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + ' ')
    output.close()



if __name__ == "__main__":
    main()
