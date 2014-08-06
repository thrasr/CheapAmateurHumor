# Rory Thrasher, 2014



class cah_set:
    punctuation = [',', '.', ';', ':', '!', '?', '/', '(', ')']
    pick2 = '../resources/pick2.png'
    pick3 = '../resources/pick3.png'
    defaulticon = '../sets/misc/assets/icon.png'
    
    def init(self, vars):
        #python does inits weird...
        if size(vars) = 4:
            self.scratch(vars[0], vars[1], vars[2], vars[3])
        elif size(vars) = 1:
            self.import(vars[0])
        else:
            print "ERROR: INVALID SET INITIALIZATION"
            print "SET IS EMPTY AND NOT USABLE"
    
    def scratch(self, setname, backline1, backline2, backline3):
        # initialize new set
        self.name=setname
        self.back1 = backline1
        self.back2 = backline2
        self.back3 = backline3
        self.blackcards = {}
        self.whitecards = {}
        self.icon = seticon
        self.numbered=false
        self.numberedinset=false

        # create folder structure
        
        self.export()


    def import(self, d):
        # initialize from XML/JSON dictionary
        # import file and convert elsewhere?
        # change parameter to file name or file object?
        self.name = d.name
        self.back1 = d.back1
        self.back2 = d.back2
        self.back3 = d.back3
        self.numbered=d.numbered
        self.numberedinset=d.numberedinset
        self.blackcards = d.blackcards
        self.whitecards = d.whitecards
        self.icon = seticon

        # create folder if need be
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
        
        #convert to XML or JSON
        #write to '../sets/' + self.name + '/assets/' + self.name + '.xml'
        
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
        # Create card images for all cards
        # Assumes icon is in folder if there is one
        pass
        
        # Create card backs (black and white)
        cahlib.createback(self.name, self.back1, self.back2, self.back3)
        
        # Create cards
        for card in whitecards:
            cahlib.createwhitecard(self.name, card)
        for card in blackcards:
            cahlib.createblackcard(self.name, card)
            
        # Future functionality: Numbered cards (1, 2, 3...) and Number in set (1/27, 2/27, 3/27...)
        
        
