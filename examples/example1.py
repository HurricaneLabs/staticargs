#let's get this party started
from staticargs import staticargs
import random

@staticargs
def append_cat(cats=[]):
    #I love cats
    cats.append("cat")
    return cats

print(append_cat())
print(append_cat())
print(append_cat())

@staticargs
def store_dog(dogs={}):
    #Dogs are OK I guess
    dog_name = random.choice(["rufus", "muffins", "scooby"])
    dogs[dog_name] = "good boy"
    return dogs

print(store_dog())
print(store_dog())
print(store_dog())
