import csv

item_dictionary = {}

def read_creature_file(file_name, row_num_of_price):
    with open(file_name) as creatures_file:
        creature_reader = csv.reader(creatures_file, delimiter=',')
        for row in creature_reader:
            name = row[0].lower()
            price = row[row_num_of_price]
            item_dictionary[name] = price

def main():
    read_creature_file('sea_creatures.csv', 3)
    read_creature_file('fish.csv', 4)
    read_creature_file('bugs.csv', 1)
    read_creature_file('shells.csv', 1)

    item1 = input('First item: ')
    item2 = input('Second item: ')

    print("CORRECTION: " + correction(item1.lower()))

    cost1 = int(item_dictionary[item1.lower()])
    cost2 = int(item_dictionary[item2.lower()])

    capitalized_item1 = " ".join([word.capitalize() for word in item1.split(" ")])
    capitalized_item2 = " ".join([word.capitalize() for word in item2.split(" ")])

    print("-----------------------------")
    print("")
    print(capitalized_item1 + " costs " + str(cost1))
    print(capitalized_item2 + " costs " + str(cost2))

    if cost1 == cost2:
        print("They are the same price")
    elif cost1 > cost2:
        print("Therefore, you should keep the " + capitalized_item1)
    else:
        print("Therefore, you should keep the " + capitalized_item2)

    print("")
    print("-----------------------------")

if __name__ == "__main__":
    main()