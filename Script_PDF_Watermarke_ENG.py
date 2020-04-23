#################################################################     Watermarker    ###################################################################
#                               
#           INSTAL:             
#           Activate:                             
#           DEFINITION:             
#           DOCUMENTATION:      
#              
##################################################################################################################################################

import PyPDF2


#PDF we want to insert watermark
template = PyPDF2.PdfFileReader(open('./PDF/SuperPDF.pdf' , 'rb'))

#PDF watermark
watermark = PyPDF2.PdfFileReader(open('./PDF/wtr.pdf' , 'rb'))


output = PyPDF2.PdfFileWriter()

#To run on all pages, and as we don't know how many pages we have, we make the range
for i in range(template.getNumPages()):
    #save all Pages
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))

    #save page
    output.addPage(page)

    #Create the document with the name / destination you want
    with open('watermarked_output.pdf' , 'wb') as file:
        output.write(file)


