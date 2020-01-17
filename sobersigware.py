# program for picking the sober sigs for the week

import random
import numpy
from brothers_list import brothers_list

# class Sobersigware to run the actual program simulation and produce output
class Sobersigware:
    year_dict = {'0': .60, '1': 0.75, '2': 0.90, '3': .99}

    # class Brother to contain the characteristics to determine the eta value
    class Brother:

        # Brother instance constructor
        def __init__(self, name, year, ro_complete, num_volunteer, service_hours):
            # fields for a Brother object
            self.name = name
            self.year = year
            self.ro_complete = ro_complete
            self.num_volunteer = num_volunteer
            self.service_hours = service_hours
            # probablistic value for sober sig determination
            self.eta_value = 0
            self.is_volunteer = False
            self.has_immunity = False

        def __str__(self):
            # for easily readible characteristics
            return f"{self.name}: {self.eta_value}"

    # avoid typing errors
    @staticmethod
    def avoid_typing_errors(brother_index):
        # prevent any typing or allocation errors
        incrementation = 0
        brothers = numpy.empty(brother_index, dtype=object)
        for bro in brothers:
            # if the index is not empty
            if bro:  # isinstance(bro, Sobersigware.Brother):
                brothers[incrementation] = bro
                incrementation += 1

    # fight the chance to be sober sig
    @staticmethod
    def fight_chance(brothers, sobersigs, sobersigs_index):
        # fight vs chance to not be chosen for sober sig
        while sobersigs_index < 9:
            for bro in brothers:
                chance = random.random()
                if bro and all([bro.eta_value < chance, sobersigs_index < 9, not bro.has_immunity]):
                    sobersigs[sobersigs_index] = bro
                    sobersigs_index += 1

    # print the sobersigs in a readable format
    @staticmethod
    def output_sobersigs():
        print("                      ")
        print("Thursday: ")
        print(str(table[0]))
        print(str(sobersigs[0]))
        print(str(sobersigs[3]))
        print("                      ")
        print("Friday: ")
        print(str(table[1]))
        print(str(sobersigs[1]))
        print(str(sobersigs[4]))
        print("                      ")
        print("Saturday: ")
        print(str(table[2]))
        print(str(sobersigs[2]))
        print(str(sobersigs[5]))
        print("                      ")


if __name__ == '__main__':
    # must differentiate names by ,
    volunteers = str(input("Any Volunteers?: ")).split(", ")
    immunity = str(input("Phone Game Winners: ")).split(", ")
    sobersigs = numpy.empty(9, dtype=object)  # int(input("How many Sobersigs?: "))
    brothers = numpy.empty(50, dtype=object)  # int(input("How many Brothers?: "))
    table = numpy.empty(3, dtype=object)
    # storage file of brothers and file information
    # file = open("Brothers.txt", "r")

    # assignment indices
    brother_index = 0
    incrementation = 0
    sobersigs_index = 0

    # creating an instance of each brother and instantiating the values
    # for line in file:
    for bro in brothers_list:
        # storage of brother information
        brother_name = ""
        brother_num = ""
        table_position = False

        # reads the numbers in the file to assign values
        for letter in bro:
            if letter.isdigit():
                brother_num = brother_num + letter
            if letter.isalpha() or letter == " ":
                brother_name = brother_name + letter
            if letter == "!":
                table_position = True

        # the instance is created
        pledge = Sobersigware.Brother(brother_name, str(brother_num[0]), brother_num[1], brother_num[2], brother_num[3])

        # for consul, pro consul, and risk manager
        if table_position:
            table[incrementation] = pledge
            incrementation += 1

        # the eta_value is determined
        pledge.eta_value = Sobersigware.year_dict[pledge.year]
        # decrement if ros have not been completed
        if bool(pledge.ro_complete):
            pledge.eta_value -= .10
        # decrement if service hours have not been completed
        if bool(pledge.service_hours):
            pledge.eta_value -= .10
        # add .025 for each volunteer
        pledge.eta_value += int(pledge.num_volunteer) * 0.025

        # if someone volunteers
        for brother in volunteers:
            if brother == pledge.name:
                pledge.is_volunteer = True
                sobersigs[sobersigs_index] = pledge
                sobersigs_index += 1

        # records brothers who possess immunity from phone game or special privildege
        for brother in immunity:
            if pledge.name == brother:
                pledge.has_immunity = True

        # if a brother is not a volunteer or tabel position
        if not pledge.is_volunteer and not table_position:
            brothers[brother_index] = pledge
            brother_index += 1

    # randomize entry order and close outer loop
    random.shuffle(brothers)
    random.shuffle(table)

    Sobersigware.avoid_typing_errors(brother_index)
    Sobersigware.fight_chance(brothers, sobersigs, sobersigs_index)

    # outputs nine names on position indexes for sober sig assignment
    Sobersigware.output_sobersigs()