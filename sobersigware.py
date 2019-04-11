# program for picking the sober sigs for the week
import random
import numpy

# potential updates
# basketball, baseball season schedule input
# writes picking and volunteers recorded, If you were picked more recently it lowers chances, if brother not here
# Count how many times and lower the chances, and if you are picked more and scholarship points


# class Sobersigware to run the actual program simulation and produce output
class Sobersigware:

    year_dict = {'0': .60, '1': 0.75, '2': 0.90, '3': .99}

    # class Brother to contain the characteristics of a Brother who could become a sober sig
    class Brother:
        # Brother instance constructor
        def __init__(self, brother, year, obligation, volunteering, service):
            # fields for a Brother object
            self.name = brother
            self.year = year
            self.ro_complete = obligation
            self.num_volunteer = volunteering
            self.service_hours = service
            self.eta_value = 0
            self.is_volunteer = False
            self.has_immunity = False

        def __str__(self):
            return f"{self.name}: {self.eta_value}"

    # avoid typing errors
    @staticmethod
    def avoid_typing_errors(brother_index):
        # prevent any typing or allocation errors
        incrementation = 0
        brothers = numpy.empty(brother_index, dtype=object)
        for bro in brothers:
            if isinstance(bro, Sobersigware.Brother):
                brothers[incrementation] = bro
                incrementation += 1

    # fight the chance to be sober sig
    @staticmethod
    def fight_chance(brothers, sobersigs, sobersigs_index):
        # fight vs chance to not be chosen for sober sig
        while sobersigs_index < 9:
            for bro in brothers:
                chance = random.random()
                if bro and bro.eta_value < chance and sobersigs_index < 9 and not bro.has_immunity:
                    sobersigs[sobersigs_index] = bro
                    sobersigs_index += 1

    # outputs nine names on position indexes for sober sig assignment
    @staticmethod
    def main():
        # initialize state
        volunteers = str(input("Any Volunteers?: ")).split(", ")  # must differentiate names by ,
        immunity = str(input("Phone Game Winners: ")).split(", ")  # must differentiate names by ,
        sobersigs = numpy.empty(9, dtype=object)  # int(input("How many Sobersigs?: "))
        brothers = numpy.empty(40, dtype=object)  # int(input("How many Brothers?: "))
        table = numpy.empty(3, dtype=object)
        # storage file of brothers and file information
        file = open("Brothers.txt", "r")

        # assignment indices
        brother_index = 0
        incrementation = 0
        sobersigs_index = 0

        for line in file:
            # storage of brother information
            brother_name = ""
            brother_num = ""
            table_position = False
            # reads information to create instance of Brother

            for letter in line:
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
            if bool(pledge.ro_complete):
                pledge.eta_value -= .10
            if bool(pledge.service_hours):  # could update it incrementally
                pledge.eta_value -= .10
            pledge.eta_value += int(pledge.num_volunteer) * 0.025  # add .025 for each volunteer
            # if someone volunteers

            for brother in volunteers:
                if brother == pledge.name:
                    pledge.is_volunteer = True
                    sobersigs[sobersigs_index] = pledge
                    sobersigs_index += 1

            # records brothers who possess immunity
            for brother in immunity:
                if pledge.name == brother:
                    pledge.has_immunity = True

            if not pledge.is_volunteer and not table_position:
                brothers[brother_index] = pledge
                brother_index += 1

        # randomize entry order and close outer loop
        random.shuffle(brothers)
        random.shuffle(table)
        file.close()

        Sobersigware.avoid_typing_errors(brother_index)
        Sobersigware.fight_chance(brothers, sobersigs, sobersigs_index)

        # output the sober sigs
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

    def __init__(self):
        Sobersigware.main()


if __name__ == '__main__':
    Sobersigware()
