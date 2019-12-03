class Input:
    def __init__(self,site,name,transcript,snippetRefers,alteration,alterName,protein,position,AA1,AA2):
        self.site = site
        self.name = name
        self.transcript = transcript
        self.snippetRefers = snippetRefers
        self.alteration = alteration
        self.alterName = alterName
        self.protein = protein
        self.position = position
        self.AA1 = AA1
        self.AA2 = AA2

    def create_post(self):
        if self.site == "mutationtaster" :
            values = {"transcript" : self.transcript,
                      "snippetRefers" : self.snippetRefers,
                      "alteration": self.alteration,
                      "alterName": self.alterName,
                      }

        if self.site == "polyphen":
            values = {"protein": self.protein,
                      "position" : self.position,
                      "AA1" : self.AA1,
                      "AA2" : self.AA2,
                      }

        return values
