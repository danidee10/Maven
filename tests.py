import unittest
from paths import Activity, criticalPath


A = Activity('A', ('0',), 2, 3)
B = Activity('B', ('A',), 6, 3)
C = Activity('C', ('A',), 7, 3)
D = Activity('C', ('B',), 3, 3)
E = Activity('C', ('C',), 1, 3)


class BasicMethodTests(unittest.TestCase):

    def setUp(self):
        self.all_objects = [A, B, C]
        self.starting_nodes = criticalPath.get_starting_nodes(self)

    def test_get_starting_nodes(self):
        self.assertEqual([A], self.starting_nodes)

if __name__ == '__main__':
    unittest.main()
