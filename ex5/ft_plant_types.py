#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 15:03:28 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/17 15:30:40 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height = height
        self._age = age

        
class Flower:
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self._color = color
        self._bloom = 0
    
    def bloom(self):
        print("[asking the " + self._name + " to bloom]")
        self.bloom = 1

    def show(self):
        

         
class Tree:
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self):
        print("Tree " + self._name + " now produce a shade of " + self._height + " cm long and " + self._trunk_diameter + " cm wide")


class Vegetable:
    def __init__(self, name, height, age, harvest_season, nutrition_value):
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutrition_value = nutrition_value

    def produce_shade(self):
        print("Tree " + self._name + " now produce a shade of " + self._height + " cm long and " + self._trunk_diameter + " cm wide")
    