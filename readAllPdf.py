import glob,json
import pprint
import PyPDF2,os
import re
def partial(lst, query):
    pattern = '.*' + query + '.*'
    return [x for x in lst if re.match(pattern, x)]
filePath = os.getcwd()
newpath = filePath +"/"+"Json File"

try:
    print(os.path.exists(os.path.join(os.getcwd(),'Json File')))
    if not os.path.exists(os.path.join(os.getcwd(),'Json File')):
        os.makedirs(os.path.join(os.getcwd(),'Json File'))
except Exception as e:
    print(e)
mylist = [file for file in glob.glob("StoreFile/*.pdf")]
data = [PyPDF2.PdfFileReader(getListOfFile) for getListOfFile in mylist]
matchWord = ["Packing Slip","invoice","Purchase Order","Receipt","invoice number"]

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
            try:
                text = pages.extract_text().lower()
                print(text)
                convertIntoList = text.split('\n')

                convertIntoList_filtrd = []
                convertIntoList_filtrd_real = []
                for txtt in convertIntoList:
                    convertIntoList_filtrd.append(txtt.replace('\xa0',' ').lower().strip())
                    convertIntoList_filtrd_real.append(txtt.replace('\xa0', ' ').strip())
                print(convertIntoList_filtrd)
                Others = "Others"
                flName = next(iterData)
                for matchListKeyword in matchWord:
                    if partial(convertIntoList_filtrd , matchListKeyword):
                        Others = matchListKeyword
                AlljsonHere.append(
                    {"FileName": flName, "Pdf Type": Others, "Data": convertIntoList_filtrd_real})

            except Exception as e:
                print(e)
    return AlljsonHere

datas = readData()
for i in datas:
    GetFileName = i.get("FileName").lower()
    convertFileType = GetFileName.replace("pdf","json")
    ConvertIntoString = json.dumps(i)
    try:
        with open(f"Json File/ {convertFileType}","w+") as file:
            store = file.write(ConvertIntoString)
    except Exception as e:
        print(e)


 