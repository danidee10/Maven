import unittest
from paths import Activity, CriticalPath


A = Activity('A', ('0',), 2, 3)
B = Activity('B', ('A',), 6, 3)
C = Activity('C', ('A',), 7, 3)
D = Activity('D', ('B',), 3, 3)
E = Activity('E', ('C',), 1, 3)


class BasicMethodTests(unittest.TestCase):

    def setUp(self):
        self.all_activities = [A, B, C, D, E]
        self.starting_nodes = criticalPath.get_starting_nodes(self)

    def test_get_starting_nodes(self):
        self.assertEqual([A], self.starting_nodes)

    #def test_build_graph(self):
        #self.assertEqual([[A, D, E], [A, C, E], ])

if __name__ == '__main__':
    unittest.main()