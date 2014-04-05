__author__ = 'obscure'
import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

myroot = 'Anonymity'


def pdfparser():
    global myroot
    for root, subFolders, files in os.walk(myroot):
        for filename in files:
            if filename.endswith('.pdf'):
                fp = open(os.path.join(root, filename), 'rb')
                parser = PDFParser(fp)
                document = PDFDocument(parser)
                if not document.is_extractable:
                    print 'Oops'
                    raise PDFTextExtractionNotAllowed
                rsrcmgr = PDFResourceManager()
                # Create a PDF device object.
                device = PDFDevice(rsrcmgr)
                # Create a PDF interpreter object.
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                # Process each page contained in the document.
                text_content = []
                for page in PDFPage.create_pages(document):
                    print type(page)
                    interpreter.process_page(page)
                    layout = device.get_result()
                break
            else:
                print filename


print 'Hello'
pdfparser()


