# pip install pypdf2

import re
import os
from collections import Counter
from PyPDF2 import PdfReader


pdf_path = os.path.join(os.path.dirname(__file__), 'sample.pdf')

def extract_text_from_pdf(pdf_file: str)-> list[str]:
    with open(pdf_file,'rb') as pdf:
        reader = PdfReader(pdf, strict=False)

        print('Pages:', len(reader.pages))
        print('-' * 10) #Divider

        pdf_text: list[str] = [page.extract_text() for page in reader.pages]
        return pdf_text
    
def count_words(text_list: list[str])-> Counter:
    all_words: list[str] = []
    for text in text_list:
          split_text: list[str] = re.split(r'\s+|[,;?!.-]\s*', text.lower())
          #print(split_text)

          all_words += [word for word in split_text if word]
    return Counter(all_words)

def main():
    extracted_text: list[str] = extract_text_from_pdf(pdf_path)
    #print(extracted_text)
    counter: Counter = count_words(text_list=extracted_text)

    for page in extracted_text:
         print(page)

    for word, mentions in counter.most_common(5):
         print(f'{word:10}: {mentions} times')

if __name__ == '__main__':
        main()