from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.BookStoreDb

posts = db.Books
first = posts.find_one({'Name': 'Design Patterns'})
print(first)
