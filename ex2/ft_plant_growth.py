#!/usr/bin/env pyhton3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 12:25:03 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/25 12:50:49 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: float) -> None:
        self.name = name
        self.height = height
        self.age = age

    def growth(self) -> None:
        self.height += 0.8
        self.age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    initial_height = rose.height
    for i in range(1, 8):
        print("=== Day " + str(i) + " ===")
        print(rose.name + ": " + str(round(rose.height, 1)) + "cm, "
              + str(rose.age) + " days old")
        rose.growth()
    print("Growth this week: " + str(round(rose.height
          - initial_height)) + "cm")
