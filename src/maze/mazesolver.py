from pyamaze import maze, agent
from maze.maze_wallfollower import wallfollower
from maze.maze_dead_end_filling import dead_end_filling
from maze.maze_bfs import bfs
#import time

class MazeSolver:
    def __init__(self, x, y, loop_percentage = 0):
        self.x = x
        self.y = y
        self.loop_percentage = loop_percentage
        self.maze = maze(x,y)

    def wall_follower(self):
        return wallfollower(self.maze)

    def dead_end_filling(self):
        return dead_end_filling(self.maze)
    
    def bfs(self):
        return bfs(self.maze)

 #TESTAUSTA VARTEN
"""ms = MazeSolver(10,10)

option = "100"

while option != "0":
    option = input(Options: \n0:Quit \n1:Save a new maze \n \nTimed 200x200 Mazes: \n2:Wall Follower 200x200 Maze 
3:Dead End Filling 200x200 Maze \n4:BFS 200x200 Maze\n \nVisual 10x10 Mazes: 
5:Wall Follower 10x10 \n6:Dead End Filling 10x10 \n7:BFS 10x10 \n)
    if option == "0":
        break

    elif option == "1":
        x = int(input("Type the wanted heigth of the maze: \n"))
        y = int(input("Type the wanted width of the maze: \n"))
        ms = MazeSolver(x,y)
        ms.maze.CreateMaze(saveMaze=True)
        #dt_string = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        #file = (f'maze--{dt_string}.csv')

    elif option == "2":
        ms.maze.CreateMaze(loadMaze="maze-200x200.csv")

        starttime=time.time_ns()

        polku = ms.wall_follower()

        endtime=time.time_ns()
        print(f"\nTime elapsed with wall follower: {(endtime-starttime)/1000000} ms\n")

    elif option == "3":
        ms.maze.CreateMaze(loadMaze="maze-200x200.csv")

        starttime=time.time_ns()

        polku = ms.dead_end_filling()

        endtime=time.time_ns()
        print(f"\nTime elapsed with dead end filling: {(endtime-starttime)/1000000} ms\n")

    elif option == "4":
        ms.maze.CreateMaze(loadMaze="maze-200x200.csv")

        starttime=time.time_ns()

        polku = ms.bfs()

        endtime=time.time_ns()
        print(f"\nTime elapsed with BFS: {(endtime-starttime)/1000000} ms\n")

    elif option == "5":
        ms.maze.CreateMaze(loadMaze="maze-10x10.csv")

        polku = ms.wall_follower()

        a = agent(ms.maze, footprints=True)

        ms.maze.tracePath({a:polku})


    elif option == "6":
        ms.maze.CreateMaze(loadMaze="maze-10x10.csv")

        polku = ms.dead_end_filling()

        a = agent(ms.maze, footprints=True)

        ms.maze.tracePath({a:polku})
    
    elif option == "7":
        ms.maze.CreateMaze(loadMaze="maze-10x10.csv")

        polku = ms.bfs()

        a = agent(ms.maze, footprints=True)

        ms.maze.tracePath({a:polku})
"""
