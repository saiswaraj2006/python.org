# compressor.py
from PyPDF2 import PdfWriter

def compress_pdf(pages, out_path):
    writer = PdfWriter()
    for page in pages:
        writer.add_page(page)
    # Example: remove metadata for smaller size
    writer.remove_metadata()
    with open(out_path, "wb") as f:  
        writer.write(f)
