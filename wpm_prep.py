import os
import slate3k

def wpm():
    #Open text file containing part of file that the user wants to read.
    file = open("wpm.txt",'r')
    text = file.read()
    file.close()

    #Split the text while preserving formatting
    text = text.split(' ')

    #Mark every 150 words
    for i,x in enumerate(text):
        if i%149 == 0 and i > 0:
            text.insert(i-1,"\n\n##150Words##\n\n") #150 wpm seperator token

    #Join text together with spaces
    text = ' '.join(text)

    #Save formatter file to text
    text_file = open("output.txt", "w")
    text_file.write(text)
    text_file.close()

def processPdf(name):
    with open(name,'rb') as f:
        extracted_text = slate3k.PDF(f)

    page_file = open("page.txt",'r')
    page = int(page_file.read())
    page_file.close()

    #Write the extracted text to a file
    text_file = open("wpm.txt", "w")
    text = extracted_text

    for x in text:
        text_file.write(x)

    text_file.close()

    wpm()
    f.close()

processPdf("Chapter11.pdf")
