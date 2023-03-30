import requests
from bs4 import BeautifulSoup
import pprint
from inflection import titleize

#MI PRIMERA SOLUCIÓN
# #ponemos la web que queremos scrapear
r = requests.get('http://www.dailysmarty.com/topics/python') 
html = r.text
# # print(html) #nos muestra el html de la web a escrapear
# # status = r.status_code
# # print(html,status) #nos muestra el estado de la web. 200 = ok

soup = BeautifulSoup(html, 'html.parser')


for link in soup.find_all('a', {'data-turbolinks': 'false'}):
    pprint.pprint(link.get('href').replace('/posts/', '').replace('-', ' ').title())


#SOLUCIÓN DEFINITIVA
def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'post' in url:
            url = url.split('/')[-1] #nos divide el string en partes a partir de /. Como indicamos el índice -1, nos quedamos con la última parte del string.
            url = url.replace('-',' ') #reemplazamos '-' por un hueco en blanco
            url = titleize(url) #ponemos todos los strings como si fueran títulos (mayúsculas)
            titles.append(url) #añadimos los títulos a la variabele url

    for link in links:
        if link.get('href') == None: 
            continue
        else:
            post_formatter(link.get('href'))

    return titles


r =requests.get('http://www.dailysmarty.com/topics/python') 
soup = soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('a')
titles = title_generator(links)

for title in titles:    
    print(title)
    










