'''
Created on May 15, 2014

@author: PengAn
'''
from PyPDF2 import PdfFileReader
 
def getPDFContent(fileStream):
    content = ""
    # Load PDF into pyPDF
    pdf = PdfFileReader(fileStream)
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "[page"+str(i+1)+"]"
    # Collapse whitespace
    #content = " ".join(content.replace(u"/xa0", " ").strip().split())
    fileStream.close()
    return content