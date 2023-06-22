graph = {}

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# 定义一个无穷大的值
infinity = float("inf")
# 创建开销的哈希表
costs = {"a": 6, "b": 2, "fin": infinity}
# 创建父节点的哈希表

parents = {"a": "start", "b": "start", "fin": None}

processed = []


def find_low_cost_node(cost_nodes):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in cost_nodes:
        cost = cost_nodes[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def find_low_cost():
    node = find_low_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        print(node)
        processed.append(node)
        node = find_low_cost_node(costs)


if __name__ == '__main__':
    find_low_cost()
