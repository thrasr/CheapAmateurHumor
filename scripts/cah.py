import CAHset
import sys

miscset = CAHset.CAHset('misc')


# Command line Argument USAGE
# python cah.py black/white "This is the card text"
if len(sys.argv) == 3:
    if sys.argv[1][0].lower() == 'b':
        miscset.addblackcard(sys.argv[2])
        cardname = 'b' + str(len(miscset.blackcards)-1) + '.png'
    elif sys.argv[1][0].lower() == 'w':
        miscset.addwhitecard(sys.argv[2])
        cardname = 'w' + str(len(miscset.whitecards)-1) + '.png'
    else:
        print 'USAGE: python ' + sys.argv[0] + ' [black|white] "This is the card text"'
        sys.exit(0)

    miscset.create()
    print "Card created!  Look for '" + cardname + "' in the misc set."

else:
    print "Welcome to the card creation process."
    print "This will create a card and add it to the misc set."
    print "Type 'exit' to leave the program at any time."

    while True:
        color = raw_input("Is this a black or a white card?\n> ")
        if color.lower() == "exit" or color.lower() == 'quit':
            sys.exit(0)
        elif not (color[0].lower() == 'b' or color[0].lower() == 'w'):
            print "Error - please choose black or white for the color\n\n"
            continue
        
        text = raw_input("Please type the text to be printed on the card\n> ")
        if text.lower() == "exit" or text.lower() == 'quit':
            sys.exit(0)

        print
        if color[0].lower() == 'b':
            print "You want to create a BLACK card with the text:"
        else:
            print "You want to create a WHITE card with the text:"

        print '"' + text + '"'

        verify = raw_input("If this is correct, type yes.  If this is not correct, type no to remake it.\n> ")
        if verify.lower() == "exit" or verify.lower() == 'quit':
            sys.exit(0)
        elif verify[0].lower() == 'y':
            # create card
            if color[0].lower() == 'b':
                miscset.addblackcard(text)
                cardname = 'b' + str(len(miscset.blackcards)-1) + '.png'
            elif color[0].lower() == 'w':
                miscset.addwhitecard(text)
                cardname = 'w' + str(len(miscset.whitecards)-1) + '.png'

            miscset.create()
            print "Card created!"
            print "Look for '" + cardname + "' in the misc set!\n"
            print "Now creating a new card - type 'exit' at anytime to quit."
        else:
            print "Card not created.\n\n"
            continue
