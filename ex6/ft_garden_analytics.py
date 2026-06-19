#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 15:03:28 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/19 15:58:01 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: float) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_age(self) -> None:
        self._age += 1

    def set_grow(self) -> None:
        self._height = round(self._height + 2.1, 1)

    def get_age(self) -> float:
        return (self._age)

    def get_grow(self) -> float:
        return (self._grow)

    def show(self) -> None:
        print(self._name + ": " + str(self._height) + "cm, " +
              str(self._age) + " days old")
        Plant.stat.stat_show += 1

    @staticmethod
    def check_age(ch_age: float) -> None:
        res: bool = (ch_age > 365)
        print("Is " + str(ch_age) + " days more than a year? -> " + res)

    def stat(self) -> None:
        stat_age: int = 0
        stat_grow: int = 0
        stat_show: int = 0
        print(f"[statistics for {self._name}]")
        print(f"Stats: {stat_grow} grow, {stat_age} age, {stat_show} show")


class Flower(Plant):
    def __init__(self, name, height, age, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._bloom = 0

    def bloom(self):
        print("[asking the " + self._name + " to bloom]")
        self._bloom = 1

    def show(self):
        super().show()
        print(" Color: " + self._color)
        if (self._bloom == 0):
            print(" " + self._name + " has not bloomed yet")
        else:
            print(" " + self._name + " is blooming beautifully!")
        self._show += 1


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print("[asking the " + self._name + " to produce shade]")
        print("Tree " + self._name + " now produce a shade of " + 
              str(self._height) + "cm long and " + str(self._trunk_diameter)
              + "cm wide.")

    def show(self):
        super().show()
        print(" Trunk diameter: " + str(self._trunk_diameter))


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    super().rose.stat()
    # rose.bloom()
    # rose.show()
    # print("\n=== Tree")
    # oak = Tree("Oak", 200.0, 365, 5.0)
    # oak.show()
    # oak.produce_shade()
    # print("\n=== Vegetable")
    # tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    # tomato.show()
    # print("[make " + tomato._name + " grown and age for 20 days]")
    # for i in range(20):
    #     tomato.grow()
    #     tomato.age()
    # tomato.show()
