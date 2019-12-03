#-----------------------------------------------Mutation Taster----------------------------------------------------------

def send_all_data_mutation(args: tuple) -> None:

    url = "http://www.mutationtaster.org/cgi-bin/MutationTaster/MutationTaster69.cgi"

    post_values = {
        "gene": args[0],
        "transcript_stable_id_text": args[1],
        "sequence_type": args[2],
        "sequence_snippet": args[3],
        "position_be": args[4],
        "new_base": args[5],
        "start_insdel": args[6],
        "end_insdel": args[7],
        "bases_inserted": args[8]
    }

    response = get_response(url, post_values)
    return response.text

def get_values_mutation(args: tuple) -> str:

    html = send_all_data_mutation(args)
    return html

#-------------------------------------polyphen-----------------------------------------------------------------------------------------------

def send_all_data_polyphen(args: tuple) -> None:

    url = "http://genetics.bwh.harvard.edu/cgi-bin/ggi/ggi2.cgi"

    post_values = {
        "_ggi_project": "PPHWeb2",
        "_ggi_origin": "query",
        "_ggi_target_submit": "submit",
        "accid": args[0],
        "seqres": args[1],
        "seqpos": args[2],
        "seqvar1": args[3],
        "seqvar2": args[4],
    }

    response = get_response(url, post_values)
    return response.text

def get_values_poly(args: tuple) -> str:

    html = send_all_data_polyphen(args)
    return html


#----------------------------------------------------------------POST-----------------------------------------------------------

def get_response(url, kwords):
    import requests

    response = requests.post(url, data=kwords, verify=False)
    return response

#------------------main-----------------------------------------------------------------------------------------------------------

data_example_mutationT = ("", "ENST00000379370", "gDNA", "", "" , "", "28669", "28672", "")
data_example_polyphenT = ("P41567", '', '59', 'L', 'P', '')

print("\n Mutation Taster  ---------------------------------------------------------------------------------- \n" , get_values_mutation(data_example_mutationT))
print("\n polyphen  ---------------------------------------------------------------------------------- \n" , get_values_poly(data_example_polyphenT))