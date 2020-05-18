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


def par(a):
    i, j = 0, len(a)-2
    key = a[i]
    a[i], a[j+1] = a[j+1], a[i]

    while i < j:
        if a[i] > key:
            a[i], a[j] = a[j], a[i]
            j -= 1
        else:
            i += 1
    a[j], a[len(a)-1] = a[len(a)-1], a[j]
    return a


def main():
    input = parse_data("rosalind_par.txt")
    answer = par(input[1])
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + ' ')
    output.close()



if __name__ == "__main__":
    main()
