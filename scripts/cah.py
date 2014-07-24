from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

## FRONT OF CARD
# RESEARCH - Better to create card and then invert it? or create from scratch?

# Create blank image of correct size and background

# Add icon to bottom left
 # Image in grayscale, invert for black cards
 # Located in sets/SETNAME/icon.png
 # Default set is Misc, which uses CustomizedAgainstHumanity icon

# Parse card text
 # Single underscore expands intelligently?

# If needed, add "pick 2" or "draw 2, pick 3" indicator
 # Bottom right, black cards only, based on number of underscores

# Add text to card
 # Font and size 16

## BACK OF CARD
# Create blank white card

# Parse card text
 # Three lines

# Add text to card
 # Font and size ??

# Invert card to get black cardback

## CREATE
# Create card function
 # createCardFront(name, string, white/black, set="Misc")
  # saves as sets/SETNAME/NAME.png

 # createCardBack(string, set="Misc")
  # saves as sets/SETNAME/cardbackWHITE.png and cardnameBLACK.png
  # run once
