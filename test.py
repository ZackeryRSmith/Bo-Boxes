# Bug: Trying to use two list boxes at once breaks the script's visual element
#      It does fix itself after you move through the options


import reter
import bo_boxes
import os

terminal = reter.Terminal().quick_start()

# Quality of life
Fore   = reter.indicator.colour.fg 
Back   = reter.indicator.colour.bg
Style  = reter.indicator.colour.formatting

# Shows the default theme
#option = bo_boxes.listBox(terminal, ["option1", "option2", "option3"])

# This example is a bit "colorful" and "abstract" but it displays all Bo-Boxes features
option = bo_boxes.listBox(terminal, ["option1", "option2", "option3"], True,
                          {
                              "pady": 0,                            # Broken
                              "bullet": "◦",
                              "bulletSelection":"•",
                              "bulletSpacing":" | ",
                              "selectionHighlight":Style.bold,
                              "highlightBullet":None,               # Broken
                              "selectionTextColor":Fore.green,
                              "textColor":Fore.blue,
                              "bulletColor":Back.red,               # Broken
                              "bulletSelectionColor":Back.magenta,
                          })

print(option)
