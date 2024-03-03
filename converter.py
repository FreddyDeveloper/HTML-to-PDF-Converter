import os
import pdfkit
import tkinter as tk
from tkinter import filedialog

# Establecer la ruta de wkhtmltopdf directamente en el entorno de Python
wkhtmltopdf_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
os.environ['PATH'] += os.pathsep + os.path.dirname(wkhtmltopdf_path)

class HTMLtoPDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML to PDF Converter")

        # Configura el botón para seleccionar el archivo HTML
        self.select_html_button = tk.Button(root, text="Seleccionar HTML", command=self.select_html_file)
        self.select_html_button.pack(pady=10)

        # Configura el botón para convertir a PDF
        self.convert_button = tk.Button(root, text="Convertir a PDF", command=self.convert_to_pdf)
        self.convert_button.pack(pady=10)

    def select_html_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos HTML", "*.html")])
        if file_path:
            self.html_file_path = file_path
            print(f'Se ha seleccionado el archivo HTML: {self.html_file_path}')

    def convert_to_pdf(self):
        if hasattr(self, 'html_file_path'):
            pdf_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

            if pdf_file_path:
                try:
                    # Configura las opciones de PDF
                    options = {
                        'quiet': '',
                        'no-images': '',
                    }

                    # Convierte el archivo HTML a PDF
                    pdfkit.from_file(self.html_file_path, pdf_file_path, options=options)

                    print(f'Se ha creado el archivo PDF: {pdf_file_path}')

                except Exception as e:
                    print(f"Ha ocurrido un error: {str(e)}")
        else:
            print("Selecciona un archivo HTML antes de convertir a PDF.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HTMLtoPDFConverterApp(root)
    root.mainloop()
