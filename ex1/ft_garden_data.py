#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 12:08:57 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/12 12:22:25 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: int, age: int):
        print(name + ": " + str(height) + "cm, " + str(age) + " days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    Plant("Rose", 25, 30)
    Plant("Sunflower", 80, 45)
    Plant("Cactus", 15, 120)
