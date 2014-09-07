CheapAmateurHumor
=========================

Generate custom cards that can be professionally printed to be compatible with your [Cards Againts Humanity (CAH)](http://cardsagainsthumanity.com) deck.

Cards will be designed for use with [printerstudio.com](http://www.printerstudio.com/make-your-own-custom-cards.aspx).  I have no affiliation whatsoever with printerstudio.com.  Card designs may be suitable for use with other printing companies, however they may require adjustments in design to meet the printer's specifications.

#Instructions

##Setup

This code is written in python 2.7 and uses the [Python Image Library (PIL)](http://www.pythonware.com/products/pil/).

##Custom Cards

The goal of this project is to create sets of custom card files for use with a professional printer.  Cards should be the same size, texture, and approximate look of the offical CAH sets.  According to the creative commons license you CAN use this program to create a copy of the official base game and expansions, however you cannot sell it.  I highly recommend that you purchase the offical sets from the [Cards Against Humanity Store](https://store.cardsagainsthumanity.com/) in order to support the game creators.  It will also be significantly cheaper than customizing the full set of cards.  This custom card program is for creating replacement cards or custom sets that fit well with the official game. 

Here is an explanation of the python files and what they do.

* cah.py - A guided walkthrough of how to create, import, or edit sets.

* card.py - Single custom (or replacement) cards can be created using command line arguments or stepping through the script.  Cards will be placed into the misc set unless otherwise specified.

* cahlib.py - Library containing the core functionality to design and create cards.

* cahset.py - The set class.

Future Projects

* convertPDF.py - This program will attempt to convert official PDFs provided by Cards Against Humanity under the CC and convert them into card sets.  This is useful for obtaining replacement cards from the base game, house of cards pack, or any PDF sets released in the future.

* cahweb - A python server and web front end for a GUI.  Users can use the website to set card text, card color, card icon (either upload a valid file or choose from a list of exisiting icons), pick template, and card back design.  There will be a button that sends the information form to the server, which will then generate a card and display a preview of the card on the front end.  The user can then download the card files to be printed.  This web front end may also serve as a set-based (rather than single card) interface and/or may simply save the files to the server, acting as a remote way to create/edit cards.

##Printer Instructions

Printer Instructions based on [this tumblr post](http://nerdsagainsthumanity.tumblr.com/post/77456664166/how-to-get-a-shit-ton-more-blank-cards-for-cards).  More targeted instructions will be available in the future.

##Card Creation Tips and Tricks

* White cards are words and phrases that are almost always nouns (person, place, thing, idea) or gerunds (the -ing form of a verb, for example, "reading a book").

* Black cards are almost always questions or fill-in-the-blank statements.

* Use a single '_' to designate a blank.  The program will intelligently expand that underscore to a valid size.

* Don't use an 'a' or 'an' right before a blank on a black card.  Any instance of 'a' or 'an' will be part of the white card.

* Black cards come in three main types.  Most cards have no indicator and are simply "play 1" cards.  Some cards require a pair of cards and have a "Pick 2" indicator in the bottom right.  Finally there a few cards that are require the player to first draw 2 cards, and then choose a set of 3 cards to play.  These cards have a "Draw 2 Pick 3" indicator.

* Draw 2 Pick 3 cards are very rare and can be difficult to design for play.  Create these cards sparingly and only in special situations.  There are only 2 in the base game!



#Licensing, Attribution, and Sources

All code in this repository is under the MIT 2.0 License.  See the included [LICENSE file](LICENSE) for more information.


I have no affiliation with Cards Against Humanity.  Their cards are under a Creative Commons license.  From the Cards Against Humanity FAQ: 

>Cards Against Humanity is available under a [BY-NC-SA 2.0 Creative Commons license](https://creativecommons.org/licenses/by-nc-sa/2.0/). That means you can use our content to make whatever, but you have to give us credit, you can’t profit from the use of our content (this means ad revenue is not allowed), and you have to share whatever you make in the same way we share it (this means you can’t submit our content to any app store). We own the name "Cards Against Humanity," so you have to call your crappy thing something else.

The base game of CAH PDF is available for free under a Creative Commons license.  See [here](http://cardsagainsthumanity.com/#download) for more info or to download the UK/Canadian versions.

The House of Cards Pack PDF is available for free, although no license is listed.  It is assumed that it falls under the same Creative Commons license as the rest of Cards Against Humanity.  See [here](http://houseofcardsagainsthumanity.com/) for more info.
