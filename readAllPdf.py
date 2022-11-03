import glob,json
import pprint
import PyPDF2,os

filePath = os.getcwd()
newpath = filePath +"/"+"Json File"
os.makedirs(newpath)
if not os.path.exists(filePath):
    os.makedirs(newpath)
mylist = [file for file in glob.glob("StoreFile/*.pdf")]
data = [PyPDF2.PdfFileReader(getListOfFile) for getListOfFile in mylist]
matchWord = ["Packing Slip","INVOICE","PUBLIC TELEPHONE COMPANY","Purchase Order","Receipt","invoice number"]

def FileNames():
	store = [getFileName.split("StoreFile\\")[1] for getFileName in mylist]
	for i in store:
		yield i

iterData = iter(FileNames())
def readData():
    AlljsonHere = list()
    for reader in data: 
        page = reader.pages
        for pages in page:
            text = pages.extract_text().lower()
            convertIntoList = text.split('\n')
            for matchListKeyword in matchWord:
                if matchListKeyword.lower() in convertIntoList:
                    flName = next(iterData)
                    AlljsonHere.append({"FileName":flName,"Pdf Type":matchListKeyword,"Data":convertIntoList})
    return AlljsonHere

datas = readData()
for i in datas:
    GetFileName = i.get("FileName").lower()
    convertFileType = GetFileName.replace("pdf","json")
    ConvertIntoString = json.dumps(i)
    with open(f"Json File/ {convertFileType}","w+") as file:
        store = file.write(ConvertIntoString)


 