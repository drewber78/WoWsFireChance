# ------------------------------------------------------------------------ #
# Title: Fire Chance Probability
# Description: Calculate the fire chance probability based on fire chance percentage with number of shells hit out of
# number of shells fired.
#
# ChangeLog (Who,When,What):
#           Drew Cochran, 01APR2023, Created project, working initial script
# 
# 
# ------------------------------------------------------------------------

import os

# Data ------------------------------------------------------------------#

strFileName = 'fire_chance.txt'
lstOfShipObjects = []
strExit = 'exit'

class ShipFireChance:
    """
    Stores data about a ships particular fire chance

    properties:

    methods:
        get & set for ship_class
        get & set for fire_chance


    changelog: (Who, When, What)
    Drew Cochran, 01APR2023, Created class and built constructor and methods/properties

    """

    # Constructor

    def __int__(self, ship_class, fire_chance, number_of_hits, number_of_guns_fired):
        """
        Init function for the class. Defines which ship class, what the fire chance per hit is, and how many shipboard
        guns were fired at a target
        :param ship_class: The class of ship to store data; i.e. Smolensk, Zao, Conqueror, etc.
        :param fire_chance: % of fire chance as stated in WoWs
        :param number_of_hits: Number of shell hits on the target, damaging or otherwise
        :param number_of_guns_fired: number of guns fired per salvo; this can vary
        :return:
        """

        # Establish initial variables
        self.__ship_class = ship_class
        self.__fire_chance = fire_chance
        self.__number_of_hits = number_of_hits
        self.__number_of_guns_fire = number_of_guns_fired

    def get_ship_class(self):
        """
        Returns ship class
        :return: self.__ship_class
        """
        return self.__ship_class

    @staticmethod
    def set_ship_class(self, value):
        """
        Sets the ship class. Does a try/except to determine if value is numeric after initial setting.
        :param value:
        :return:
        """
        self.__ship_class = value

    def get_fire_chance(self):
        """
        Returns the fire chance for a specific ship class.
        :return: self.__fire_chance
        """
        return self.__fire_chance

    @staticmethod
    def set_fire_chance(self, value):
        """
        Changes the fire chance of a specific ship class.
        :param value: fire chance
        :return:
        """
        self.__fire_chance = value

    @staticmethod
    def to_string(self):
        """
        Returns the ship class and the fire chance in a string to be output on screen for a user to see, based on the
        fire chances and ships user has inputted.
        :param self:
        :return: object_data
        """
        object_data = self.__ship_class + ', ' + self.__fire_chance + '%'
        return object_data

    def __str__(self):
        """
        Returns to_string. Overrides default Python string function
        :return: to_string function
        """
        return self.to_string(self)


# Processing
class FileProcessor:
    """
    Processes data to and from a file for the list of ship fire chance objects:

    methods:
        save_data_to_file(file_name, list_of_ship_objects):

        read_data_from_file(file_name): -> (a list of ship class objects with fire chance)

    changelog: (Who, When, What)
        Drew Cochran, 02APR2023, Created class, intial methods, hoping to complete all today.
    """

    def __init__(self):
        """
        Init for class.
        """

    @staticmethod
    def read_data_from_file():
        """
        Reads the data from fire_chance.txt into lstOfShipObjects for future use in the program.

        :return:
        """

        # if check to see if file exists; else, file is created via append. The file will be located in the same
        # directory as this program. Can be changed in code below.

        isExisting = os.path.exists(os.getcwd() + '/' + os.path.normpath(strFileName))
        if isExisting is True:
            try:
                # creates object of the text file
                objClassShip = open(os.getcwd() + '/' + strFileName, 'r')
                # for loop to read in data to lstOfShipObjects
                for row in objClassShip:
                    # splits the comma out of the data
                    lstRow = row.split(',')
                    # Runs the data through the ShipFireChance Class
                    objRow = ShipFireChance(lstRow[0], lstRow[1])
                    lstOfShipObjects.append(objRow)
                objClassShip.close()
            # Create print statement for error message.
            except TypeError as v:
                print(v)
                print("Error retrieving data from file.")

        else:
            objClassShip = open(os.getcwd() + '/' + os.path.normpath(strFileName), 'a')
            objClassShip.close()

    @staticmethod
    def save_data_to_file():
        """
        Writes the data from lstOfShipObjects to fire_chance.txt and closes file. Overwrites all existing data
        :return:
        """

        # Opens file
        objClassShip = open(os.getcwd() + '/' + os.path.normpath(strFileName), 'w')

        # Iterate through lstOfShipObjects to then write to Fire_Chance.txt. Adds a comma and a new line after each
        #list item pair of ship_class and fire_chance

        try:
            for row in lstOfShipObjects:
                ship_class = str(row.get_ship_class())
                fire_chance = str(row.get_fire_chance())
                objClassShip.write(ship_class + ',' + fire_chance +'\n')

        except TypeError as v:
            print(v)
            print("Unable to save data to file.")

        # closes file and prints success statement
        objClassShip.close()
        print("Items saved successfully to fire_chance.txt.")

# Processing   ------------------------------------------------------------------#

# Presentation (Input/Output)   -------------------------------------------------#

class IO:
    """
    Class for performing Input and Output

    methods:
        print_items(): Prints current ship class and fire chance from list.

        print_menu_items(): Prints user menu

        input_ship_class_data(): Inputs new data into lstOfShipObjects

        change_class_or_fire_chance: allows for the change in ship_class or fire_chance

        calculate_overall_fire_chance: Based on number of shells fired, number of hits, and ship's fire chance.

    changelog: (Who, When, What)
        Drew Cochran, 02APR2023, Created Class
    """