def printscores(**scores):
    for k, v in scores.items():
        print (f'Subject {k:>10}: {v:>10}')

kwargs = { 'Math': 90,  'English': 100,  'Computer': 90}
printscores(**kwargs)