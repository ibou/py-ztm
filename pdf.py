from pypdf import PdfReader, PdfWriter
import os

from_directory = 'pdf-playground' 
to_directory = 'pdf-playground/new'
# create directory to_directory if it does not exist
if not os.path.exists(to_directory):
  os.makedirs(to_directory)

def list_pdfs():
  pdf_list = []
  for filename in os.listdir(from_directory):
    if filename.endswith('.pdf'):
      pdf_list.append(f'{from_directory}/{filename}')
  return pdf_list

def main(): 
  pdf_list = list_pdfs()
  
  pdf_combiner(pdf_list)

def pdf_combiner(pdf_list):
  merger = PdfWriter()
  for pdf in pdf_list:
    print(pdf)
    merger.append(pdf)
  merger.write(f'{to_directory}/super.pdf')
  


if __name__ == '__main__':
    main()
    