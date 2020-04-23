#################################################################     PDF Merger   ###################################################################
#                               
#           INSTAL:             pip install PyPDF2 (in cmd)
#           Activate:                             
#           DEFINITION:             
#           DOCUMENTATION:      https://pypi.org/project/PyPDF2/
#           CMD:                python3 Scpript_PDF_Merger_ENG.py dummy.pdf twopage.pf  
#                               (dummy.pdf twopage.pdf = the names of the pdfs you want to add)  
######################################################################################################################################################


import sys
import PyPDF2

inputs = sys.argv[1:]

def pdf_Combiner(pdf_list):
    
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('Super.pdf')

pdf_Combiner(inputs)
