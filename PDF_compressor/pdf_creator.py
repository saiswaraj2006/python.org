from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, "World Records Highlights (2026)")
    c.drawString(100, 730, "Largest Marathon Ever: 59,830 finishers")
    c.drawString(100, 710, "Fastest Marathon Performance: 1h 59m 30s")
    c.save()

create_pdf(create_pdf("C:/Users/saisw/OneDrive/Desktop/python_practice/PDF_compressor/samples.pdf"))

