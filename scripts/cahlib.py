from os import path
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

DEBUG = 1
PUNCTUATION = [',', '.', ';', ':', '!', '?', '/', '(', ')']
BLANK = '../resources/blankcard.png'
PICK = '../resources/pick'
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
    # Start with blank card
    im = Image.open(BLANK)

    # Add set icon
    if DEBUG:
        icon = Image.open("../resources/fullicon.png")
    elif path.isfile('../sets/' + name + '/assets/icon.png'):
        icon = Image.open('../sets/' + name + '/assets/icon.png')
    else:
        icon = Image.open(DEFAULTICON)

    iconbox = (144, 915, 483, 990)
    im.paste(icon, iconbox, mask=icon)

    # Add text
    #card['text']

    # Save image
    im.save('../sets/' + name + '/' + card['name'] + '.png')

    #return im


def createblackcard(name, card):
    # Start with blank card
    im = Image.open(BLANK)

    # Add set icon
    if DEBUG:
        icon = Image.open("../resources/fullicon.png")
    elif path.isfile('../sets/' + name + '/assets/icon.png'):
        icon = Image.open('../sets/' + name + '/assets/icon.png')
    else:
        icon = Image.open(DEFAULTICON)

    iconbox = (144, 915, 483, 990)
    im.paste(icon, iconbox, mask=icon)


    # Add pick icon if needed
    if (card['pick'] == 2) or (card['pick'] == 3):
        pick = Image.open(PICK + str(card['pick']) + '.png')
        pickbox = (471, 853, 696, 1003)
        im.paste(pick, pickbox, mask=pick)

    # Add text
    #card['text']

    # Invert text to make black card
    #PIL.invert

    # Save image
    im.save('../sets/' + name + '/' + card['name'] + '.png')

    #return im

def createback(name, line1, line2, line3):
    # Start with black card
    im = Image.open(BLANK)

    # Add text
    #PIL.type line1
    #PIL.type line2
    #PIL.type line3
    
    # Save white card back
    im.save('../sets/' + name + '/assets/wcardback.png')
    
    # Invert image and save black card back
    #PIL.invert
    im.save('../sets/' + name + '/assets/bcardback.png')
