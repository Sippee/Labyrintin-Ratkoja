import unittest
import maze.maze_dead_end_filling as deaf
from pyamaze import maze

class dead_end_fillingTest(unittest.TestCase):
    def setUp(self):
        pass
    def test_dead_end_filling(self):
        amaze = maze(2,2)
        amaze.CreateMaze(loadMaze="src/maze/maze-5x5.csv")
        self.assertEqual(deaf.dead_end_filling(amaze),[(5, 5), (5, 4), (5, 4), (4, 4),
        (3, 4), (2, 4), (2, 3), (2, 3), (1, 3), (1, 2), (1, 1)])
