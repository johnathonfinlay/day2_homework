stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]
stops.append("Edinburgh Waverley")
# 1
print(stops)
# 2
stops.insert(0,"Glasgow Queen Street")
print(stops)
# 3
stops.insert(4,"Polmont")
print(stops)
# 4
index = stops.index("Linlithgow")
print(index)
# 5
stops.remove("Livingston")
print(stops)
# 6
del stops[2]
print(stops)
# 7
print(len(stops))
# 8
stops.sort()
print(stops)
# 9
stops.reverse()
print(stops)
# 10
for stop in stops:
    print(stop)