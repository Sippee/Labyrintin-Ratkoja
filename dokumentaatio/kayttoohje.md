# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/Sippee/Labyrintin-Ratkoja/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Ohjelman käynnistämisen jälkee
- Ohjelma antaa ohjeet, mihin toimintoihin pääsee milläkin käskyllä
- Ensimmäinen ohje "Save a new maze" on toimintoa varten, jonka avulla tallennetaan uusi labyrintti koneelle
- Toinen ohje toimintoihin "Timed 200x200 Mazes", nämä ottavat vain ajan kauan algoritmillä kesti selvittää reitti 200x200 kokoisessa labyrintissä
- Viimeinen ohje toimintoihin "Visual 10x10 Mazes", nämä luovat visuaalisen esityksen labyrintin ratkaisemisesta

## Huomautukset
- Tällä hetkellä ei voi käyttää ensin algoritmin ajastus toimintoa ja sitten visuaalista esitystä.  
  - Sovellus pitää käynnistää näiden välillä uudelleen, mutta ajastus toimintoja ja visuaalisia esityksiä voi keskenään käyttää vapaasti.  
- Visuaalisten esitysten kuuluu päästä maaliin ennen kuin ikkunan voi sammuttaa, muuten saa virheilmoituksen
