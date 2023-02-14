# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/14/23
# Description: The std_dev function calculates the population standard deviation of the ages of Person objects in a
#              list. It first computes the mean age and the sum of squared differences from the mean,
#              then calculates the standard deviation using the population formula.

class Person:
    """
    A class that represents a person with a name and an age.

    _name: The name of the person.
    _age: The age of the person.
    """

    def __init__(self, name, age):
        """
        Initializes a new instance of the Person class with the given name and age.

        name: The name of the person.
        age: The age of the person.
        """

        self._name = name
        self._age = age

    def get_age(self):
        """
        Returns the age of the person.
        """
        return self._age


def std_dev(person_list):
    """
    Calculates the population standard deviation of the ages of a list.

    person_list (list): A list of person objects.

    Returns: The population standard deviation of the ages of the person objects in the list.
    """

    n = len(person_list)

    total_age = sum([person.get_age() for person in person_list])
    mean_age = total_age / n

    sum_squares = sum([(person.get_age() - mean_age) ** 2 for person in person_list])

    variance = sum_squares / n
    std_dev = variance ** 0.5

    return std_dev
