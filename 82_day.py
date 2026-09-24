
# Exercise 8 - Merge the Pdf Solution in Python

from PyPDF2 import PdfMerger
import os

merger = PdfMerger()
file=[file for file in os.listdir() if file.endswith('.pdf')]

for f in file:
    merger.append(f)

merger.write("merged.pdf")
merger.close()
