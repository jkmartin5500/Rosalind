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


def dfs(graph, vertices):
    visited = set()
    search = []
    for i in range(vertices):
        if i+1 not in visited:
            search.append([])
            dfs_recur(graph, visited, search, i+1)
    return search


def dfs_recur(graph, visited, search, start):
    visited.add(start)
    search[len(search)-1].append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recur(graph, visited, search, neighbor)


def cc(graph, vertices):
    search = dfs(graph, vertices)
    return len(search)


def main():
    input = parse_data("rosalind_cc.txt")
    answer = cc(input[0], input[1])
    output = open("output.txt", 'w')
    print(answer)
    output.write(str(answer) + ' ')
    output.close()


if __name__ == "__main__":
    main()
