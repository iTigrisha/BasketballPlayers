#!

"""
Создайте программу, хранящую информацию о великих баскетболистах.
Нужно хранить имя, фамилию, год рождения и рост (в сантиметрах) баскетболиста.
Требуется реализовать возможность добавления, удаления, поиска.
Используйте словарь для хранения данных баскетболиста.
"""

import pprint
import operator

list_of_dicts_basketball_players = []
keys = ["name", "surname", "year of birth", "height"]


# b. написать функцию которая считывает из файла всех баскетболистов,
def famous_basketball_players():
    with open(file="famous_basketball_players.csv", mode="r") as file:
        for line in file:
            player_list = line.split(",")
            player_list[-1] = player_list[-1][:3]
            players_with_keys = dict(zip(keys, player_list))
            list_of_dicts_basketball_players.append(players_with_keys)


# c. Написать функцию которая “красиво“ выводит на экран данные одного баскетболиста
# с.1 узнаем информацию о каком баскетболисте вывести информацию ( для функции аbout_person_you_want_to_know() )
def who_you_want():
    names = []
    print("\nSo, we have the following persons as a famous backetball players:")
    for i in range(len(list_of_dicts_basketball_players)):
        names.append(list_of_dicts_basketball_players[i]["name"])
    print(names)
    who_you_want = str(input("About which basketball player you would like to know? Enter his name >>> "))
    return who_you_want


# с.2 выводим данные одного баскетболиста
def about_person_you_want_to_know(who_you_want):
    pp = pprint.PrettyPrinter(indent=10, width=50,sort_dicts=False)
    for item in list_of_dicts_basketball_players:
        if who_you_want in item.values():
            pp.pprint(item)


# d. Написать функцию которая “красиво“ выводит на экран данные всех баскетболистов
def pretty_print_all():
    for i in range(len(list_of_dicts_basketball_players)):
        who_you_want = list_of_dicts_basketball_players[i]["name"]
        about_person_you_want_to_know(who_you_want)


# e. написать функцию которая принимает от пользователя данные нового баскетболиста и добавляет их в список
def add_basketball_player():
# variant_1 with immediate  write to the file
    # temp = "\n"
    # print(f"\nLets add new basketball player to the list of Glory.")
    # for i in range(len(keys)):
    #     new_info = str(input(f"Please enter his\her {keys[i]}: "))
    #     temp = temp + new_info + ","
    #
    # with open(file="famous_basketball_players.csv", mode="a") as file:
    #     file.write(temp)
    #     file.close()

# variant_2 with changes in global variable only (no changes within the file)
    temporary = []
    print(f"\nLets add new basketball player to the list of Glory.")
    for i in range(len(keys)):
        new_info = str(input(f"Please enter his\her {keys[i]}: "))
        temporary.append(new_info)
    list_of_dicts_basketball_players.append(dict(zip(keys,temporary)))

# f. написать функцию которая сохраняет всех баскетболистов в файл
def save():
    with open(file="famous_basketball_players.csv", mode="r") as existing_file:
        with open(file="Saved data", mode="w") as new_file:
            new_file.write(existing_file.read())


# g. написать функцию поиска баскетболиста по имени или фамилии
def search():
    who_you_want = str(input(f"About whom you want to know please enter {keys[0]} or {keys[1]}: "))
    for item in list_of_dicts_basketball_players:
        if who_you_want in item.values():
            print(item)
        elif who_you_want in item.keys():
            print(item)
        else:
            print("No such person in the list of famous basketball players :(")


# h. написать функцию которая напечатает данные 3 самых высоких баскетболистов
def three_tallest():
# variant_1
    new_sorted_list = sorted(list_of_dicts_basketball_players, key=lambda value: value["height"], reverse=True)
    print(new_sorted_list[0])
    print(new_sorted_list[1])
    print(new_sorted_list[2])

# variant_2
#     list_of_dicts_basketball_players.sort(key=operator.itemgetter("height"), reverse=True)
#     print(list_of_dicts_basketball_players[0])
#     print(list_of_dicts_basketball_players[1])
#     print(list_of_dicts_basketball_players[2])


# i. написать функцию которая удаляет баскетболиста из списка по имени и фамилии
def delete_payer():
    print(list_of_dicts_basketball_players)
    whom_to_delete = str(input("Please enter name or surname of the player to delete:   "))
    for item in list_of_dicts_basketball_players:
        if item["name"] == whom_to_delete or item["surname"] == whom_to_delete:
            list_of_dicts_basketball_players.remove(item)


# j. написать функцию main которая будет предлагать пользователю описанные выше возможности и выполнять их.
# Программа будет работать до тех пор пока пользователь не ввел -1 для выхода.
# В завершении программы программа будет сохранять список баскетболистов в файл.
def main():
    print("\033[32m\033[47m", "Please choose the option:"
          "\n1. Info about a player."
          "\n2. Info about famous players."
          "\n3. To add your favourite player to the list"
          "\n4. To save the list of famous players to another file."
          "\n5. To find the player in the list."
          "\n6. Info about three the tallest players."
          "\n7. To detele a player."
          "\n-1. To Save & Quit." "\033[0m")
    what_to_do = int(input("And enter option's number: "))
    while what_to_do != -1:
        if what_to_do == 1:
            about_person_you_want_to_know(who_you_want())
            what_to_do = int(input("\nEnter next option's number: "))
        elif what_to_do == 2:
            pretty_print_all()
            what_to_do = int(input("\nEnter next option's number: "))
        elif what_to_do == 3:
            add_basketball_player()
            what_to_do = int(input("\nEnter next option's number: "))
        elif what_to_do == 4:
            save()
            what_to_do = int(input("\nEnter next option's number: "))
        elif what_to_do == 5:
            search()
            what_to_do = int(input("\nEnter next option's number: "))
        elif what_to_do == 6:
            three_tallest()
            what_to_do = int(input("\nEnter next option's number: "))
        elif what_to_do == 7:
            delete_payer()
            what_to_do = int(input("\nEnter next option's number: "))
    else:
        global list_of_dicts_basketball_players
        print(list_of_dicts_basketball_players)
        with open(file="famous_basketball_players.csv", mode="w") as file:
            for item in list_of_dicts_basketball_players:
                file.write(",".join(item.values()) + "\n")
        print("Thanks for flying with Aeroflot :)")


if __name__ == "__main__":
    famous_basketball_players()
    main()