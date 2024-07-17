
import re

def preprocessing(text):
    return re.sub(r'\<@[A-Z0-9]*\>', ' ', text).strip()

