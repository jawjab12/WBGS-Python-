from collections import namedtuple
#Imports the namedtuple bulit in function Pets
Pets= namedtuple('pets', 'animal name age') #defines the tuple Pets and the fields animal, name and age
Dottie=Pets(animal='cat', name='Dottie', age=9)
#Creates a new record
Jack=Pets(animal='cat', name='Jack', age= 9)
Lassie=Pets(animal='dog', name='Lassie', age = 13)
print(Dottie)
#prints the record print (Jack) print (Lassie)
