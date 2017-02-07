#Jason Chua and Chloe Delfau
#SoftDev2 pd8
#Work 1: hey MON, GO and get some data!
#2017-02-04 

#imports
from pymongo import MongoClient
import csv

#connect to the server and create a database
server = MongoClient('lisa.stuy.edu')
fluffyengine = server.fluffyengine

#deletes collection and all of its documents if it already exists
fluffyengine.collection.drop()

#opens the csv files and gets the csv reader iterator for each
#instantiate doc which will be a list of all the documents to be added to the collection
peeps = csv.reader(open("peeps.csv"))
courses = csv.reader(open("courses.csv"))
docs = []

#creates a document for each peep with all of their info (name, age, and id) from the peeps.csv file
#gives each document a 'courses' key which is an empty dictionary that will be filled up later
peeps.next()
for peep in peeps:
    doc = {}
    doc['name'] = peep[0]
    doc['age'] = peep[1]
    doc['id'] = peep[2]
    doc['courses'] = {}
    docs.append(doc)

#uses each peep's id to access their index in the docs list
#ex: kruder's id is 1 so docs[id - 1] will access kruder's doc
#adds course information to each document's courses dictionary where the course is the key and the mark is the value
courses.next()
for course in courses:
    doc = docs[int(course[2]) - 1]
    c = doc['courses']
    c[course[0]] = course[1]
