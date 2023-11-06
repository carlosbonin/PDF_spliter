from PyPDF4 import PdfFileReader, PdfFileWriter
import os

# Original file path
original_file_path = r'original path/original file.pdf'

# Read the PDF
pdf = PdfFileReader(original_file_path)
num_page = pdf.numPages
print("The PDF file has ", num_page, " pages.")

# Ask the user for the starting and ending page numbers
start_page = int(input("Please, type the number of the initial page you would like to extract: "))
end_page = int(input("Please, type the number of the final page you would like to extract: "))

# Validate the user input
if start_page < 1 or start_page > num_page or end_page < 1 or end_page > num_page or start_page > end_page:
    print("Sorry, you range of pages is not valid. Please, type a number between 1 and ", num_page)
else:
    # Create a PdfFileWriter object
    pdf_writer = PdfFileWriter()

    # Iterate over the range of pages and add each to the PdfFileWriter object
    for k in range(start_page - 1, end_page):
        pdf_writer.addPage(pdf.getPage(k))

    # Create a new file name
    original_file_name, file_extension = os.path.splitext(original_file_path)
    new_file_name = f"{original_file_name}_pages_{start_page}_to_{end_page}{file_extension}"

    # Save the pages to a new file
    with open(new_file_name, 'wb') as f:
        pdf_writer.write(f)

    print(f"The pages from {start_page} to {end_page} were succesfully saved as {new_file_name}.")
