# day 76 main File
from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["CS06 Critical Thinking and Problem Solving.pdf", "CS07_Mathematics_in_Ancient_IndiaExploring_the_Rich_Heritage_of.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()