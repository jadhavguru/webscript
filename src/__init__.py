import PyPDF2
import  re




filename = "Regex Test Data(1).pdf"


pdfFileObj = open(filename,'rb')


pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages
count = 0
text = ""

#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

pattern = re.compile(r'([0-9]|10|11|12)[:.][0-5][0-9]\s?(AM|PM|am|pm)')
matches_time = pattern.finditer(text)
for match in matches_time:
        print(match)
print("#########################################")
mobile_pattern=re.compile(r'(\(?\+?\s?(91)?\s?\))?\s?\d{10}')
text4 = mobile_pattern.finditer(text)
for i in text4:
    print(i)
print("#########################################")
pattern2 = re.compile(r'(\(?\s?\d{3}\s?\)?)?\s?\d{5}')
matches = pattern2.finditer(text)
for match in matches:
    print(match)
print("#########################################")
pattern3=re.compile(r'[0-1-2][0-9]:([0-5]\d?)(:([0-5]\d))?(\.[0-5]\d)?')
matches=pattern3.finditer(text)
for i in matches:
    print(i)
print("#########################################")
pattern4 = re.compile(r'(\$?\s?\d+(\,)?\d*\.\d+\s?(dollars))|(\$\s?\d+(\,)?\d*\.\d+\s?(dollars)?)')
matches = pattern4.finditer(text)
for match in matches:
    print(match)
print("#########################################")
pattern5 = re.compile(r'(http(s)?://)?www\.[a-zA-z0-9.-]+\.[a-zA-z0-9.-]*')
matches = pattern5.finditer(text)
for match in matches:
    print(match)
print("###############################################")
pattern6=re.compile(r"([^a-zA-Z]\d{1,4}[/.-]\d+[/\.\-]\d{1,4}|\n?\s*[A-Z][a-z]*\s?\d{1,32}\s*,\s*\d{4}|\s*\d+\s?[A-Z][a-z]*\s*,\d{4})")
matches=pattern6.finditer(text)
for match in matches:
    print(match)

print("##################################")
name_pattern=re.compile( r'((Mr|mr|Shr|shr|Dr|dr|prof|Prof)[.]?|([A-Z][.]?(\ )?[a-z]*))\ ?(([A-Z][.]?\ ?[a-z]*)?\ ?([A-Z][.]?\ ?[a-z]*?)? ([A-Z][a-z]*)?)')

text10 = name_pattern.finditer(text)

for i in text10:
    print(i)
print("##################################")
pattern=re.compile(r'[a-zA-Z0-9_.-]+\s?(\[\s?at\s?\]|\[\s?AT\s?\]|\(\s?AT\s?\)|\(\s?at\s?\))\s?([a-z\sA-Z0-9-]+\s?(\(\s?DOT\s?\)|\(\s?dot\s?\)|\.|\[\s?dot\s?\]|\[\s?DOT\s?\]))+\s?(edu|in|In)')
matches=pattern.finditer(text)
for match in matches:
    print(match)

