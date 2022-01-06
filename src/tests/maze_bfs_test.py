import unittest
import maze.maze_bfs as bfs
from pyamaze import maze

class bfsTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_bfs(self):
        amaze = maze(2,2)
        amaze.CreateMaze(loadMaze="src/maze/maze-5x5.csv")
        self.assertEqual(bfs.bfs(amaze),{(1, 2): (1, 1),(1, 3): (1, 2),
        (2, 3): (1, 3),(2, 4): (2, 3),(3, 4): (2, 4),(4, 4): (3, 4),
        (5, 4): (4, 4),(5, 5): (5, 4)})
