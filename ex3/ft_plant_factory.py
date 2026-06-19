#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 13:09:05 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/19 15:11:42 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:
    def __init__(self, name: str, height: float, age: float) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print("Created: " + self.name + ": " + str(self.height) + "cm, "
              + str(self.age) + " days old")


if __name__ == "__main__":
    print("=== Plant Factorry Output ===")
    p1 = Plant("Rose", 25.0, 30)
    p2 = Plant("Oak", 200.0, 365)
    p3 = Plant("Cactus", 5.0, 90)
    p4 = Plant("Sunflower", 80.0, 45)
    p5 = Plant("Fern", 15.0, 120)
    for plant in [p1, p2, p3, p4, p5]:
        plant.show()
