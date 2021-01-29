"""
Name: state_and_flower.py
Author: Patrick Walsh
Date: 1/29/2021
Purpose: Program that lets user search database of information
about U.S. states, their capitals, population, and state flower.
Uses matplotlib to show graphs and images.

Comment: Run following command to generate pylintrc file in directory
where pylint command is being run:
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc
"""

import matplotlib.pyplot as plt

# tuple of state abbreviations
# make tuple so that values cannot be altered accidentally
state_iter = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")

# Format of state_pop (alterable) dictionary:
# "KEY" (state name, str) : VALUE (float)
# user can update population values for a given state.
# STATE_DATA dictionary draws from state_pop dictionary for population data.
state_pop = {"AL": 4887680,
             "AK": 735139,
             "AZ": 7158020,
             "AR": 3009730,
             "CA": 39461600,
             "CO": 5691290,
             "CT": 3571520,
             "DE": 965479,
             "FL": 21244300,
             "GA": 10511100,
             "HI": 1420590,
             "ID": 1750540,
             "IL": 12723100,
             "IN": 6695500,
             "IA": 3148620,
             "KS": 2911360,
             "KY": 4461150,
             "LA": 4659690,
             "ME": 1339060,
             "MD": 6035800,
             "MA": 6882640,
             "MI": 9984070,
             "MN": 5606250,
             "MS": 2981020,
             "MO": 6121620,
             "MT": 1060660,
             "NE": 1925610,
             "NV": 3027340,
             "NH": 1353460,
             "NJ": 8886020,
             "NM": 2092740,
             "NY": 19530400,
             "NC": 10381600,
             "ND": 758080,
             "OH": 11676300,
             "OK": 3940240,
             "OR": 4181890,
             "PA": 12800900,
             "RI": 1058290,
             "SC": 5084160,
             "SD": 878698,
             "TN": 6771630,
             "TX": 28628700,
             "UT": 3153550,
             "VT": 624358,
             "VA": 8501290,
             "WA": 7523870,
             "WV": 1804290,
             "WI": 5807410,
             "WY": 577601}

