"""Dead end filling algoritmi
"""

import src.maze.maze_wallfollower as wf

def dead_end_filling(maze, aloitus = None):
    """Dead end filling algoritmin päärunko

    Args:
        maze: maze-olio, sisältää tiedon labyrintistä
        aloitus: optional, oletuksena aloitusruutu on labyrintin oikeassa alakulmassa

    Returns:
        polku: dead end filling algoritmin kulkema polku
    """

    if aloitus is None:
        aloitus = (maze.rows, maze.cols)
    polku = []
    suunta = "N"
    ratkaistu = False
    nykyruutu = aloitus

    maze = dead_end_filler(maze)

    while ratkaistu is not True:
        if nykyruutu == (1,1):
            ratkaistu = True

        polku.append(nykyruutu)

        if wf.tarkista_vasen_seina(maze, suunta, nykyruutu):
            suunta = wf.kaanny_vasemmalle(suunta)
            nykyruutu = wf.eteenpain(suunta, nykyruutu)
        else:
            if wf.tarkista_seina_edessa(maze, suunta, nykyruutu):
                nykyruutu = wf.eteenpain(suunta, nykyruutu)
            else:
                suunta = wf.kaanny_ympari(suunta)

    return polku

def dead_end_finder(maze):
    """Tämä methodi toimii umpikujien löytäjänä

    Args:
        maze: maze-olio, sisältää tiedon labyrintistä

    Returns:
        dead_ends: löydetyt umpikujat
    """

    dead_ends = []

    for row in range(1,maze.rows+1):
        for column in range(1,maze.cols+1):
            if (maze.maze_map[(row,column)]["W"] == False
            and maze.maze_map[(row,column)]["N"] == False
            and maze.maze_map[(row,column)]["E"] == False):
                if ((row,column) != (1,1)) and ((row,column) != (maze.rows,maze.cols)):
                    dead_ends.append((row,column))

            if (maze.maze_map[(row,column)]["N"] == False
            and maze.maze_map[(row,column)]["E"] == False
            and maze.maze_map[(row,column)]["S"] == False):
                if ((row,column) != (1,1)) and ((row,column) != (maze.rows,maze.cols)):
                    dead_ends.append((row,column))

            if (maze.maze_map[(row,column)]["E"] == False
            and maze.maze_map[(row,column)]["S"] == False
            and maze.maze_map[(row,column)]["W"] == False):
                if ((row,column) != (1,1)) and ((row,column) != (maze.rows,maze.cols)):
                    dead_ends.append((row,column))

            if (maze.maze_map[(row,column)]["S"] == False
            and maze.maze_map[(row,column)]["W"] == False
            and maze.maze_map[(row,column)]["N"] == False):
                if ((row,column) != (1,1)) and ((row,column) != (maze.rows,maze.cols)):
                    dead_ends.append((row,column))

    return dead_ends

def dead_end_filler(maze):
    """Tämä methodi täyttää labyrintin umpikujat siihen saakka, kun päästään risteykseen,
    jota pitkin algoritmi kulkee maaliin

    Args:
        maze: maze-olio, sisältää tiedon labyrintistä

    Returns:
        maze: maze-olio, palauttaa maze-olion, jonka umpikujat ovat suljettu
    """

    for ruutu in dead_end_finder(maze):
        risteys = False

        while risteys is not True:
            if ruutu == (maze.cols, maze.rows):
                break
            if maze.maze_map[ruutu]["W"] == True:
                maze.maze_map[ruutu]["W"] = 0
                ruutu = (ruutu[0], ruutu[1]-1)
                maze.maze_map[ruutu]["E"] = 0

            elif maze.maze_map[ruutu]["N"] == True:
                maze.maze_map[ruutu]["N"] = 0
                ruutu = (ruutu[0]-1,ruutu[1])
                maze.maze_map[ruutu]["S"] = 0

            elif maze.maze_map[ruutu]["E"] == True:
                maze.maze_map[ruutu]["E"] = 0
                ruutu = (ruutu[0],ruutu[1]+1)
                maze.maze_map[ruutu]["W"] = 0

            elif maze.maze_map[ruutu]["S"] == True:
                maze.maze_map[ruutu]["S"] = 0
                ruutu = (ruutu[0]+1,ruutu[1])
                maze.maze_map[ruutu]["N"] = 0

            if (maze.maze_map[ruutu]["W"] == True
            and maze.maze_map[ruutu]["N"] == True ) or (maze.maze_map[ruutu]["N"] == True
            and maze.maze_map[ruutu]["E"] == True):
                risteys = True

            elif (maze.maze_map[ruutu]["E"] == True
            and maze.maze_map[ruutu]["S"] == True) or (maze.maze_map[ruutu]["S"] == True
            and maze.maze_map[ruutu]["W"] == True):
                risteys = True

            elif (maze.maze_map[ruutu]["W"] == True
            and maze.maze_map[ruutu]["E"] == True) or (maze.maze_map[ruutu]["N"] == True
            and maze.maze_map[ruutu]["S"] == True):
                risteys = True

    return maze
