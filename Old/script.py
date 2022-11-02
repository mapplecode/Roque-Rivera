import PyPDF2
import tabula,json
with open("3.pdf", "rb") as pdf_file:
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.pages[0]
    page_content = page.extractText()
data = page_content
ShipToList= list()
EmptyList = list()
projectName = data
getBeforeVendor = projectName.split('Vendor')
addSplit =  getBeforeVendor[0].split("/")[0]
addSplit1 = getBeforeVendor[0].split("/")[1]
addSplit2 = getBeforeVendor[0].split("/")[2].split()[0]
addSplit3 = getBeforeVendor[0].split("/")[2].split()[1]

ProjectName = addSplit.split('#')[1].split('\n')[0]
Po = getBeforeVendor[0].split("/")[2].split()[1]

# Date.................
d = getBeforeVendor[0].split("/")[0].split()[-1]
dat = getBeforeVendor[0].split("/")[1]
Date = getBeforeVendor[0].split("/")[2].split()[0]
getDate = d+ "/" + dat+ "/" +Date

PurchageAddress = getBeforeVendor[0].split("/")[2].split()[2:]
Vendor = getBeforeVendor[1].split('Ship To')[0]

ShipTo = getBeforeVendor[1].split('Ship To')[1].split('QUOTE')[0]
Comments =  getBeforeVendor[1].split('Ship To')[1].split('QUOTE')[1].split('Comment or Special Instruction')[0]
EmptyList.append({"ProjectName":ProjectName,"Date":getDate,"Po":Po,"PurchageAddress":PurchageAddress,"Vendor":Vendor,"ShipTo":ShipTo})

df = tabula.io.read_pdf('3.pdf', pages='all')
QuoteNumerLine = df[0].items()
ItemLine =df[1].items()
OrderPriceLine = df[2].items()

ItemData =list()
QuoteData = list()
OrderDate = list()

for k in ItemLine:
    GetStoreValue = str(k[1]).split('\n')[0].split('  ')[2]
    ItemData.append({k[0]:GetStoreValue})

for k in QuoteNumerLine:
    GetStoreValue = str(k[1]).split('\n')[0].split('  ')[2]
    QuoteData.append({k[0]:GetStoreValue})

for i in OrderPriceLine:
    data = str(i[1]).split('\n')
    Tax = data[0].split()[1]
    Shipping = data[1].split()[1]
    Other = data[2].split()[1]
    Total = data[3].split()[1]
t = Tax,Shipping,Other,Total
OrderDate.append(t)
da = list()
for f in OrderDate:
    da.append({"Tax":f[0],"Shipping":f[1],"Other":f[2],"Total":f[3]})

datas = EmptyList,QuoteData,ItemData,da,


with open('samples.json','w') as file:
    fileData = json.dumps(datas)
    file.write(fileData)

with open('samples.json','w') as file:
        fileData = json.dumps(datas)
        file.write(fileData)

if __name__ == '__main__':
    print("Execute..")