# Format of STATE_DATA (constant) dictionary:
# "KEY" (state abbreviation, str) : VALUE (list) ["State name" (str), "Capital" (str),
# state_pop["KEY"] (dict), "flower" (str), "flower image path" (str)]
STATE_DATA = {"AL": ["Alabama", "Montgomery", state_pop["AL"], "Camellia", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/camellia-flower.jpg"],
              "AK": ["Alaska", "Juneau", state_pop["AK"], "Forget Me Not", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/Alpineforgetmenot.jpg"],
              "AZ": ["Arizona", "Phoenix", state_pop["AZ"], "Saguaro Cactus Blossom", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/saguaroflowersFlickr.jpg"],
              "AR": ["Arkansas", "Little Rock", state_pop["AR"], "Apple Blossom", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/AppletreeblossomArkansasflower.JPG"],
              "CA": ["California", "Sacramento", state_pop["CA"], "California Poppy", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/CAflowerCaliforniaPoppy.jpg"],
              "CO": ["Colorado", "Denver", state_pop["CO"], "White and Lavender Columbine", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/Colorado_columbine2.jpg"],
              "CT": ["Connecticut", "Hartford", state_pop["CT"], "Mountain Laurel", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/Mountain-Laural-flowers2.jpg"],
              "DE": ["Delaware", "Dover", state_pop["DE"], "Peach Blossom", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/peachblossomspeachflowers.jpg"],
              "FL": ["Florida", "Tallahassee", state_pop["FL"], "Orange Blossom", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/OrangeBlossomsFloridaFlower.jpg"],
              "GA": ["Georgia", "Atlanta", state_pop["GA"], "Cherokee Rose", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/CherokeeRoseFlower.jpg"],
              "HI": ["Hawaii", "Honolulu", state_pop["HI"], "Hibiscus", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/yellowhibiscusPuaAloalo.jpg"],
              "ID": ["Idaho", "Boise", state_pop["ID"], "Syringa", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/syringaPhiladelphuslewisiiflower.jpg"],
              "IL": ["Illinois", "Springfield", state_pop["IL"], "Purple Violet", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/singlebluevioletflower.jpg"],
              "IN": ["Indiana", "Indianapolis", state_pop["IN"], "Peony", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/PeonyPaeoniaflowers.jpg"],
              "IA": ["Iowa", "Des Moines", state_pop["IA"], "Wild Prairie Rose", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/WildPrairieRose.jpg"],
              "KS": ["Kansas", "Topeka", state_pop["KS"], "Sunflower", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/native-sunflowers.jpg"],
              "KY": ["Kentucky", "Frankfort", state_pop["KY"], "Goldenrod", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/stateflowergoldenrod-bloom.jpg"],
              "LA": ["Louisiana", "Baton Rouge", state_pop["LA"], "Magnolia", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/MagnoliagrandifloraMagnoliaflower.jpg"],
              "ME": ["Maine", "Augusta", state_pop["ME"], "White Pine Cone and Tassel", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/whitepinemalecones.jpg"],
              "MD": ["Maryland", "Annapolis", state_pop["MD"], "Black-Eyed Susan", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/FlowerMDBlack-eyedSusan.jpg"],
              "MA": ["Massachusetts", "Boston", state_pop["MA"], "Mayflower", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/MayflowerTrailingArbutus.jpg"],
              "MI": ["Michigan", "Lansing", state_pop["MI"], "Apple Blossom", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/appleblossombeauty.jpg"],
              "MN": ["Minnesota", "Saint Paul", state_pop["MN"], "Pink and White Lady Slipper", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/pinkwhiteladysslipperflower1.jpg"],
              "MS": ["Mississippi", "Jackson", state_pop["MS"], "Magnolia", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/magnoliablossomflower01.jpg"],
              "MO": ["Missouri", "Jefferson City", state_pop["MO"], "White Hawthorn Blossom", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/hawthornflowersblossoms1.jpg"],
              "MT": ["Montana", "Helena", state_pop["MT"], "Bitterroot", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/bitterrootfloweremblem.jpg"],
              "NE": ["Nebraska", "Lincoln", state_pop["NE"], "Goldenrod", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/goldenrodflowersyellow4.jpg"],
              "NV": ["Nevada", "Carson City", state_pop["NV"], "Sagebrush", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/Nevada-Sagebrush-Artemisia-tridentata.jpg"],
              "NH": ["New Hampshire", "Concord", state_pop["NH"], "Purple Lilac", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/lilacflowerspurplelilac.jpg"],
              "NJ": ["New Jersey", "Trenton", state_pop["NJ"], "Violet", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/wood-violet.jpg"],
              "NM": ["New Mexico", "Santa Fe", state_pop["NM"], "Yucca Flower", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/YuccaFlowersclose.jpg"],
              "NY": ["New York", "Albany", state_pop["NY"], "Rose", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/redrosebeautystateflowerNY.jpg"],
              "NC": ["North Carolina", "Raleigh", state_pop["NC"], "Dogwood", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/floweringdogwoodflowers2.jpg"],
              "ND": ["North Dakota", "Bismarck", state_pop["ND"], "Wild Prairie Rose", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/flowerwildprairierose.jpg"],
              "OH": ["Ohio", "Columbus", state_pop["OH"], "Scarlet Carnation", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/redcarnationOhioflower.jpg"],
              "OK": ["Oklahoma", "Oklahoma City", state_pop["OK"], "Mistletoe", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/mistletoe_phoradendron_serotinum.jpg"],
              "OR": ["Oregon", "Salem", state_pop["OR"], "Oregon Grape", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/Oregongrapeflowers2.jpg"],
              "PA": ["Pennsylvania", "Harrisburg", state_pop["PA"], "Mountain Laurel", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/Mt_Laurel_Kalmia_Latifolia.jpg"],
              "RI": ["Rhode Island", "Providence", state_pop["RI"], "Violet", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/violetsflowers.jpg"],
              "SC": ["South Carolina", "Columbia", state_pop["SC"], "Yellow Jessamine", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/CarolinaYellowJessamine101.jpg"],
              "SD": ["South Dakota", "Pierre", state_pop["SD"], "Pasque Flower", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/Pasqueflower-03.jpg"],
              "TN": ["Tennessee", "Nashville", state_pop["TN"], "Iris", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/purpleirisflower.jpg"],
              "TX": ["Texas", "Austin", state_pop["TX"], "Bluebonnet", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/BluebonnetsBlueRed.jpg"],
              "UT": ["Utah", "Salt Lake City", state_pop["UT"], "Sego Lily", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/SegoLily.jpg"],
              "VT": ["Vermont", "Montpelier", state_pop["VT"], "Red Clover", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/redcloverstateflowerWV.jpg"],
              "VA": ["Virginia", "Richmond", state_pop["VA"], "Dogwood", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/floweringDogwoodSpring.jpg"],
              "WA": ["Washington", "Olympia", state_pop["WA"], "Pink Rhododendron", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/flower_rhododendronWeb.jpg"],
              "WV": ["West Virginia", "Charleston", state_pop["WV"], "Rhododendron", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/rhododendronWVstateflower.jpg"],
              "WI": ["Wisconsin", "Madison", state_pop["WI"], "Wood Violet", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/wood-violet.jpg"],
              "WY": ["Wyoming", "Cheyenne", state_pop["WY"], "Indian Paintbrush", "https://statesymbolsusa.org/sites/statesymbolsusa.org/files/primary-images/indianpaintbrushWYflower.jpg"]}


def pop_normalize(tuple_states):
    """
    Population normalizer function
    Function takes state population and adds commas to make value more readable.
    For example, normalizes: 9456132 to 9,456,132
    Can normalize numbers up to 21 digits long
    """
    population = str(tuple_states)

    # insert commas iteratively, starting with numbers greater than 3 digits
    if len(population) > 3:
        population = population[:-3] + "," + population[-3:]
    if len(population) > 6:
        population = population[:-7] + "," + population[-7:]
    if len(population) > 9:
        population = population[:-11] + "," + population[-11:]
    if len(population) > 12:
        population = population[:-15] + "," + population[-15:]
    if len(population) > 15:
        population = population[:-19] + "," + population[-19:]
    if len(population) > 18:
        population = population[:-23] + "," + population[-23:]
    # trim off leading commas
    if population[0] == ",":
        population = population[1:]
        if population[0] == ",":
            population = population[1:]
    return population


def top_five(tuple_states):
    """
    Top 5 population finder function
    Function finds the 5 states with the highest population
    and puts them in a list
    """
    list_top_five = []
    names_top_five = []
    # create list of all populations
    for state in tuple_states:
        list_top_five.append(STATE_DATA[state][2])
    list_top_five.sort()  # sort list
    list_top_five.reverse()  # sort from highest to lowest
    # use only 5 highest values
    count = 45
    while count > 0:
        list_top_five.pop()
        count -= 1

    temp_state_iter = []
    for state in tuple_states:
        temp_state_iter.append(state)

    # get names of the top 5 states
    count = 0
    while count < 5:
        for temp_state in temp_state_iter:
            if STATE_DATA[temp_state][2] == list_top_five[count]:
                names_top_five.insert(count, temp_state)
                temp_state_iter.remove(temp_state)
                count += 1
                if count == 5:
                    break
    return list_top_five, names_top_five


print("**************************************")
print("WELCOME TO U.S. STATE INFO DATABASE")
print("**************************************")

running = True  # flag variable
while running:
    print("CHOOSE FROM THE FOLLOWING OPTIONS: \n(enter number choice)\n")
    print("1. Display all U.S. States in alphabetical order along with the capital, population, and state flower\n2. "
          "Search for a specific state and display associated data along with photo of state flower\n3. Provide bar "
          "graph of top 5 populated states along with their populations\n4. Update population data for specific U.S. "
          "state\n5. Exit")
    main_menu = input(">>> ")

    # display all states
    if main_menu == "1":
        # iterate through STATE_DATA dictionary
        # print(STATE_DATA)
        for i in state_iter:
            print("\nState:", STATE_DATA[i][0],
                  "\nCapital:", STATE_DATA[i][1],
                  "\nPopulation:", pop_normalize(STATE_DATA[i][2]),
                  "\nState flower:", STATE_DATA[i][3])
        print("\n\n")
    # search for state
    elif main_menu == "2":
        while True:
            try:
                print("\nPlease enter a two-letter state abbreviation (i.e., MD for Maryland)")
                search_state = input(">>> ").upper()
                url = STATE_DATA[search_state][4]  # get URL of state flower image
                img = plt.imread(url, format='jpg')  # read as jpg
                plt.imshow(img)
                plt.suptitle(STATE_DATA[search_state][0] + " state flower: " + STATE_DATA[search_state][3] + "\nCapital: " + STATE_DATA[search_state][1] + "     Population: " + pop_normalize(STATE_DATA[search_state][2]))
                plt.axis("off")  # hide axes
                plt.show()
                break
            except KeyError as err:
                print("\nInvalid key!")
                print("Error code:", err)
        print("\n" * 40)

    elif main_menu == "3":
        bar_labels = top_five(state_iter)[1]
        bar_values = top_five(state_iter)[0]
        # create bar chart
        plt.bar(bar_labels, bar_values)
        plt.suptitle("Most Populated States")
        plt.ylabel("Population of States")  # text along y axis
        plt.text(x=-0.4, y=bar_values[0] / 2, s=bar_values[0])  # text labels (x=coord, y=coord, s="string")
        plt.text(x=0.6, y=bar_values[1] / 2, s=bar_values[1])
        plt.text(x=1.6, y=bar_values[2] / 2, s=bar_values[2])
        plt.text(x=2.6, y=bar_values[3] / 2, s=bar_values[3])
        plt.text(x=3.6, y=bar_values[4] / 2, s=bar_values[4])
        plt.yticks([])  # clear ytick values
        plt.show()  # show plot
        print("\n" * 40)

    # update population
    elif main_menu == "4":
        while True:
            try:
                print("\nPlease enter a two-letter state abbreviation (i.e., MD for Maryland)")
                update_state = input(">>> ").upper()
                print(STATE_DATA[update_state][0])
                print("Population: " + pop_normalize(STATE_DATA[update_state][2]))

                print("\nWhat is the new population?")
                new_pop = int(input(">>> "))
                state_pop[update_state] = new_pop
                STATE_DATA[update_state][2] = state_pop[update_state]

                print(STATE_DATA[update_state][0])
                print("Population (adjusted): " + pop_normalize(STATE_DATA[update_state][2]))
                print("\n")
                break
            except KeyError as err:
                print("\nInvalid key!")
                print("Error code:", err)
            except ValueError as err:
                print("\nInvalid input!")
                print("Error code:", err)
        print("\n" * 40)

    # exit
    elif main_menu == "5":
        running = False
        print("\n\nTHANK YOU FOR USING THE U.S. STATE INFO DATABASE!!")
    # invalid input
    else:
        print("\nInvalid input!\n\n")
