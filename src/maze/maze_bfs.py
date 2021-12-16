from collections import deque

def bfs(maze, aloitus = None):             # aloitus on aloitus ruutu, joka tässä tilanteessa vielä on (1,1)
    if aloitus is None:
        aloitus = (maze.rows, maze.cols)
    seuraavat = deque()                 # seuraavat sisältää tiedon pääseekö viereisiin ruutuihin
    seuraavat.append(aloitus)
    polku = {}                          # bfs kulkema polku
    tutkittu = [aloitus]

    while len(seuraavat)>0:
        nykyruutu=seuraavat.popleft()       # nykyruutu = nykyinen ruutu
        if nykyruutu==(1,1):
            break
        for d in "ESNW":
            if maze.maze_map[nykyruutu][d] is True:
                if d=="E":
                    lapsi = (nykyruutu[0], nykyruutu[1]+1)      # lapsi = ruudun lapsi, eli nykyisen ruudun viereinen ruutu
                elif d=="W":
                    lapsi = (nykyruutu[0], nykyruutu[1]-1)
                elif d=="S":
                    lapsi = (nykyruutu[0]+1, nykyruutu[1])
                elif d=="N":
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
