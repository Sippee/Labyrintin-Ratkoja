"""Tämä on sovelluksen logiikka
"""

import time
from pyamaze import agent
from src.maze.mazesolver import MazeSolver

ms = MazeSolver(4,4)
ms2 = MazeSolver(4,4)
OPTION = "100"

while OPTION != "0":
    OPTION = input("""Options: \nCTRL+C:Quit \n1:Save a new maze \n \nTimed 200x200 Mazes:
2:Wall Follower 200x200 Maze
3:Dead End Filling 200x200 Maze \n4:BFS 200x200 Maze\n
Restart application after using Timed mazes before using visual ones
The maze has to be completely solved before closed\nVisual 10x10 Mazes:
5:Wall Follower 10x10 \n6:Dead End Filling 10x10 \n7:BFS 10x10 \n""")

    if OPTION == "1":
        x = int(input("Type the wanted heigth of the maze: \n"))
        y = int(input("Type the wanted width of the maze: \n"))
        ms = MazeSolver(x,y)
        ms.maze.CreateMaze(saveMaze=True)
        #mahdollinen ominaisuus uuden labyrintin teon jälkeen voisi heti runata sen
        #dt_string = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        #file = (f'src/maze/maze--{dt_string}.csv')

    elif OPTION == "2":
        ms.maze.CreateMaze(loadMaze="src/maze/maze-200x200.csv")

        starttime=time.time_ns()

        polku = ms.wall_follower()

        endtime=time.time_ns()
        print(f"\nTime elapsed with wall follower: {(endtime-starttime)/1000000} ms\n")

        #ms.maze.run() # mahdollinen tapa korjata ongelma visualisointejen kanssa

    elif OPTION == "3":
        ms.maze.CreateMaze(loadMaze="src/maze/maze-200x200.csv")

        starttime=time.time_ns()

        polku = ms.dead_end_filling()

        endtime=time.time_ns()
        print(f"\nTime elapsed with dead end filling: {(endtime-starttime)/1000000} ms\n")

    elif OPTION == "4":
        ms.maze.CreateMaze(loadMaze="src/maze/maze-200x200.csv")

        starttime=time.time_ns()

        polku = ms.bfs()

        endtime=time.time_ns()
        print(f"\nTime elapsed with BFS: {(endtime-starttime)/1000000} ms\n")

    elif OPTION == "5":
        ms2.maze.CreateMaze(loadMaze="src/maze/maze-10x10.csv")

        polku = ms2.wall_follower()

        a = agent(ms2.maze, footprints=True)

        ms2.maze.tracePath({a:polku})

        ms2.maze.run()

    elif OPTION == "6":
        ms.maze.CreateMaze(loadMaze="src/maze/maze-10x10.csv")

        polku = ms.dead_end_filling()

        a = agent(ms.maze, footprints=True)

        ms.maze.tracePath({a:polku})

        ms.maze.run()

    elif OPTION == "7":
        ms.maze.CreateMaze(loadMaze="src/maze/maze-10x10.csv")

        polku = ms.bfs()

        a = agent(ms.maze, footprints=True)

        ms.maze.tracePath({a:polku})

        ms.maze.run()

    else:
        break
