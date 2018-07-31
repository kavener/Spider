import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test

collection = db.students

student1 = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

student2 = {
    'id': '20170102',
    'name': 'Mary',
    'age': 21,
    'gender': 'female'
}

# result = collection.insert_one(student2)
# print(result)

reslut = collection.find_one({'name': 'Jordan'})
print(reslut)

count = collection.find().count()
print(count)