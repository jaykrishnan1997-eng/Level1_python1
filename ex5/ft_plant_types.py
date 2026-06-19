#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 15:03:28 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/19 12:00:56 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age
    
    def age(self):
        self._age += 1
        
    def grow(self):
        self._height = round(self._height + 2.1, 1)
        
    def show(self):
        print(self._name + ": " + str(self._height) + "cm, " +
              str(self._age) + " days old")


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


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season: str, n_value: int):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._n_value = n_value
        
    def age(self):
        super().age()

    def grow(self):
        super().grow()
        self._n_value += 1
    
    def show(self):
        super().show()
        print(" Harvest season: " + self._harvest_season)
        print(" Nutritional value: " + str(self._n_value))


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make " + tomato._name + " grown and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()
