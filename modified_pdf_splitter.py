from PyPDF4 import PdfFileReader, PdfFileWriter
import os

# Original file path
original_file_path = r'C:/Users/Carlos/Meu Drive/Aulas/Aulas - UEPG/EaD/2024/Introducao a Pratica Extensionista/EDITAL_433_23___Abertura____Professores_Formadores___Curso_de_Licenciatura_em_Matematia____Disciplinas_1__semestre_2024.pdf'

# Read the PDF
pdf = PdfFileReader(original_file_path)
num_page = pdf.numPages
print ("O pdf possui ", num_page , " páginas.")

page = 18

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

