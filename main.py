from flat import Bill, Flatmate
from report import PdfReport

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
pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

