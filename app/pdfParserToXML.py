'''
Created on May 8, 2014

@author: PengAn
'''
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import HTMLConverter,TextConverter
from pdfminer.layout import LAParams
from cStringIO import StringIO
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

def parsePDFtoXML(filepath):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = HTMLConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    fp = file(filepath, 'rb')
    parser = PDFParser(fp)
    
    for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
    fp.close()
   
    device.close()

    str = retstr.getvalue()
    retstr.close()
    return str.decode('utf-8')
