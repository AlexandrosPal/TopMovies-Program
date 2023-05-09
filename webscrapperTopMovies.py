from bs4 import BeautifulSoup
import requests
from mongo import insertMovie

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
result = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=HEADERS)
doc = BeautifulSoup(result.text, 'html.parser')


parent = doc.find_all('tbody', class_='lister-list')
parent = parent[0].find_all('tr')
for tr in parent:
    name = tr.find('td', class_='titleColumn')
    name =  name.find('a')
    link = name['href']
    result = requests.get(f"https://www.imdb.com/{link}", headers=HEADERS)
    doc = BeautifulSoup(result.text, 'html.parser')

    parentName = doc.find("h1")
    name = parentName.string

    parentRating = doc.find_all(string='/')
    parentRating = parentRating[0].parent.parent
    parentRating = parentRating.find("span")
    rating = parentRating.string


    parentYear = doc.find_all(class_='ipc-link ipc-link--baseAlt ipc-link--inherit-color')
    year = parentYear[4].string

    parentLength = doc.find_all(class_='ipc-inline-list__item')
    length = []
    for tag in parentLength:
        if tag.string != None:
            if 'h' in tag.string or 'm' in tag.string:
                length.append(tag.string)
    length = length[0]

    parentCats = doc.find_all(class_='ipc-chip-list__scroller')
    categories = []
    div = parentCats[0]
    for a in div:
        span = a.find('span')
        categories.append(span.string)

    parentDesc = doc.find_all(class_='sc-5f699a2-0 kcphyk')
    description = parentDesc[0].contents[0]

    parentDir = doc.find_all(class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
    director = parentDir[0].string

    parentStars = doc.find_all(class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt')
    stars = []
    parentStars = parentStars[2].find_all('li')
    for a in parentStars:
        stars.append(a.string)

    parentWriters = doc.find_all(class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt')
    writers = []
    parentWriters = parentWriters[1].find_all('li')
    for a in parentWriters:
        writers.append(a.string)

    insertMovie(name, rating, year, length, categories, description, director, stars, writers)



# print(name)
# print(rating)
# print(year)
# print(length)
# print(categories)
# print(description)
# print(director)
# print(stars)
# print(writers)