#!/usr/bin/env pyhton3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 12:25:03 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/19 15:11:09 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: float) -> None:
        self.name = name
        self.height = height
        self.age = age

    def growth(self) -> None:
        print("=== Garden Plant Growth ===")
        initial_height = self.height
        for i in range(1, 8):
            print("=== Day " + str(i) + " ===")
            print(self.name + ": " + str(round(self.height, 1)) + "cm, "
                  + str(self.age) + " days old")
            self.height += 0.8
            self.age += 1
        print("Growth this week: " + str(round(self.height
              - initial_height, 0)) + "cm")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    rose.growth()
