#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 13:47:28 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/29 12:03:04 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: float) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print("Plant created: " + self._name + ": " + str(round(self._height,
              1)) + "cm, " + str(self._age) + " days old")

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(self._name + ": Error, height can't be negative")
            print("Height update rejected")
        elif (height >= 0):
            self._height = float(height)
            print("Height updated: " + str(self._height) + "cm")
        # else:
        #     print(self._name + ": Invalid data")

    def set_age(self, age: float) -> None:
        if (age < 0):
            print(self._name + ": Error, age can't be negative")
            print("Age update rejected")
        elif (age >= 0):
            self._age = age
            print("Age updated: " + str(self._age) + " days")
        # else:
        #     print(self._name + ": Invalid data")

    def get_name(self) -> str:
        return (self._name)

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> float:
        return (self._age)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15.0, 10)
    p1.show()
    print("")
    p1.set_height(25)
    p1.set_age(30)
    print("")
    p1.set_height(-25)
    p1.set_age(-30)
    print("")
    print("Current state: " + p1.get_name() + ": " + str(round(
          p1.get_height(), 1)) + "cm, " + str(p1.get_age()) + " days old")
