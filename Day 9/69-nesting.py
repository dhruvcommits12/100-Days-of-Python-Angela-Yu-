# #Nested list in dictionary

# travel_log = {
#     "Germany":["Berlin","Hamburg","Stuttgart"],
#     "England":["Birmingham","Cardiff","Manchester"],

# }

# print(travel_log["Germany"][2])

nested_list = ["A","B",["C","D"]]
print(nested_list[2][1])

#Nested dict. in dict.

travel_log = {
    "Germany":{
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits" : 7,
    },
    "England":{
        "cities_visited":["Birmingham","Cardiff","Manchester"],
        "total_visits":12,

    }
}

print(travel_log["England"]["cities_visited"][2])
