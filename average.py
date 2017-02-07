#Jason Chua and Chloe Delfau
#SoftDev2 pd8
#Work 2: You Boys Like Mexico?
#2017-02-06

#imports
from pymongo import MongoClient

#connect to the server and create a database
server = MongoClient('lisa.stuy.edu')
fluffyengine = server.fluffyengine

#converts each item in the courses.values() list to int and then returns average of grades in the list
def average(courses):
    grades = map(int, courses.values())
    return sum(grades) / float(len(grades))

#iterates through collection documents and prints id, name, and average for each    
for peep in fluffyengine.collection.find():
    print peep['id'], peep['name'], average(peep['courses'])
