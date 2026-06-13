from PyPDF2 import PdfReader
def read_pdf(file_path):
    reader=PdfReader(file_path)
    return reader.pages
