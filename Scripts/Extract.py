import PyPDF2

pdfFile = open('sample.pdf', 'rb')

pdfReader = PyPDF2.pdfFileReader(pdfFile)

print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

print(pageObj.extractText())

pdfFile.close()