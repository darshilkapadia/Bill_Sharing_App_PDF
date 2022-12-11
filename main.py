import os.path
import webbrowser

from fpdf import FPDF

class Bill:
    """
    Object that contains data about the bill such as
    total amount and period of bill
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Creates a flatmate person who lives in in the flat and
    pays the share of the bill
    """

    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    #  now how to get the other flatmates days: either by manually adding the flatmate2 amount in or call flatmate 2
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    Creates a pdf files that contains data about their names , due amount
    and period over the bills
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        # orientation portrait mode
        pdf = FPDF(orientation='P', unit='pt', format='A4')  # this line will create onl pdf with blank pages.
        # to add pages to blank pdf
        pdf.add_page()

        # Add Icon
        pdf.image("house.png", w=30, h=30)

        # Insert Main heading text
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)  # to create next cell in new line use 'ln'
        #  if w(width) set to zero will take entire row

        # insert the periods labels and values
        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=160, h=40, txt='Periods', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1,ln=1)

        # insert the fmate1 name labels and amount
        pdf.set_font(family='Times', size=14, style='I')
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)

        # insert the fmate2 name labels and amount
        pdf.set_font(family='Times', size=14, style='I')
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        # to open file automatically (For mac users)
        webbrowser.open('file://' + os.path.realpath(self.filename))


# for cli interface
amt = float(input("Hey, Enter the bill amount: "))
period = input("What is Bill Period(e.g: December 2022): ")

f_name1 = input("What is first Flatmate name?: ")
days_fname1 = int(input(f"How many days did {f_name1} stays?: "))

f_name2 = input("What is Second Flatmate name?: ")
days_fname2 = int(input(f"How many days did {f_name2} stays?: "))


the_bill = Bill(amount=amt, period = period)
flatmate1 = Flatmate(name=f_name1, days_in_house=days_fname1)
flatmate2 = Flatmate(name=f_name2, days_in_house=days_fname2)

print(f"{flatmate1.name} pays:", flatmate1.pays(bill=the_bill, flatmate2=flatmate2))
print(f"{flatmate2.name} pays:", flatmate2.pays(bill=the_bill, flatmate2=flatmate1))

# to call the pdf generate method
pdf_report = PdfReport(filename="Report-1.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

