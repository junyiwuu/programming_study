# A placeholder skeleton  module - to be fleshed out in class

def read(filename):
    """ Ignore the file, just return any sequence """
    return "AMINOACIDSEQUENCE"


# the test code below only runs when the module is not imported, but 
# runs as a stand-alone python program by typing on the command line
# python fastaio.py
if __name__=="__main__":
    if read("testfile.fas") != "AMINOACIDSEQUENCE":
        print("Error!")
    else:
        print("Test passed")



def readFasta(fname):
    FASTA=open(fname, "r")
    header=FASTA.readline()
    protein="" # build up the sequence here
    for ll in FASTA:
        protein+=ll.rstrip() # remove trailing '\n'
    FASTA.close()
    # Done. This is just    pretty-printing
    (code, name)= header.split('|')
    data = {'name': name,
            'code': code,
            'seq' : protein}
    return data
