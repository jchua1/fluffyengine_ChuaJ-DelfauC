#Jason Chua and Chloe Delfau
#SoftDev2 pd8
#Work 1: hey MON, GO and get some data!
#2017-02-04 

#imports 
from pymongo import MongoClient
import csv

#connect to the server and create a data base
server = MongoClient('149.89.150.100')
db = server.mydb
c = db.students

#open the csv files and put all of the data into a dictionary
courses = open("courses.csv","r")
peeps = open("peeps.csv","r")
dict = {}


