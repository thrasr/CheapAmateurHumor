CustomizedAgainstHumanity
=========================

Generate custom [Cards Againts Humanity (CAH)](http://cardsagainsthumanity.com) cards that can be professionally printed to be compatible with your deck.

Cards will be designed for use with [printerstudio.com](http://www.printerstudio.com/make-your-own-custom-cards.aspx).  I have no affiliation whatsoever with printerstudio.com.  Card designs may be suitable for use with other companies, however they may require adjustments in design to meet the printer's specifications.

#Instructions

##Setup

This code is written in python 2.7 and uses the [Python Reddit Api Wrapper](https://praw.readthedocs.org/) library.  There are instructions to install this library on their page.

##Custom Cards

The core program will create sets of custom card templates for use with a professional printer.  The goal is to create cards that are the same size, texture, and approximate look of the offical CAH sets.  According to the creative commons license you CAN use this program to create a copy of the official base game and expansions, however you cannot sell it.  I highly recommend that you purchase the offical sets from the [Cards Against Humanity Store](https://store.cardsagainsthumanity.com/) in order to support the game creators.  It will also be significantly cheaper than customizing the full set of cards.  This custom card program is for creating replacement cards or custom sets that fit well with the official game. 

The core program is cah.py and will be a library to create card templates.

There will also be a couple of small scripts that use the cah.py library to create cards.

* card.py - Single custom (or replacement) cards can be created using command line arguments or stepping through the script.  Cards will be placed into the Misc set unless otherwise specified.

* set.py - Custom expansion sets can be created with by using a file with the proper format or stepping through the script.  The file will contain information on the set name, card back, set icon, and then will contain a list of black and white card texts.  A set folder will be created and card templates will be added to this folder.

* convertPDF.py - This program will attempt to convert official PDFs provided by Cards Against Humanity under the CC and convert them into card sets.  This is useful for obtaining replacement cards from the base game, house of cards pack, or any PDF sets released in the future.


##Printer Instructions

Printer Instructions based on [this tumblr post](http://nerdsagainsthumanity.tumblr.com/post/77456664166/how-to-get-a-shit-ton-more-blank-cards-for-cards).  More targeted instructions will be available in the future.


#Licensing and Attribution

All code in this repository is under the MIT 2.0 License.  See the included [LICENSE file](LICENSE) for more information.


I have no affiliation with Cards Agains Humanity.  Their cards are under a Creative Commons license.  From the Cards Against Humanity FAQ: 

>Cards Against Humanity is available under a [BY-NC-SA 2.0 Creative Commons license](https://creativecommons.org/licenses/by-nc-sa/2.0/). That means you can use our content to make whatever, but you have to give us credit, you can’t profit from the use of our content (this means ad revenue is not allowed), and you have to share whatever you make in the same way we share it (this means you can’t submit our content to any app store). We own the name "Cards Against Humanity," so you have to call your crappy thing something else.


There will be font files included in the future that will be available for personal use.  A more accurate description and a source link will be added when the font file is uploaded.
