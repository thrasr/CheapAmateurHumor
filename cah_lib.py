from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

## FRONT OF CARD

# Use ../resouces/blankcard.png for base

# Add icon to bottom left
 # Image in grayscale
 # Located in ../sets/SETNAME/assets/icon.png
 # Default set is misc, which uses CustomizedAgainstHumanity icon

# Parse card text
 # Single underscore expands intelligently
 # Measure length of text?
 # Use a "text box"?

# If needed, add "pick 2" or "draw 2, pick 3" indicator
 # Bottom right, black cards only, based on number of underscores (or manual intervention)

# Add text to card
 # Font and size 16

## BACK OF CARD
# Use ../resouces/blankcard.png for base

# Parse card text
 # Three lines

# Add text to card
 # Font and size ??

# Invert card to get black cardback

## CREATE
# Create card function
 # createCardFront(name, string, white/black, set="misc")
  # saves as sets/SETNAME/NAME.png
  # Set class should provide name

 # createCardBack(line1, line2, line3, set="misc")
  # saves as sets/SETNAME/assets/wcardback.png and bcardback.png
  # runs once per set
