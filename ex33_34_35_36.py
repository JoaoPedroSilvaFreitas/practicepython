__author__ = 'joao'

import json
from bokeh.plotting import figure, show, output_file

##Não sei se está funcionando corretamente
def bokehGraph(birthdates):
    months = [{"id": 1, "month": "January", "births": 0},
    {"id": 2, "month": "February", "births": 0},
    {"id": 3, "month": "March", "births": 0},
    {"id": 4, "month": "April", "births": 0},
    {"id": 5, "month": "May", "births": 0},
    {"id": 6, "month": "June", "births": 0},
    {"id": 7, "month": "July", "births": 0},
    {"id": 8, "month": "August", "births": 0},
    {"id": 9, "month": "September", "births": 0},
    {"id": 10, "month": "October", "births": 0},
    {"id": 11, "month": "November", "births": 0},
    {"id": 12, "month": "December", "births": 0},]

    for i in birthdates:
        for j in months:
            if i.get("month") == j.get("id"): j["births"] += 1

    x_months = []
    y_births = []
    output_file("graph.html")
    for i in months:
        x_months.append(i.get("months"))
        y_births.append(i.get("births"))

    graph = figure()
    graph.vbar(x = x_months, top = y_births, width = 1)
    show(graph)

def writeJson(birthdates):
    with open("output/birthdates.json", "w") as open_file:
        json.dump(birthdates, open_file)

def readJson():
    with open("output/birthdates.json", "r") as open_file:
        return json.load(open_file)

def countSameMonthBirthday(birthdates):
    months = [{"id": 1, "month": "January", "births": 0},
    {"id": 2, "month": "February", "births": 0},
    {"id": 3, "month": "March", "births": 0},
    {"id": 4, "month": "April", "births": 0},
    {"id": 5, "month": "May", "births": 0},
    {"id": 6, "month": "June", "births": 0},
    {"id": 7, "month": "July", "births": 0},
    {"id": 8, "month": "August", "births": 0},
    {"id": 9, "month": "September", "births": 0},
    {"id": 10, "month": "October", "births": 0},
    {"id": 11, "month": "November", "births": 0},
    {"id": 12, "month": "December", "births": 0},]

    for i in birthdates:
        for j in months:
            if i.get("month") == j.get("id"): j["births"] += 1

    
    for i in months:
        if i.get("births") > 1: print(str(i.get("births")) + " people were born in " + i.get("month"))

def searchBirthdate(birthdates):
    name = input("Who's birthday do you want to look up? ")
    for i in birthdates:
        if i.get("name") == name:
            print(i.get("name") + " birthdate is in " + str(i.get("day")) + "/" + str(i.get("month")) + "/"+ str(i.get("year")))
            return
    print(name + " birthdate is not avaiable!")

def addNewBirthdate(birthdates):
    birthdate = { "name": "", "day": 0, "month": 0, "year": 0}
    birthdate.update({"name" : input("Name: ")})
    birthdate.update({"day" : int(input("Day: "))})
    birthdate.update({"month" : int(input("Month: "))})
    birthdate.update({"year" : int(input("Year: "))})
    birthdates.append(birthdate)
    writeJson(birthdates)

def printMenu(birthdates):
    print("--------------------------------------------------------------")
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    for i in birthdates:
        print(i.get("name"))
    print("1 - Search birthdate")
    print("2 - Add birthdate")
    print("3 - Search for same month birthday")
    print("4 - Create graph using bokeh library")
    print("0 - Exit")
    option = input("Select: ")
    return option

birthdates = readJson()
while True:
    option = printMenu(birthdates)
    if option == '1': searchBirthdate(birthdates)
    elif option == '2': addNewBirthdate(birthdates)
    elif option == '3': countSameMonthBirthday(birthdates)
    elif option == '4': bokehGraph(birthdates)
    elif option == '0': break
    else : print("Invalid option!")