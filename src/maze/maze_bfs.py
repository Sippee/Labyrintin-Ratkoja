"""bfs algoritmi
"""

from collections import deque

def bfs(maze, aloitus = None):
    """bfs algoritmin runko

    Args:
        maze: maze-olio, sisältää tiedon labyrintistä
        aloitus: optional, oletuksena aloitusruutu on labyrintin oikeassa alakulmassa

    Returns:
        seurvaavatpolku: bfs algoritmin kulkema polku
    """

    if aloitus is None:
        aloitus = (maze.rows, maze.cols)
    seuraavat = deque()      # seuraavat sisältää tiedon pääseekö viereisiin ruutuihin
    seuraavat.append(aloitus)
    polku = {}
    tutkittu = [aloitus]

    while len(seuraavat)>0:
        nykyruutu=seuraavat.popleft()
        if nykyruutu==(1,1):
            break
        for direction in "ESNW":
            if maze.maze_map[nykyruutu][direction] == True:
                if direction=="E":
                    lapsi = (nykyruutu[0], nykyruutu[1]+1)
                elif direction=="W":
                    lapsi = (nykyruutu[0], nykyruutu[1]-1)
                elif direction=="S":
                    lapsi = (nykyruutu[0]+1, nykyruutu[1])
                elif direction=="N":
                    lapsi = (nykyruutu[0]-1, nykyruutu[1])
                if lapsi in tutkittu:
                    continue

                tutkittu.append(lapsi)
                seuraavat.append(lapsi)
                polku[lapsi]=nykyruutu

    seuraavatpolku={}
    ruutu=(1,1)
    while ruutu!=aloitus:
        seuraavatpolku[polku[ruutu]]=ruutu
        ruutu=polku[ruutu]

    return seuraavatpolku
