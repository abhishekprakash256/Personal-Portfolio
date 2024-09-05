
import redis
import os

from mongo.mongo_helper import create_mongo_client


#make the mongo client 
client = create_mongo_client()

print(client)





# Define the databases and collections you want to search through
search_targets = {
    'articles': ["projects","tech","life"],
    'section': ['section_data'],
    # Add more databases and collections as needed
}

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

