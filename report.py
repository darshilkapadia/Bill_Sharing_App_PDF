import webbrowser
import os
from fpdf import FPDF
from filestack import Client


class PdfReport:
    """
    Creates a pdf files that contains data about their names , due amount
    and period over the bills
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        # orientation portrait mode
        pdf = FPDF(orientation='P', unit='pt', format='A4')  # this line will create onl pdf with blank pages.
        # to add pages to blank pdf
        pdf.add_page()

        # Add Icon
        pdf.image("files/house.png", w=30, h=30)

        # Insert Main heading text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)  # to create next cell in new line use 'ln'
        #  if w(width) set to zero will take entire row

        # insert the periods labels and values
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=160, h=40, txt='Periods', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # insert the fmate1 name labels and amount
        pdf.set_font(family='Times', size=14, style='I')
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # insert the fmate2 name labels and amount
        pdf.set_font(family='Times', size=14, style='I')
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(f"{self.filename}")

        # to open file automatically (For mac users)
        webbrowser.open('file://' + os.path.realpath(f"{self.filename}"))


class FileSharer:
    def __init__(self, filepath, api_key='ABhmbjy5GRq6Q0Q3gndZhz'):
        self.filepath = filepath
        self.apikey = api_key

    def share(self):
        client = Client(self.apikey)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
