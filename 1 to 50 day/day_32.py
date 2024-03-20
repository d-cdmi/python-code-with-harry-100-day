# Union
# s1={1,5,2,4,3}
# s2={3,5,4,2,9}
# print(s1.union(s2))   #no change for s1
# print(s1)
# s1.update(s2)     #update function User s1 update
# print(s1)


#intersection
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# # cities.update(cities2)
# print(cities.intersection(cities2))

# symmetric difference
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# print(cities.symmetric_difference(cities2))

# difference() and difference_update():
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}        
# cities2 = {"Seoul", "Kabul", "Delhi"}
# cities3 = cities.difference(cities2)
# print(cities3)                                  #A-b


#isdisjoint()   jo same hay to false and same no hoy  Ture
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}        
# cities2 = {"Seoul", "Kabul", "Deflhi"}
# print(cities.isdisjoint(cities2))

# issubset()   
# cities = {"Tokyo", "Kabul", "Berlin"}        
# cities2 = {"Tokyo", "Kabul", "Berlin"}
# # print(cities.issuperset(cities2))
# print(cities.issubset(cities2))


#add
# cities = {"Tokyo", "Kabul", "Berlin"}        
# cities.add("dhruvish")
# print(cities)

#remove-->>no hoy to error  discard----> no hoy to not error
# cities = {"Tokyo", "Kabul", "Berlin"}        
# cities.discard("Tokyo2")
# print(cities)

#pop
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}        
# item=cities.pop()
# print(item)

#del  deletal all item
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}        
# item=cities.pop()
# del cities
# print(cities)

#clear  remove the item
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}        
# print(cities.clear())
# cities.add("dhruvish")
# print(cities)



#if condition ma pan use thay chhe 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}        

if "Tokydo" in cities:
    print("yes")
else:
    print("No")