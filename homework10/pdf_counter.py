import re


def count_pages(path):
    with open(path, 'rb') as f:
        a = f.read()

    print(len(re.findall(r'Page\W', str(a))))

if __name__=="__main__":
    count_pages("files/lesson-3.pdf")  # 34

# from PyPDF2 import PdfFileReader
#
# pdf_document = "lesson-3.pdf"
# with open(pdf_document, "rb") as filehandle:
#    pdf = PdfFileReader(filehandle)
#    info = pdf.getDocumentInfo()
#    pages = pdf.getNumPages()
#    # print (info)
#    print ("number of pages: %i" % pages)
