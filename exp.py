
import redis
import os

from mongo.mongo_helper import create_mongo_client


#make the mongo client 
client = create_mongo_client()

print(client)





# Define the databases and collections you want to search through
databases_and_collections = {
    'articles': ["projects","tech","life"],
    'section': ['section_data'],
    # Add more databases and collections as needed
}
"""
def search_mongodb(query):
    all_results = []
    # Regular expression to search for the query
    regex_query = {"$regex": query, "$options": "i"}  # "i" option for case-insensitive search
    
    # Iterate through each database and collection
    for db_name, collections in search_targets.items():
        db = client[db_name]
        for collection_name in collections:
            collection = db[collection_name]
            # Perform a regex search in each collection for the query in specific fields
            results = collection.find({
                "$or": [
                    {"article_name": regex_query}, 
                    {"aticle_data.title": regex_query},
                    {"aticle_data.article_para": regex_query},
                    {"aticle_data.markdown_data": regex_query},
                    {"card_one_text": regex_query},
                    {"card_two_text": regex_query},
                    {"card_three_text": regex_query}
                ]
            })
            
            # Process and append the results
            for result in results:
                result['_id'] = str(result['_id'])  # Convert ObjectId to string
                all_results.append(result)
    
    return all_results

# Example usage
if __name__ == '__main__':
    query = input("Enter search query: ")
    results = search_mongodb(query)
    
    # Print the results
    if results:
        print(f"Found {len(results)} result(s) for query '{query}':")
        for result in results:
            print(result)
    else:
        print(f"No results found for query '{query}'.")
"""

#this has to be run to create the index during bulk insertion
def create_indexes():
    for db_name, collections in databases_and_collections.items():
        db = client[db_name]
        for collection_name in collections:
            collection = db[collection_name]
            # Create a text index on multiple fields
            collection.create_index([
                ('article_name', 'text'),
                ('aticle_data.title', 'text'),
                ('aticle_data.article_para', 'text'),
                ('aticle_data.markdown_data', 'text'),
                ('card_one_text', 'text'),
                ('card_two_text', 'text'),
                ('card_three_text', 'text')
            ])

# Run index creation
#create_indexes()
#page usinng is search result

def search_mongodb(query):
    all_results = []
    regex_query = {"$regex": query, "$options": "i"}  # For regex search, if text search is not used

    for db_name, collections in databases_and_collections.items():
        db = client[db_name]
        for collection_name in collections:
            collection = db[collection_name]
            # Perform text search using the $text operator
            results = collection.find({
                "$text": {"$search": query}
            })
            
            # Process and append the results
            for result in results:
                result['_id'] = str(result['_id'])  # Convert ObjectId to string
                all_results.append(result)
    
    return all_results

# Example usage
if __name__ == '__main__':
    query = input("Enter search query: ")
    results = search_mongodb(query)
    
    # Print the results
    if results:
        print(f"Found {len(results)} result(s) for query '{query}':")
        for result in results:
            print(result)
    else:
        print(f"No results found for query '{query}'.")


