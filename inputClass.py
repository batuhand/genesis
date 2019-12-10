class Input:
    transcript = ""
    snippetrefers = ""
    firstwildtype = ""
    lastwildtype = ""
    protein = ""
    position = ""
    aa1 = ""
    aa2 = ""
    alteration = ""
    nameofalteration = ""
    gene = ""
    insertedbase = ""
    newbase = ""

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


""" 
def __init__(self,transcript,snippetRefers,alteration,alterName,protein,position,AA1,AA2):
     self.transcript = transcript
     self.snippetRefers = snippetRefers
     self.alteration = alteration
     self.alterName = alterName
     self.protein = protein
     self.position = position
     self.AA1 = AA1
     self.AA2 = AA2
"""