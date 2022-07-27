people=[
    {"name":"harry","house":"Gryffindor"},
    {"name":"cho","house":"ravenclaw"},
    {"name":"draco","house":"slytherin"},
]


people.sort(key=lambda person:person["name"])

print(people)