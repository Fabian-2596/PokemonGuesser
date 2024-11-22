from urllib.request import urlopen
from bs4 import BeautifulSoup
from nicegui import ui
import random

pokemonList = []
pokemonImages = []
points = 0

url = "https://www.pokewiki.de/Pok%C3%A9mon-Liste"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

td = soup.find_all("td")
img = soup.find_all("img")
count = 3
imgcount = 0
size = len(td)
while (count < size):
    pokemonImages.append(img[imgcount]["src"])
    pokemonList.append(td[count].string)
    count += 9 
    imgcount += 1

@ui.refreshable
def newPokemon(img):
    siteurl = "https://www.pokewiki.de"
    index = random.randrange(len(img))
    imgurl = siteurl + pokemonImages[index]
    ui.label(points)
    ui.image(imgurl).style("width: 25%").style("height: 25%").style("")


newPokemon(img)
ui.button("next", on_click=newPokemon.refresh)
#ui.run()