from pymongo import MongoClient
    client = MongoClient()
    #client = MongoClient('localhost', 27017) # Default connection params
    # client = MongoClient('mongodb://localhost:27017') # Mongourl style
    
    # Get database
    db = client.test_database

    # Access collection
    collection = db.test_collection
    # collection = db['test-collection']

    # Insert document
    post = {
        "author": "Mike",
        "text": "My first blog post!"
    }
    db.posts.insert_one(postdict)

    # Find one query with simple filter
    db.posts.find_one({"author": "Mike"})
    # Find by id
    db.posts.find_one({"_id": post_id}) 

    # Count
    db.posts.count_documents()
    # Count with filter
    db.posts.count_documents({"author": "Mike"})

    # Filter and sort (example with $lt less-than operator)
    d = datetime.datetime(2009, 11, 12, 12)
    db.posts.find({"date": {"$lt": d}}).sort("author")