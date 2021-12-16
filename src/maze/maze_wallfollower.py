"""Wall follower algoritmi
"""

def wallfollower(maze, aloitus = None):
    """wall follower algoritmin päärunko

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

    while ratkaistu is not True:
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
    """Methodi tarkistaa, onko nykyisen ruudun vasemmalla seinä

    Args:
        maze: maze-olio, sisältää tiedon labyrintistä
        suunta: nykyinen etenemissuunta
        nykyruutu: nykyinen ruutu

    returns:
        Bool: True, jos ei ole seinää, ja False, jos on seinä
    """

    if suunta == "N":
        if maze.maze_map[nykyruutu]["W"] == True:
            return True

    elif suunta == "E":
        if maze.maze_map[nykyruutu]["N"] == True:
            return True

    elif suunta == "S":
        if maze.maze_map[nykyruutu]["E"] == True:
            return True

    elif suunta == "W":
        if maze.maze_map[nykyruutu]["S"] == True:
            return True

    return False

def tarkista_seina_edessa(maze, suunta, nykyruutu):
    """Methodi tarkistaa, onko nykyisen ruudun edessä seinä

    Args:
        maze: maze-olio, sisältää tiedon labyrintistä
        suunta: nykyinen etenemissuunta
        nykyruutu: nykyinen ruutu

    Returns:
        Bool: True, jos ei ole seinää, ja False, jos on seinä
    """

    if suunta == "N":
        if maze.maze_map[nykyruutu]["N"] == True:
            return True

    elif suunta == "E":
        if maze.maze_map[nykyruutu]["E"] == True:
            return True

    elif suunta == "S":
        if maze.maze_map[nykyruutu]["S"] == True:
            return True

    elif suunta == "W":
        if maze.maze_map[nykyruutu]["W"] == True:
            return True

    return False

def kaanny_vasemmalle(suunta):
    """Methodi muuttaa etenemissuunnan nykyisestä vasemmalle

    Args:
        suunta: nykyinen etenemissuunta

    Returns:
        suunta: uusi etenemissuunta
    """

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
    """Methodi kääntää etenemissuunnan ympäri

    Args:
        suunta: nykyinen etenemissuunta

    Returns:
        suunta: uusi etenemissuunta
    """

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
    """Methodi liikuttaa nykyistä ruutua yhden ruudun eteenpäin

    Args:
        suunta: nykyinen etenemissuunta
        nykyruutu: nykyinen ruutu

    Returns:
        nykyruutu: uusi ruutu
    """

    if suunta == "W":
        nykyruutu = (nykyruutu[0],nykyruutu[1]-1)

    elif suunta == "N":
        nykyruutu = (nykyruutu[0]-1,nykyruutu[1])

    elif suunta == "E":
        nykyruutu = (nykyruutu[0],nykyruutu[1]+1)

    elif suunta == "S":
        nykyruutu = (nykyruutu[0]+1,nykyruutu[1])

    return nykyruutu
