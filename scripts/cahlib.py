from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

PUNCTUATION = [',', '.', ';', ':', '!', '?', '/', '(', ')']
PICK2 = '../resources/pick2.png'
PICK3 = '../resources/pick3.png'
DEFAULTICON = '../sets/misc/assets/icon.png'

## PARSE
def expand(text):
    # Expand single '_' into right size
    # Easy version is to expand to a set number (5?)
    # Hard version is to expand to fill the line
    ## Leave room for punctuation at the end
    ## If blank is below a threshhold (4?), then go to next line

    pass
    return text

## CREATE
def createwhitecard(name, card):
    # Start with black card
    
    # Add set icon
    if '../sets/' + name + '/assets/icon.png':
        #import and add icon
    else:
        #import and add DEFAULTICON'

    # Add text
    #card.text

    # Save image
    #card.name + '.png'


def createblackcard(name, card):
    # Start with black card
    pass

    # Add set icon
    if '../sets/' + name + '/assets/icon.png':
        #add icon
    else:
        #add DEFAULTICON

    # Add pick icon if needed
    if card.pick == 2:
        #add PICK2
    elif card.pick == 3:
        #add PICK3

    # Add text
    #card.text

    # Invert text to make black card
    #PIL.invert

    # Save image
    #card.name + '.png'

createback(name, line1, line2, line3)
    # Start with black card
    pass

    # Add text
    #PIL.type line1
    #PIL.type line2
    #PIL.type line3
    
    # Save white card back
    #'../sets/' + name + '/assets/wcardback.png'
    
    # Invert image and save black card back
    #PIL.invert
    #'../sets/' + name + '/assets/bcardback.png'
