'''
Created on May 8, 2014

@author: PengAn
'''
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer import converter
from pdfminer.layout import LAParams
from cStringIO import StringIO
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

def parsePDFPorto(fileStream,OutType):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
   
    if (OutType=="HTML"):
        device = converter.HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    if (OutType=="Text"):
        device = converter.TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    if (OutType=="XML"):
        device = converter.XMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    parser = PDFParser(fileStream)
    
    for page in PDFPage.get_pages(fileStream):
            interpreter.process_page(page)
    fileStream.close()
   
    device.close()

    str = retstr.getvalue()
    retstr.close()
    return str.decode('utf-8')
def toHTML(fileStream):
    
    return parsePDFPorto(fileStream, "HTML")

def toText(fileStream):
    
    return parsePDFPorto(fileStream, "Text")

def toXML(fileStream):
    
    return parsePDFPorto(fileStream, "XML")