import sys
if __name__ == '__main__':
    nodes_num = 4
    fun_graph = [
        [0, 10, 6, 0],
        [10, 0, 5, 16],
        [6, 5, 0, 6],
        [0, 16, 6, 0]
    ]
    distance = [999] * nodes_num
    parent = [-1] * nodes_num
    distance[0] = 0


    def extract_minimum(row):
        # extract minimum index from given index row
        min_value = 999
        min_index = -1
        for node_index0 in range(nodes_num):
            if fun_graph[row][node_index0] != 0 and fun_graph[row][node_index0] < min_value:
                min_value = fun_graph[row][node_index0]
                min_index = node_index0
        return min_index


    def find_adjacent_node(node_index1):
        adjacent_node_list = []
        for column in range(nodes_num):
            if fun_graph[node_index1][column] != 0:
                adjacent_node_list.append(column)

        return adjacent_node_list


    has_been_finalized = []

    for node_index in range(nodes_num):
        min_adjacent_node = extract_minimum(node_index)

        # find adjacent nodes
        adj = find_adjacent_node(node_index)
        for node in adj:
            if node not in has_been_finalized:
                if distance[node] > distance[node_index] + fun_graph[node_index][node]:
                    distance[node] = distance[node_index] + fun_graph[node_index][node]
                    parent[node] = node_index

        has_been_finalized.append(min_adjacent_node)

    for i in range(len(distance)):
        print(f"Minimum Distance for node {i} is {distance[i]}")

    parent.reverse()
    parent.remove(-1)
    p = set(parent)
    for a in p:
        print(f"Move to node {a}")
    print("Finally move to final node")