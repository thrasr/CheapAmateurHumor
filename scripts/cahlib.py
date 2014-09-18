from os import path
from PIL import Image
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageDraw

BLANK = '../resources/blankcard.png'
PICK = '../resources/pick'
DEFAULTICON = "../resources/fullicon.png"
FONT = ImageFont.truetype('../resources/helvetica-neue-bold.ttf', 56)
LINELENGTH = 530

## EXPAND FUNCTIONS
def underscores(words, lines):
    # Mirror function of expander that deals with underscores
    
    # Determine words on line before '_'
    line = ''
    i = 0
    for word in words:
        if '_' not in word:
            line += word + ' '
            i += 1
        else:
            break

    # words[i] now points to _*
    # If line is too short for a blank, we have two lines
    # Note we're measuring including the space and punctuation
    if FONT.getsize(line + words[i][1:])[0] > 335:
        lines.append(line.strip())
        temp = words[i]
        while True:
            if FONT.getsize('_' + temp)[0] > LINELENGTH:
                lines.append(temp)
                return expander(words[i+1:], lines)
            temp = '_' + temp

    # Line has room for a blank
    while True:
        if FONT.getsize(line + '_' + words[i])[0] > LINELENGTH:
            lines.append(line + words[i])
            return expander(words[i+1:], lines)
        line = line + '_'


def expander(words, lines):
    # Tail-end recursion function to figure out lines

    # Exit condition
    if len(words) == 0:
        return lines
 
    # Determine max words that can fit on line
    line = words[0]
    i = 1
    while True:
        if i >= len(words):
            break 
        elif FONT.getsize(line + ' ' + words[i])[0] > LINELENGTH:
            break

        line = line + ' ' + words[i]
        i += 1

    # If blank on the line, redo line in mirror function
    # Else recurse
    if '_' in line:
        return underscores(words, lines)
    else:
        lines.append(line)
        return expander(words[i:], lines)

def stripunderscores(text):
    # Sanitize input - strip down to a single '_'
    while '__' in text:
        text = text.strip().replace('__', '_')
    return text

def expand(text):
    # Prepare for and determine text format
    text = stripunderscores(text)

    lines = []
    words = text.split()
    result = expander(words, lines)
    if len(result) > 9:
        print "WARNING - CARD TEXT IS TOO LONG"
        print "CANNOT CREATE CARD WITH TEXT:"
        print text
    return result[:9]

## CREATE FUNCTIONS
def createicon(name):
    # Open default full icon
    full = Image.open("../resources/fullicon.png")

    # Open custom icon
    icon = Image.open('../sets/' + name + '/assets/' + name + 'icon.png')

    # Paste custom icon onto full icon
    coords = (27, 18)
    full.paste(icon, coords, mask=icon)

    # Return new icon
    return full

def createwhitecard(name, card):
    # Start with blank card
    im = Image.open(BLANK)

    # Add set icon
    if path.isfile('../sets/' + name + '/assets/' + name + 'icon.png'):
        icon = createicon(name)
    else:
        icon = Image.open(DEFAULTICON)

    iconbox = (144, 915, 483, 990)
    im.paste(icon, iconbox, mask=icon)

    # Add text
    im = im.convert('RGB')
    draw = ImageDraw.Draw(im)
    text = expand(card['text'])
    num = 0
    for line in text:
        draw.text((146, 134+68*num), line, font=FONT, fill='black')
        num += 1


    # Save image
    im.save('../sets/' + name + '/' + card['name'] + '.png', dpi=(300,300))

    #return im


def createblackcard(name, card):
    # Start with blank card
    im = Image.open(BLANK)

    # Add set icon
    if path.isfile('../sets/' + name + '/assets/' + name + 'icon.png'):
        icon = createicon(name)
    else:
        icon = Image.open(DEFAULTICON)

    iconbox = (144, 915, 483, 990)
    im.paste(icon, iconbox, mask=icon)

    # Check for pick x icon
    pnum = card['pick']
    # Use given pick icon if present, count _'s otherwise
    if pnum == 0:
        pnum = stripunderscores(card['text']).count('_')
    # Add icon if needed
    if pnum == 2 or pnum == 3:
        pick = Image.open(PICK + str(pnum) + '.png')
        pickbox = (471, 853, 696, 1003)
        im.paste(pick, pickbox, mask=pick)


    # Add text
    im = im.convert('RGB')
    draw = ImageDraw.Draw(im)
    text = expand(card['text'])
    num = 0
    for line in text:
        draw.text((146, 134+68*num), line, font=FONT, fill='black')
        num += 1

    # Invert text to make black card
    im = ImageOps.invert(im)

    # Save image
    im.save('../sets/' + name + '/' + card['name'] + '.png', dpi=(300,300))

    #return im

def createback(name, line1, line2, line3):
    # Start with black card
    im = Image.open(BLANK)
    im = im.convert('RGB')
    
    font = ImageFont.truetype('../resources/helvetica-neue-bold.ttf', 127)
    draw = ImageDraw.Draw(im)

    # Validate line sizes
    if font.getsize(line1)[0] > 576 or font.getsize(line2)[0] > 576 or font.getsize(line3)[0] > 576:
        print "WARNING - CARD BACK TEXT TOO LONG"
        print "TEXT MAY OVERFLOW OFF CARD"

    # Add text (with 120 pixel between lines)
    # Lines adjusted assuming a C, A, H for the first letters
    draw.text((145, 120), line1, font=font, fill='black')
    draw.text((146, 240), line2, font=font, fill='black')
    draw.text((140, 360), line3, font=font, fill='black')
    
    # Save white card back
    im.save('../sets/' + name + '/assets/wcardback.png', dpi=(300,300))
    
    # Invert image and save black card back
    im = ImageOps.invert(im)
    im.save('../sets/' + name + '/assets/bcardback.png', dpi=(300,300))
