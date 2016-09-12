persons = [
    {'city': 'Kiev', 'name': 'Andrey'},
    {'city': 'Roma', 'name': 'Marcus'}
]
romans = list(filter(lambda x: x['city'] == 'Roma', persons))
print(romans)