stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverley")
print(stops)
#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0,"Glasgow Queen")
print(stops)
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4,"Polmont")
print(stops)
#4. Print out the index position of "Linlithgow"
index = stops.index('Linlithgow')
print(index)
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
print(stops)
#6. Delete "Cumbernauld" from the list by index
del stops[2]
print(stops)
#7. Print the number of stops there are in the list
stops = ["Glasgow Queen", "Croy", "Falkirk High", "Polmont", "Linlithgow", "Haymarket", "Edinburgh Waverley"]
num_stops = len(stops) 
print(len(stops))
#8. Sort the list alphabetically
stops.sort()
print(stops)
#9. Reverse the positions of the stops in the list
stops.reverse()
print(stops)
#10 Print out all the stops using a for loop
stops = ["Polmont", "Linlithgow", "Haymarket", "Glasgow Queen", "Falkirk High", "Edinburgh Waverley", 'Croy']
[print(x) for x in stops]


