from file_reader import read_pdf
from Compressor import compress_pdf
import os

def main():
    input_file = "C:/Users/saisw/OneDrive/Desktop/python_practice/PDF_compressor/samples.pdf"
    output_file = "C:/Users/saisw/OneDrive/Desktop/python_practice/PDF_compressor/compressed.pdf"

    if not os.path.exists(input_file):
        print("File not found:", input_file)
        return

    pages = read_pdf(input_file)
    compress_pdf(pages, output_file)
    print("Compression complete!")

if __name__ == "__main__":
    main()


