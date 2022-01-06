"""Tämä on sovelluksen logiikka
"""

import time
from pyamaze import agent
from maze.mazesolver import MazeSolver

ms = MazeSolver(5,5)
ms2 = MazeSolver(5,5)
OPTION = "100"

while OPTION != "0":
    OPTION = input("""Options:
CTRL+C:Sammuta
1:Tallenna uusi labyrintti

Ajastetut 200x200:
2:Wall Follower
3:Dead End Filling
4:BFS

Visuaalinen 5x5:
5:Wall Follower
6:Dead End Filling
7:BFS
""")

    """Restart application after using Timed mazes before using visual ones
The maze has to be completely solved before closed"""

    if OPTION == "1":
        x = int(input("Type the wanted heigth of the maze: \n"))
        y = int(input("Type the wanted width of the maze: \n"))
        ms = MazeSolver(x,y)
        ms.maze.CreateMaze(saveMaze=True)
        #mahdollinen ominaisuus uuden labyrintin teon jälkeen voisi heti runata sen
        #dt_string = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        #file = (f'src/maze/maze--{dt_string}.csv')

    elif OPTION == "2":
        ms = MazeSolver(5,5)
        ms.maze.CreateMaze(loadMaze="src/maze/maze-200x200.csv")

        starttime=time.time_ns()

        polku = ms.wall_follower()

        endtime=time.time_ns()
        print(f"\nAikaa kului: {(endtime-starttime)/1000000} ms\n")

        #ms.maze.run() # mahdollinen tapa korjata ongelma visualisointejen kanssa

    elif OPTION == "3":
        ms = MazeSolver(5,5)
        ms.maze.CreateMaze(loadMaze="src/maze/maze-200x200.csv")

        starttime=time.time_ns()

        polku = ms.dead_end_filling()

        endtime=time.time_ns()
        print(f"\nAikaa kului: {(endtime-starttime)/1000000} ms\n")

    elif OPTION == "4":
        ms = MazeSolver(5,5)
        ms.maze.CreateMaze(loadMaze="src/maze/maze-200x200.csv")

        starttime=time.time_ns()

        polku = ms.bfs()

        endtime=time.time_ns()
        print(f"\nAikaa kului: {(endtime-starttime)/1000000} ms\n")

    elif OPTION == "5":
        ms2 = MazeSolver(5,5)
        ms2.maze.CreateMaze() #loadMaze="src/maze/maze-5x5.csv"

        polku = ms2.wall_follower()

        a = agent(ms2.maze, footprints=True)

        ms2.maze.tracePath({a:polku})

        ms2.maze.run()

    elif OPTION == "6":
        ms2 = MazeSolver(5,5)
        ms.maze.CreateMaze()

        polku = ms.dead_end_filling()

        a = agent(ms.maze, footprints=True)

        ms.maze.tracePath({a:polku})

        ms.maze.run()

    elif OPTION == "7":
        ms2 = MazeSolver(5,5)
        ms.maze.CreateMaze()

        polku = ms.bfs()

        a = agent(ms.maze, footprints=True)

        ms.maze.tracePath({a:polku})

        ms.maze.run()

    else:
        break
