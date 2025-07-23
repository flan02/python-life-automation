import os
from docx2pdf import convert  # Transform .docx files to PDF
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()  # Hide the root window

main_folder = filedialog.askdirectory(title="Select Folder with .docx Files")

destiny_folder = os.path.join(main_folder, "converted_PDFs")
os.makedirs(
    destiny_folder, exist_ok=True
)  # - Create destination folder if it doesn't exist

for archive in os.listdir(main_folder):
    if archive.endswith(".docx"):
        docx_path = os.path.join(main_folder, archive)
        # pdf_path = os.path.splitext(docx_path)[0] + ".pdf"
        pdf_path = os.path.join(destiny_folder, archive.replace(".docx", ".pdf"))
        convert(docx_path, pdf_path)
        print(f"Converted {archive} to PDF.")
