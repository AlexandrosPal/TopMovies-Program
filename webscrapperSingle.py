from bs4 import BeautifulSoup
import requests
from mongo import insertMovie

HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}

# result = requests.get('https://www.imdb.com/title/tt0071562/?ref_=tt_sims_tt_i_1', headers=HEADERS) # Godfather 2
# result = requests.get('https://www.imdb.com/title/tt0110912/?ref_=tt_sims_tt_i_8', headers=HEADERS) # Pulp Fiction
# result = requests.get('https://www.imdb.com/title/tt0468569/?ref_=tt_sims_tt_i_3', headers=HEADERS) # Dark Knight
# result = requests.get('https://www.imdb.com/title/tt0108052/?ref_=tt_sims_tt_i_4', headers=HEADERS) # Sindler's List
# result = requests.get('https://www.imdb.com/title/tt0120382/?ref_=nv_sr_srsg_0_tt_7_nm_1_q_truman%2520sh', headers=HEADERS) # The Truman Show
# result = requests.get('https://www.imdb.com/title/tt0266543/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_finding%2520nemo', headers=HEADERS) # Finding Nemo
# result = requests.get('https://www.imdb.com/title/tt0109830/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=FHH2734QW8JCRVVP979H&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_11', headers=HEADERS) # Forrest Gump
result = requests.get('https://www.imdb.com/title/tt0364569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=1a264172-ae11-42e4-8ef7-7fed1973bb8f&pf_rd_r=FHH2734QW8JCRVVP979H&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_71', headers=HEADERS) # Oldboy

doc = BeautifulSoup(result.text, 'html.parser')

parent = doc.find("h1")
name = parent.string

parent = doc.find_all(string='/')
parent = parent[0].parent.parent
parent = parent.find("span")
rating = parent.string


parent = doc.find_all(class_='ipc-link ipc-link--baseAlt ipc-link--inherit-color')
year = parent[4].string

parent = doc.find_all(class_='ipc-inline-list__item')
length = []
for tag in parent:
    if tag.string != None:
        if 'h' in tag.string or 'm' in tag.string:
            length.append(tag.string)
length = length[0]

parent = doc.find_all(class_='ipc-chip-list__scroller')
categories = []
div = parent[0]
for a in div:
    span = a.find('span')
    categories.append(span.string)

parent = doc.find_all(class_='sc-5f699a2-0 kcphyk')
description = parent[0].contents[0]

parent = doc.find_all(class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
director = parent[0].string

parent = doc.find_all(class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt')
stars = []
parent = parent[2].find_all('li')
for a in parent:
    stars.append(a.string)

parent = doc.find_all(class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt')
writers = []
parent = parent[1].find_all('li')
for a in parent:
    writers.append(a.string)

# insertMovie(name, rating, year, length, categories, description, director, stars, writers)



print(name)
print(rating)
print(year)
print(length)
print(categories)
print(description)
print(director)
print(stars)
print(writers)