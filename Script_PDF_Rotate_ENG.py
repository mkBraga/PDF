#################################################################     Rotation    ###################################################################
#                               
#           INSTAL:             
#           Activate:                             
#           DEFINITION:             
#           DOCUMENTATION:      
#              
#####################################################################################################################################################

#Works for just one page

import PyPDF2


#PDf to be changed
with open('./watermarked_output.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)

    #identifies the first page, you can choose the one you want
    page = reader.getPage(0)
    
    #rotate the page
    page.rotateCounterClockwise(90)

    writer = PyPDF2.PdfFileWriter()
    
    #insert the round page
    writer.addPage(page)

    #To Save edited file
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

        