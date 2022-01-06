"""Toimii maze-olion luomisessa ja servicenä
"""

from pyamaze import maze
from maze.maze_wallfollower import wallfollower
from maze.maze_dead_end_filling import dead_end_filling
from maze.maze_bfs import bfs

class MazeSolver:
    """Luokka toimii maze-olion luomisessa
    ja servicenä algoritmeille
    """

    def __init__(self, height, width):
        """Luokan konstruktori

        Args:
            height: labyrintin korkeus
            width: labyrintin leveys
        """

        self.height = height
        self.width = width
        self.maze = maze(height,width)

    def wall_follower(self):
        """
        Returns:
            wallfollower: palauttaa wallfollower algoritmin,
            joka palauttaa reitin, jota pitkin se kulki
        """

        return wallfollower(self.maze)

    def dead_end_filling(self):
        """
        Returns:
            dead_end_filling: palauttaa dead end filling algoritmin,
            joka palauttaa reitin, jota pitkin se kulki
        """

        return dead_end_filling(self.maze)

    def bfs(self):
        """
        Returns:
            bfs: palauttaa bfs algoritmin,
            joka palauttaa reitin, jota pitkin se kulki
        """

        return bfs(self.maze)
