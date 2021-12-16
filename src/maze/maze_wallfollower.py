def wallfollower(maze, aloitus = None):
    if aloitus is None:
        aloitus = (maze.rows, maze.cols)
    polku = []
    suunta = "N"
    ratkaistu = False
    nykyruutu = aloitus

    while ratkaistu != True:
        if nykyruutu == (1,1):
            ratkaistu = True

        polku.append(nykyruutu)

        if tarkista_vasen_seina(maze, suunta, nykyruutu):
            suunta = kaanny_vasemmalle(suunta)
            nykyruutu = eteenpain(suunta, nykyruutu)
        else:
            if tarkista_seina_edessa(maze, suunta, nykyruutu):
                nykyruutu = eteenpain(suunta, nykyruutu)
            else:
                suunta = kaanny_ympari(suunta)

    return polku

def tarkista_vasen_seina(maze, suunta, nykyruutu):
    if suunta == "N":
        if maze.maze_map[nykyruutu]["W"] is True:
            return True

    elif suunta == "E":
        if maze.maze_map[nykyruutu]["N"] is True:
            return True

    elif suunta == "S":
        if maze.maze_map[nykyruutu]["E"] is True:
            return True

    elif suunta == "W":
        if maze.maze_map[nykyruutu]["S"] is True:
            return True

    return False

def tarkista_seina_edessa(maze, suunta, nykyruutu):
    if suunta == "N":
        if maze.maze_map[nykyruutu]["N"] is True:
            return True

    elif suunta == "E":
        if maze.maze_map[nykyruutu]["E"] is True:
            return True

    elif suunta == "S":
        if maze.maze_map[nykyruutu]["S"] is True:
            return True

    elif suunta == "W":
        if maze.maze_map[nykyruutu]["W"] is True:
            return True

    return False

def kaanny_vasemmalle(suunta):
    if suunta == "W":
        suunta = "S"

    elif suunta == "N":
        suunta = "W"

    elif suunta == "E":
        suunta = "N"

    elif suunta == "S":
        suunta = "E"

    return suunta

def kaanny_ympari(suunta):
    if suunta == "W":
        suunta = "E"

    elif suunta == "N":
        suunta = "S"

    elif suunta == "E":
        suunta = "W"

    elif suunta == "S":
        suunta = "N"

    return suunta

def eteenpain(suunta, nykyruutu):
    if suunta == "W":
        nykyruutu = (nykyruutu[0],nykyruutu[1]-1)

    elif suunta == "N":
        nykyruutu = (nykyruutu[0]-1,nykyruutu[1])

    elif suunta == "E":
        nykyruutu = (nykyruutu[0],nykyruutu[1]+1)

    elif suunta == "S":
        nykyruutu = (nykyruutu[0]+1,nykyruutu[1])

    return nykyruutu
