import re


def parse_data(filename):
    # Get all numbers from the input data
    file = open(filename, 'r')
    contents = file.read()
    file.close()
    contents = re.compile('-?\d+').findall(contents)
    contents = [int(i) for i in contents]
    # Returned the parsed input data
    graph = {}
    for i in range(contents[0]):
        graph[i+1] = []
    for i in range(contents[1]):
        graph[contents[2 * i + 2]].append(contents[2 * i + 3])
        graph[contents[2 * i + 3]].append(contents[2 * i + 2])
    return graph, contents[0]


def deg(graph, vertices):
    print(graph)
    degrees = [0]*vertices
    for i in range(vertices):
        degrees[i] += len(graph[i+1])
    return degrees



def main():
    input = parse_data("rosalind_deg.txt")
    answer = deg(input[0], input[1])
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + ' ')
    output.close()


if __name__ == "__main__":
    main()
