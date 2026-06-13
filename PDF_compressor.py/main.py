from file_reader import read_pdf
from compressor import compress_pdf

def main():
    input_file = "sample.pdf"
    output_file = "compressed.pdf"
    pages = read_pdf(input_file)
    compress_pdf(pages, output_file)
    print("Compression complete!")

if __name__ == "__main__":
    main()
