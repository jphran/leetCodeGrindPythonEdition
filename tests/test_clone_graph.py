import unittest
from leet_code_grind import clone_graph


class MyTestCase(unittest.TestCase):
    def test_basic_fn(self):
        node1 = clone_graph.Node(1)
        node2 = clone_graph.Node(2)
        node3 = clone_graph.Node(3)
        node4 = clone_graph.Node(4)

        node1.neighbors = node3.neighbors = [node2, node4]
        node2.neighbors = node4.neighbors = [node1, node3]

        cloned_graph = clone_graph.cloneGraph(None, node1)

        print('Hard to test, just run it in leetcode')


if __name__ == '__main__':
    unittest.main()
