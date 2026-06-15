from PyPDF2 import PdfReader
reader=PdfReader("C:/Users/saisw/OneDrive/Desktop/python_practice/PDF_compressor/samples.pdf")
for i,page in enumerate(reader.pages):
    text=page.extract_text()
    print(f"page {i+1}:")
    print(text)