def consonant(string):


    consonant = [i for i in string if i not in "aeiouAEIOU "]
    print(consonant)

string = "Python Programing"


consonant(string)
