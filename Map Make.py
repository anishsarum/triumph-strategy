def makeMap(width, height):
    Map = []
    for i in range(height):
        Map.append([])
        types = input("Row Types: ")
        for j in range(width):
            Map[i].append(details[types[j].upper()])
    return Map

details = {"G":[0, 0, "grass"], "S":[0, 0, "desert"], "M":[0, 0, "snow"],\
           "F":[0, 0, "forest"]}

print(makeMap(15, 15))

            
