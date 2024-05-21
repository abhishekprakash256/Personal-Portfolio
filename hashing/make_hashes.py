"""
The file to make hashes for the url and that hashes will be use for the url storage in redis hahes

"""

import random

def generate_random_hash():
    """
    The function to generates a random hash of the given length.
    """

    random_length = random.randint(5, 10)
    hash = ""
    for i in range(random_length):
        hash += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    return hash

