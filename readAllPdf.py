import glob,json
import pprint
import PyPDF2
mylist = [file for file in glob.glob("StoreFile/*.pdf")]
for getFileName in mylist:
    fileName = getFileName.split("StoreFile\\")[1]
data = [PyPDF2.PdfFileReader(getListOfFile) for getListOfFile in mylist]
AlljsonHere = list()
matchWord = ["Packing Slip","INVOICE","others","Invoice","nvoice Number","Purchase Order","Receipt","Ridaro Inc."]
for reader in data:
    number_of_pages = len(reader.pages)
    page = reader.pages
    for pages in page:
        text = pages.extract_text()
        convertIntoList = text.split('\n')
        for matchListKeyword in matchWord:
            if matchListKeyword in convertIntoList:
                AlljsonHere.append({"File Name":fileName,"Pdf Type":matchListKeyword,"Data":convertIntoList})
pprint.pprint(AlljsonHere)
with open("samples.json","w")as file:
    js = json.dumps(AlljsonHere)
    StoreRecords = file.write(js)