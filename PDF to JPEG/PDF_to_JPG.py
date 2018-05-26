# coding=utf-8
# Extract jpg's from pdf's. 
# Code upgraded from https://nedbatchelder.com/blog/200712/extracting_jpgs_from_pdfs.html
# Input file -- PDF
# Output file -- multiple images (jpg0, jpg1, ..., jpg(n-1) where n is the number of pages in the PDF)

import sys

# Open and read PDF file in binary mode
with open("Link/To/PDF/File.pdf", "rb") as file:
    pdf = file.read()

# Declare variables to use, including start and end marks  
startmark = b"\xff\xd8"
startfix = 0
endmark = b"\xff\xd9"
endfix = 2
i = 0
njpg = 0

while True:
    istream = pdf.find(b"stream", i)
    if istream < 0:
        break
    istart = pdf.find(startmark, istream, istream + 20)
    if istart < 0:
        i = istream + 20
        continue
    iend = pdf.find(b"endstream", istart)
    if iend < 0:
        raise Exception("Didn't find end of stream!")
    iend = pdf.find(endmark, iend - 20)
    if iend < 0:
        raise Exception("Didn't find end of JPG!")

    istart += startfix
    iend += endfix

    print("JPG %d from %d to %d" % (njpg, istart, iend))
    jpg = pdf[istart:iend]

    #Save as image
    with open("jpg%d.jpg" % njpg, "wb") as jpgfile:
        jpgfile.write(jpg)

    #Update image number
    njpg += 1
    i = iend