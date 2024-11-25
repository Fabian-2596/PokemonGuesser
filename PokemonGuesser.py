from urllib.request import urlopen
from bs4 import BeautifulSoup
from nicegui import ui
import random

pokemonList = []
points = 0
input = ""
currentPokemon = ""


url = "https://www.pokewiki.de/Pok%C3%A9mon-Liste"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

td = soup.find_all("td")
count = 2
size = len(td)
while (count < size):
    pokemonList.append(td[count].string)
    count += 9

@ui.refreshable
def newPokemon():
    index = random.randrange(len(pokemonList))
    global currentPokemon
    currentPokemon = pokemonList[index]
    print(currentPokemon)
    url = "https://www.pokewiki.de/" + currentPokemon
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find_all('td', attrs={'colspan': "2"})
    for x in table:
        ref = x.find('a', class_="mw-file-description")
        if(ref != None):
            break

    image_tag = ref.find('img')
    imagelink = "https://www.pokewiki.de/" + image_tag["src"]
    ui.label(points)
    ui.image(imagelink).style("width: 25%").style("height: 25%").style("")

def checkAnswer():
    global points
    if(textInput.value.lower() == currentPokemon.lower()):
        points += 1
    newPokemon.refresh()

newPokemon()
textInput = ui.input(label="Welches Pokemon ist das?")
ui.button("Rate!", on_click=checkAnswer)
ui.run()