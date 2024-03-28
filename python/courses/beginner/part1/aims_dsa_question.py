from collections import defaultdict

def maximum_saving(input_network: str) -> int:
    # Parse the input network
    network = []
    for row in input_network.strip().split('\n'):
        row_values = []
        for value in row.split(','):
            try:
                row_values.append(int(value))
            except ValueError:
                row_values.append(-1)
        network.append(row_values)
    n = len(network)

    # Create a list of edges
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if network[i][j] != -1:
                edges.append((network[i][j], i, j))

    # Sort the edges by weight
    edges.sort()

    # Kruskal's algorithm
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    mst_cost = 0
    total_cost = sum(network[i][j] for i in range(n) for j in range(i + 1, n) if network[i][j] != -1)

    for weight, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_cost += weight

    return total_cost - mst_cost

# Test case
input_network = '''-,14,10,19,-,-,-
14,-,-,15,18,-,-
10,-,-,26,,29,-
19,15,26,-,16,17,21
-,18,-,16,-,-,9
-,-,29,17,-,-,25
-,-,-,21,9,25,-
'''
max_saving = maximum_saving(input_network)
print(max_saving)  
