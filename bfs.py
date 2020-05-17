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
    return graph, contents[0]


def bfs(graph, vertices, start):
    distances = [-1] * vertices
    distances[start-1] = 0
    visited = [False] * vertices
    visited[start-1] = True
    queue = [start]
    while len(queue) > 0:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor-1]:
                distances[neighbor-1] = distances[node-1] + 1
                queue.append(neighbor)
                visited[neighbor-1] = True
    return distances


def main():
    input = parse_data("rosalind_bfs.txt")
    answer = bfs(input[0], input[1], 1)
    output = open("output.txt", 'w')
    print(answer)
    for i in range(len(answer)):
        output.write(str(answer[i]) + ' ')
    output.close()


if __name__ == "__main__":
    main()
