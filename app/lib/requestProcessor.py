'''
Created on May 20, 2014

@author: PengAn
'''
from app.lib import pdfMinerHelper, pyPdfHelper
from flask import render_template
import urllib2
from flask import Response

def parseRequest(request,fileStream):
    parserChoice = request.form['parser']
    if parserChoice == 'html':
        resultHtml = pdfMinerHelper.toHTML(fileStream)
        return resultHtml
    if parserChoice == 'text':
        resultText = pdfMinerHelper.toText(fileStream)
        return render_template("result.html",result=resultText)
    if parserChoice == 'minerxml':
        resultXML = pdfMinerHelper.toXML(fileStream)
        return Response(resultXML, mimetype='text/xml')
    if parserChoice == 'xpdf':
        resultXML = requestPDFX(fileStream)
        return Response(resultXML, mimetype='text/xml')
    if parserChoice == 'pypdf2text':
        resultText = pyPdfHelper.getPDFContent(fileStream)
        return render_template("result.html",result=resultText)

def requestPDFX(fileStream):
    pdfdata = fileStream.read()
    request = urllib2.Request('http://pdfx.cs.man.ac.uk', pdfdata, headers={'Content-Type' : 'application/pdf'})
    resultXML = urllib2.urlopen(request).read()
    return resultXML

def parseRequestWithLocalPath(request,filepath):
    fileStream = file(filepath, 'rb')
    return parseRequest(request, fileStream)
    