# Rory Thrasher, 2014
import cahlib.py
import json
import os

class cah_set:
    def init(self, vars):
        #python does inits weird...
        if size(vars) = 4:
            self.scratch(vars[0], vars[1], vars[2], vars[3])
        elif size(vars) = 1:
            self.importset(vars[0])
        else:
            print "ERROR: INVALID SET INITIALIZATION"
            print "SET IS EMPTY AND NOT USABLE"
    
    def scratch(self, setname, backline1, backline2, backline3):
        # initialize new set
        self.name = setname
        self.back1 = backline1
        self.back2 = backline2
        self.back3 = backline3
        self.blackcards = {}
        self.whitecards = {}

        # For possible future functionality
        self.numbered = false
        self.numberedinset = false

        # Setup folders and do first export
        self.foldersetup()
        self.export()
        
    def importset(self, setname):
        # Create file structure
        self.foldersetup()

        # Read json file
        try:
            f = open('../imports/' + setname + '/assets/' + setname + '.json', 'r')
            d = json.loads(f.read())
        except:
            print "UNABLE TO FIND/READ FILE: ../imports/" + setname + ".json"
            print "SET NOT IMPORTED - ATTEMPT MANUAL SETUP"
            return

        try:
            if os.path.exists("../import/" + self.name + "icon.png")
        except:
            print "No custom icon found for set " + self.name
            print "Set will use default icon"

        # Initialize from JSON dictionary
        self.name = setname
        self.back1 = d.back1
        self.back2 = d.back2
        self.back3 = d.back3
        self.blackcards = d.blackcards
        self.whitecards = d.whitecards

        # For possible future functionality
        self.numbered=d.numbered
        self.numberedinset=d.numberedinset

        # First export
        self.export()

    def export(self):
        dict = {}
        dict['name'] = self.name
        dict['back1'] = self.back1
        dict['back2'] = self.back2
        dict['back3'] = self.back3
        dict['numbered'] = self.numbered
        dict['numberedinset'] = self.numberedinset
        dict['blackcards'] = self.blackcards
        dict['whitecards'] = self.whitecards
        
        # Create JSON file
        out = json.dumps(dict)
        f = open('../sets/' + self.name + '/assets/' + self.name + '.json', 'w')
        f.write(out)

    def foldersetup(self):
        # Check if folders exist and need to be setup
        if not (os.path.exists("../sets/" + self.name) and os.path.isdir("../sets/" + self.name)):
            os.makedirs("../sets/" + self.name)
            os.makedirs("../sets/" + self.name + "/assets")
        elif os.path.exists("../sets/" + self.name) and os.path.isdir("../sets/" + self.name):
            if not (os.path.exists("../sets/" + self.name + "/assets") and os.path.isdir("../sets/" + self.name + "/assets")):
                os.makedirs("../sets/" + self.name + "/assets")

        print "File structure has been set up for set '" + self.name + "'."


    def addwhitecard(self, cardtext):
        tempcard = {}
        tempcard['name'] = 'w' + str(size(self.whitecards))
        # possibly add some sort of text validation here? if so, return false
        tempcard['text'] = cardtext
        self.whitecards[tempcard.name] = tempcard
        
        self.export()
        return true
        
    def addblackcard(self, cardtext, pickx=0):
        tempcard = {}
        tempcard['name'] = 'b' + str(size(self.blackcards))
        # possibly add some sort of text validation here? if so, return false
        if pickx>0 && pickx<4:
            tempcard['pick']=pickx
        else:
            tempcard['pick']= #number of '_' in cardtext
        tempcard['text'] = cahlib.expand(cardtext)
        self.blackcards[tempcard.name] = tempcard
        
        self.export()
        return true
        
    def create(self):
        # Create card backs (black and white)
        cahlib.createback(self.name, self.back1, self.back2, self.back3)
        
        # Create cards
        for card in whitecards:
            cahlib.createwhitecard(self.name, card)
        for card in blackcards:
            cahlib.createblackcard(self.name, card)
            
        # Future functionality: Numbered cards (1, 2, 3...) and Number in set (1/27, 2/27, 3/27...)
        
        
