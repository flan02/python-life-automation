import os
from pdf2docx import Converter  # Import the Class to convert PDF to DOCX
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()  # Hide the root window

main_folder = filedialog.askdirectory(title="Select Folder with PDF Files")

destiny_folder = os.path.join(main_folder, "converted_docx")

os.makedirs(
    destiny_folder, exist_ok=True
)  # - Create destination folder if it doesn't exist

for archive in os.listdir(main_folder):
    if archive.endswith(".pdf"):
        pdf_path = os.path.join(main_folder, archive)
        # pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
        docx_path = os.path.join(destiny_folder, archive.replace(".pdf", ".docx"))
        cv = Converter(pdf_path)
        cv.convert(
            docx_path, start=0, end=5
        )  # ? Converts first 5 pages. Args END is optional if not defined it converts all pages
        cv.close()  # ? Close the converter to free memory resources
