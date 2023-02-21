import uuid

def get_random_word():
    word = str(uuid.uuid4())[:8].replace('-', '').lower()
    return word