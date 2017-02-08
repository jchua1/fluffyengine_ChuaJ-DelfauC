#imports
from pymongo import MongoClient
import csv

#connect to the server and create a database
server = MongoClient('lisa.stuy.edu')
fluffyengine = server.fluffyengine

#deletes teacher collection and all of its documents if it already exists
fluffyengine.teachers.drop()

#opens the csv file and gets the csv reader
#instantiate doc which will be a list of all the documents to be added to the collection
teachers = csv.reader(open('teachers.csv'))
docs = []

#creates a document for each peep with all of their info (code, teacher, and period) from the teachers.csv file
#when appending to the student list, checks for course name in each peep document's course dictionary keys
teachers.next()
for teacher in teachers:
    doc = {}
    doc['code'] = teacher[0]
    doc['teacher'] = teacher[1]
    doc['period'] = teacher[2]
    doc['students'] = []
    for peep in fluffyengine.peeps.find():
        if doc['code'] in peep['courses']:
            doc['students'].append(peep['id'])
    docs.append(doc)

fluffyengine.teachers.insert_many(docs)

