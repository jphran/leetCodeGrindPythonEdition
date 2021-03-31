import collections


class Node:
    """"Definition for a Node."""
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return node

    is_visited = {node: Node(node.val)}
    to_visit = collections.deque([node])

    while to_visit:
        curr_node = to_visit.pop()

        for n in curr_node.neighbors:
            if n not in is_visited:
                neighbor_clone = Node(n.val)
                to_visit.append(n)
                is_visited.update({n: neighbor_clone})
                is_visited[curr_node].neighbors.append(neighbor_clone)
            else:
                is_visited[curr_node].neighbors.append(is_visited[n])

    return is_visited[node]
