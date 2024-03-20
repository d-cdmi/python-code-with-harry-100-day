# day 82 main File
import os
from PyPDF2 import PdfWriter

marge = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
for pdf in files:
    marge.append(pdf)

marge.write("merged-pdf.pdf")
marge.close()