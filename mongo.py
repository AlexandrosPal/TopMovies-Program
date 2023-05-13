from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient
from mongo_validator import movies_validator
load_dotenv(find_dotenv())

password = os.environ.get('MONGO_PWD')

connection_string = f'mongodb+srv://admin:{password}@main.oukdars.mongodb.net/'
client = MongoClient(connection_string)
dbs = client.list_database_names()
moviesDB = client.MoviesDB
moviesApp = moviesDB.moviesApp


def createCollection():
    moviesDB.create_collection("moviesApp")
    moviesDB.command("collMod", "moviesApp", validator=movies_validator)

def insertMovie(name, rating, year, length, categories, description, director, stars, writers):
    try:
        doc = {'name': name,
           'rating': float(rating),
           'year': int(year),
           'length': length,
           'categories': categories,
           'description': description,
           'director': director,
           'stars': stars,
           'writers': writers
        }
        moviesApp.insert_one(doc)
    except Exception as e:
        print(e)

def viewAllMovies():
    movies = moviesApp.find()
    for index, movie in enumerate(movies):
        print(f"[{index+1}] Name: {movie['name']}  -  Rating: {movie['rating']}/10")

def getByRating(min, max):
    query = {'rating': {'$gte': float(min), '$lte': float(max)}}
    movies = moviesApp.find(query)
    return movies

def getByName(name):
    query = {'name': {'$regex': name, "$options": "i"}}
    movies = moviesApp.find(query)
    return movies

def countMovies():
    count = moviesApp.count_documents(filter={})
    print(f"There are {count} movies in the database.")

def addNewField(fieldName, value):
    query = {}
    newValue = {"$set": {f"{fieldName}": f"{value}"}}
    moviesApp.update_many(query, newValue)

def updateField(name, fieldName, value):
    query = {"name": name}
    newValue = {"$set": {f"{fieldName}": f"{value}"}}
    moviesApp.update_one(query, newValue)

def getSaved():
    query = {'savedState': 'saved'}
    movies = moviesApp.find(query)
    
    return movies

def filterSavedByName(name):
    query = {'savedState': 'saved', 'name': {'$regex': name, "$options": "i"}}
    movies = moviesApp.find(query)
    return movies

def getAllCategories():
    categories = []
    movies = moviesApp.find()
    for movie in movies:
        for category in movie['categories']:
            if category not in categories:
                categories.append(category)
    
    return categories

def getByRatingAndCategory(min, max, category):
    if category == ' ':
        query = {'rating': {'$gte': float(min), '$lte': float(max)}}
    else:
        query = {'rating': {'$gte': float(min), '$lte': float(max)}, 'categories': category}
    movies = moviesApp.find(query)
    return movies


# getAllCategories()
# createCollection()
# insertMovie(name, rating, year, length, categories, description, director, stars, writers)
# viewAllMovies()
# getByRating(8, 10)
# getByName('Pulp')
# countMovies()
# addNewField("userRating", 0)