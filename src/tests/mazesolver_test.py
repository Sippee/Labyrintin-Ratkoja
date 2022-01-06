import unittest
import src.maze.mazesolver as ms
from pyamaze import maze

class TestMazeSolver(unittest.TestCase):
    def setUp(self):
        self.amaze = ms.MazeSolver(2,2)
        self.assertEqual(self.amaze.height,2)
        self.assertEqual(self.amaze.width,2)
        self.amaze.maze.CreateMaze(loadMaze="src/maze/maze-5x5.csv")

    def test_mazesolver(self):
        self.assertIsInstance(self.amaze.maze,maze)

    def test_wall_follower(self):
        self.assertEqual(ms.wallfollower(self.amaze.maze), [(5, 5), (5, 4), (5, 3), (5, 2),
        (5, 2), (4, 2), (4, 2), (4, 3), (3, 3), (3, 2), (3, 1), (4, 1), (5, 1), (5,
 1), (4, 1), (3, 1), (2, 1), (2, 1), (2, 2), (2, 2), (2, 1), (3, 1), (3, 2), (3, 3),
 (3, 3), (4, 3), (4, 3),(4, 2), (5, 2), (5, 3), (5, 4), (4, 4), (3, 4), (2, 4), (2, 3),
 (2, 3), (1, 3), (1, 2), (1, 1)])

    def test_dead_end_filling(self):
        self.assertEqual(ms.dead_end_filling(self.amaze.maze),[(5, 5), (5, 4), (5, 4),
        (4, 4), (3, 4), (2, 4), (2, 3), (2, 3), (1, 3), (1, 2), (1, 1)])

    def test_bfs(self):
        self.assertEqual(ms.bfs(self.amaze.maze), {(1, 2): (1, 1), (1, 3): (1, 2),
        (2, 3): (1, 3), (2, 4): (2, 3), (3, 4): (2, 4),
        (4, 4): (3, 4), (5, 4): (4, 4), (5, 5): (5, 4)})