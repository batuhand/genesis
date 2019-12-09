class Send:
    def __init__(self,name, site, values, output):
        self.name = name
        self.site = site
        self.values = values




def read_input():
    f = open("input.txt", "r")
    file = f.readlines()
    for i in file:
        values = i.split(":")
        print(values)
        if values[0] == "to":
            site = values[1]

        elif values[0] == "name":
            name = values[1]

        #elif values[0] == "transcript":
            #values["transcript_stable_id_text"] = values[1]

        print(i)


read_input()



"""  
    #---------------- MuTaster
post_values = {"gene": args[0],
                   "transcript_stable_id_text": args[1],
                   "sequence_type": args[2],
                   "sequence_snippet": args[3],
                   "position_be": args[4],
                   "new_base": args[5],
                   "start_insdel": args[6],
                   "end_insdel": args[7],
                   "bases_inserted": args[8]}
                   
                   """


"""------------------ Polyphen
  
    post_values = {
        "_ggi_project" : "PPHWeb2", 
        "_ggi_origin": "query",
        "_ggi_target_submit": "submit",
        "accid" : args[0],
        "seqres": args[1],
        "seqpos" : args[2],
        "seqvar1" : args[3],
        "seqvar2" : args[4],
        #"description":args[5]
    }
    """