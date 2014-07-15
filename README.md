CustomizedAgainstHumanity
=========================

Convert Official CAH PDFs and/or generate custom CAH cards that can be professionally printed to be compatible with your deck.

Cards will be designed for use with [printerstudio.com](http://www.printerstudio.com/make-your-own-custom-cards.aspx).  I have no affiliation whatsoever with printerstudio.com.  Card designs may be suitable for use with other companies, however they may require adjustments in design to meet the printer's specifications.

=Instructions=

==Custom Cards==

The core program will create sets of custom card templates for use with a professional printer.  The goal is to create cards that are the same size, texture, and approximate look of the offical CAH sets.  According to the creative commons license you CAN use this program to create a copy of the official base game and expansions, however you cannot sell it.  I highly recommend that you purchase the offical sets from the [Cards Against Humanity Store](https://store.cardsagainsthumanity.com/) in order to support the game creators.  It will also be significantly cheaper than customizing the full set of cards.  This custom card program is for creating replacement cards or custom sets that fit well with the official game. 

The cah.py program will be able to create custom sets in a number of ways:

* Single custom (or replacement) cards can be created using command line arguments.  Single cards will use the Customized Against Humanity card back, the Customized Against Humanity icon, and will take in the card color and text from command line arguments.  An option may be available in the future to use the standard CAH back after I determine the legality of it.  These cards will be placed into the Misc. set.

* Custom expansions can be created by designating a file with the proper format.  The file will contain information on the card back, card icon, and then will contains a list of black and white card texts.  A set folder will be created and card templates will be added to this folder.

* In conjuction with the convertPDF.py program to create a set of cards from creative commons PDFs released by CAH.  This is useful for obtaining replacement cards from the base game, house of cards pack, or any PDF sets released in the future.

==Convert an offical PDF==

CAH has currently released the base game and the House of Cards Pack available as PDFs full of square cards.  These two PDFs are available online and are included in the [/CAH PDFs/](CAH PDFS/) folder.

The convert.py program attempts to take in a pdf, convert the squares into card templates that can be sent to a professional printer for printing.  These PDFs typically have rules or an introduction section before the cards begin, so it is advisable to look through the resulting set of cards to remove any card templates created from the introduction section.

Eventual usage will be as follows:

    python convert.py nameofPDF.pdf "Set Name Here"

The program will take a .pdf file found in the same folder and convert the squares into card templates.  These templates will be placed in a folder located inside the [sets/](sets/) folder.

==Printer Instructions==

Printer Instructions based on [this tumblr post](http://nerdsagainsthumanity.tumblr.com/post/77456664166/how-to-get-a-shit-ton-more-blank-cards-for-cards).  More targeted instructions will be available in the future.



=Licensing and Attribution=

All code in this repository is under the MIT 2.0 License.  See the included [LICENSE file](LICENSE) for more information.


From the Cards Against Humanity FAQ: "Cards Against Humanity is available under a [BY-NC-SA 2.0 Creative Commons license](https://creativecommons.org/licenses/by-nc-sa/2.0/). That means you can use our content to make whatever, but you have to give us credit, you can’t profit from the use of our content (this means ad revenue is not allowed), and you have to share whatever you make in the same way we share it (this means you can’t submit our content to any app store). We own the name "Cards Against Humanity," so you have to call your crappy thing something else."
