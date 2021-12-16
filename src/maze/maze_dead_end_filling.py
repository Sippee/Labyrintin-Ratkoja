import maze.maze_wallfollower as wf

def dead_end_filling(maze, aloitus = None):
    if aloitus is None:
        aloitus = (maze.rows, maze.cols)
    polku = []
    suunta = "N"
    ratkaistu = False
    nykyruutu = aloitus

    m = dead_end_filler(maze)

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
    dead_ends = []

    for row in range(1,maze.rows+1):
        for column in range(1,maze.cols+1):
            if (maze.maze_map[(row,column)]["W"] is False and maze.maze_map[(row,column)]["N"] is False
            and maze.maze_map[(row,column)]["E"] is False) or (maze.maze_map[(row,column)]["N"] is False and maze.maze_map[(row,column)]["E"] is False
            and maze.maze_map[(row,column)]["S"] is False) or (maze.maze_map[(row,column)]["E"] is False and maze.maze_map[(row,column)]["S"] is False
            and maze.maze_map[(row,column)]["W"] is False) or (maze.maze_map[(row,column)]["S"] is False and maze.maze_map[(row,column)]["W"] is False
            and maze.maze_map[(row,column)]["N"] is False):
                if ((row,column) != (1,1)) and ((row,column) != (maze.rows,maze.cols)):
                    dead_ends.append((row,column))

    return dead_ends

def dead_end_filler(maze):
    for ruutu in dead_end_finder(maze):
        risteys = False

        while risteys is not True:
            if ruutu == (maze.cols, maze.rows):
                break
            elif maze.maze_map[ruutu]["W"] is True:
                maze.maze_map[ruutu]["W"] = 0
                ruutu = (ruutu[0], ruutu[1]-1)
                maze.maze_map[ruutu]["E"] = 0

            elif maze.maze_map[ruutu]["N"] is True:
                maze.maze_map[ruutu]["N"] = 0
                ruutu = (ruutu[0]-1,ruutu[1])
                maze.maze_map[ruutu]["S"] = 0

            elif maze.maze_map[ruutu]["E"] is True:
                maze.maze_map[ruutu]["E"] = 0
                ruutu = (ruutu[0],ruutu[1]+1)
                maze.maze_map[ruutu]["W"] = 0

            elif maze.maze_map[ruutu]["S"] is True:
                maze.maze_map[ruutu]["S"] = 0
                ruutu = (ruutu[0]+1,ruutu[1])
                maze.maze_map[ruutu]["N"] = 0

            if (maze.maze_map[ruutu]["W"] is True and maze.maze_map[ruutu]["N"] is True ) or (maze.maze_map[ruutu]["N"] is True
            and maze.maze_map[ruutu]["E"] is True) or (maze.maze_map[ruutu]["E"] is True and maze.maze_map[ruutu]["S"] is True) or (maze.maze_map[ruutu]["S"] is True
            and maze.maze_map[ruutu]["W"] is True) or (maze.maze_map[ruutu]["W"] is True and maze.maze_map[ruutu]["E"] is True) or (maze.maze_map[ruutu]["N"] is True
            and maze.maze_map[ruutu]["S"] is True):
                risteys = True

    return maze
