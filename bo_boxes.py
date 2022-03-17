# This code is a bit messy due to the syntax of reter.
# I could have optimised this code and cleaned it up but I opted not too.
# I'm a bit drained as of writing this, but this is a project I have come back too for fun from time to time.
# Anyways please enjoy the mess that is, Bo-Boxes.

# Quick note, some features were not fixed so some features do not work...

__author__ = "Zackery Smith"
__email__ = "zackery.smith82307@gmail.com"
__copyright__ = "Copyright © 2020 Zackery Smith. All rights reserved."
__license__ = "GNU GPL-3.0"
__version_info__ = (0, 0, 1)
__version__ = ".".join(map(str, __version_info__))

import sys
from reter import Terminal, indicator
from typing import Optional


########################################
# listBox
########################################

def listBox(terminal: Terminal, choices: list, cycle_cursor: bool=True, theme: Optional[dict]={"pady": 0, "bullet": None, "bulletSelection": ">", "bulletSpacing": " ", "selectionHighlight": indicator.colour.formatting.reverse, "highlightBullet": False, "selectionTextColor": None, "textColor": None, "bulletColor": None, "bulletSelectionColor": indicator.colour.fg.red}):
    """
    Creates selection list of objects.

    :rtype: String
    :return: Returns selection 
    """
    # Correctness checks
    for index, choice in enumerate(choices):
        if choice.strip() == "":
            raise ValueError("Empty choice item!")


    # Create "padx". It is a bit of a challenge to create so I left it out for now.
    
    # Create y padding (top)
    if theme["pady"] != 0 and theme["pady"] > 0:
        print("\n"*theme["pady"], end="", flush=True)

    terminal.cursor.change_visibility(False)
    
    lines = len(choices)
    for index, option in enumerate(choices):
        # Make sure only the needed amount of lines are created (according to theme)
        if index == lines-1:
            print(
                # Create all the bullets (Defined by theme)
                "" if theme["bulletColor"] == None else theme["bulletColor"] 
                ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) 
                if theme["highlightBullet"] == True else 
                (" "*len(theme["bulletSelection"]) if theme["bullet"] == None else theme["bullet"])

                # Add extra spacing if defined
                + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"])
                # Set the text colour
                + ("" if theme["textColor"] == None else theme["textColor"]) 
                # Finally add the option (text)
                + option, end='', flush=True
            )
        
        elif index != lines:
            print(
                # Bullet points
                (
                    # Create all the bullets (Defined by theme)
                    "" if theme["bulletColor"] == None else theme["bulletColor"] 
                    ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"])
                    if theme["highlightBullet"] == True else (" "*len(theme["bulletSelection"])
                    if theme["bullet"] == None else theme["bullet"])
                )
                
                # Add extra spacing if defined
                + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"])
                # Set the text colour
                + ("" if theme["textColor"] == None else theme["textColor"])
                # Finally add the option (text)
                + option
            )
        
        #elif index==lines:  # Really never used. Kept just incase a user goes beyond other checks
        #    print((("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) if theme["highlightBullet"] == True else (" " if theme["bullet"] == None else theme["bullet"])) + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"]) + ("" if theme["textColor"] == None else theme["textColor"]) + option, end='', flush=True)
    
    # Realign cursor
    terminal.cursor.move(0, -len(choices)-1)
    terminal.cursor.align("left")

    startingLine = currentLine = 1
    while True:
        stripped = choices[currentLine-1].rstrip()
        # Current selected option theming
        sys.stdout.write(
            # Highlight bullet
            (
                ("" if theme["selectionHighlight"] == None else theme["selectionHighlight"])
                if theme["highlightBullet"] == True else ""
            )
            
            # Set all colours for text
            +(" " if theme["bulletSelection"] == None else ("" if theme["bulletSelectionColor"] == None else theme["bulletSelectionColor"])
            + theme["bulletSelection"]) + ("" if theme["bulletSelectionColor"] == None else indicator.colour.formatting.eoc)
            + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"])
            + ("" if theme["selectionHighlight"] == None else theme["selectionHighlight"])
            + ("" if theme["selectionTextColor"] == None else theme["selectionTextColor"])
            # Option + An end of colour statement
            + stripped + indicator.colour.formatting.eoc
        )
        terminal.cursor.align("left")
        key = terminal.keyboard.capture_key()

        if key == indicator.arrow.up:
            if currentLine-1 <= 0:  # Make sure current line and cursor don't move any further
                if cycle_cursor:
                    # Reset selection highlight (According to theme)
                    sys.stdout.write(
                        (
                            indicator.colour.formatting.eoc if theme["textColor"] == None else theme["textColor"]  # Text colour
                        )

                        + (" "*len(theme["bulletSelection"]) if theme["bullet"] == None else theme["bullet"])  # Bullet selection
                        + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"])  # Bullet spacing
                        + stripped + indicator.colour.formatting.eoc  # Text
                    )
                    # Move cursor
                    terminal.cursor.move(0, len(choices)-1)
                    terminal.cursor.align("left")
                    
                    currentLine+=len(choices)-1 # Let the rest of the code know we jumped
                continue  
            
            elif currentLine == 0:
                currentLine+=1
                terminal.cursor.move(0, -1)
                continue

            currentLine-=1
            # Reset selection highlight (According to theme)
            sys.stdout.write(
                (
                    indicator.colour.formatting.eoc if theme["textColor"] == None else theme["textColor"]  # Text colour
                )

                + (" "*len(theme["bulletSelection"]) if theme["bullet"] == None else theme["bullet"])  # Bullet selection
                + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"])  # Bullet spacing
                + stripped + indicator.colour.formatting.eoc  # Text
            )
            terminal.cursor.move(0, -1)
            terminal.cursor.align("left")

        elif key == indicator.arrow.down:
            if currentLine+1 >= len(choices)+1:  # Make sure current line and cursor don't move any further
                if cycle_cursor:
                    # Reset selection highlight (According to theme)
                    sys.stdout.write(
                        (
                            indicator.colour.formatting.eoc if theme["textColor"] == None else theme["textColor"]  # Text colour
                        )

                        + (" "*len(theme["bulletSelection"]) if theme["bullet"] == None else theme["bullet"])  # Bullet selection
                        + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"])  # Bullet spacing
                        + stripped + indicator.colour.formatting.eoc  # Text
                    )
                    # Move cursor
                    terminal.cursor.move(0, -(len(choices)-1))
                    terminal.cursor.align("left")
                    
                    currentLine-=len(choices)-1 # Let the rest of the code know we jumped
                continue
            elif currentLine > len(choices):
                currentLine-=1
                terminal.cursor.move(0, 1)
                continue
            currentLine+=1
            # Reset selection highlight (According to theme)
            sys.stdout.write(
                (
                    indicator.colour.formatting.eoc if theme["textColor"] == None else theme["textColor"]  # Text colour
                )

                + (" "*len(theme["bulletSelection"]) if theme["bullet"] == None else theme["bullet"])  # Bullet selection
                + ("" if theme["bulletSpacing"] == None else theme["bulletSpacing"])  # Bullet spacing
                + stripped + indicator.colour.formatting.eoc)  # Text
            
            terminal.cursor.align("left")
            terminal.cursor.move(0, 1)
        
        elif key == indicator.escape.enter:
            # Fix cursor (position, visibility, and add padding if needed)
            terminal.cursor.move(0, (len(choices)-currentLine))  # Fix pos
            if theme["pady"] != 0 and theme["pady"] > 0:
                print("\n"*theme["pady"], end="", flush=True)
                terminal.cursor.move(0, -theme["pady"])  # Fix me
            terminal.cursor.change_visibility(True)  # Return visibility
            
            # Remove all special formating
            print(indicator.colour.formatting.eoc, end="\n")
            return choices[currentLine-1]
        else:
            pass
