import unittest
import src.maze.maze_wallfollower as wf
from pyamaze import maze

class Testwallfollower(unittest.TestCase):
    def setUp(self):
        pass
    def test_wf(self):
        amaze = maze(2,2)
        amaze.CreateMaze(loadMaze="src/maze/maze-5x5.csv")
        self.assertEqual(wf.wallfollower(amaze),[(5, 5),(5, 4),(5, 3),
        (5, 2),(5, 2),(4, 2),(4, 2),(4, 3),(3, 3),(3, 2),(3, 1),(4, 1),
        (5, 1),(5, 1),(4, 1),(3, 1),(2, 1),(2, 1),(2, 2),(2, 2),(2, 1),
        (3, 1),(3, 2),(3, 3),(3, 3),(4, 3),(4, 3),(4, 2),(5, 2),(5, 3),
        (5, 4),(4, 4),(3, 4),(2, 4),(2, 3),(2, 3),(1, 3),(1, 2),(1, 1)])
