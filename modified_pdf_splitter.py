from PyPDF4 import PdfFileReader, PdfFileWriter
import os

# Original file path
original_file_path = r'path/file.pdf'

# Read the PDF
pdf = PdfFileReader(original_file_path)
num_page = pdf.numPages
print ("O pdf possui ", num_page , " páginas.")

page = 2 #change this to whatever page you want to split the file in

# Process each page (in this example, just the first page)
for k in range(page - 1, page):  # Replace range(0, 1) with range(0, num_page) to process all pages
    # Create a PdfFileWriter object
    pdf_writer = PdfFileWriter()
    
    # Add the page to the PdfFileWriter object
    pdf_writer.addPage(pdf.getPage(k))
    
    # Create a new file name
    original_file_name, file_extension = os.path.splitext(original_file_path)
    new_file_name = f"{original_file_name}_page_{k + 1}{file_extension}"
    
    # Save the page to a new file
    with open(new_file_name, 'wb') as f:
        pdf_writer.write(f)


