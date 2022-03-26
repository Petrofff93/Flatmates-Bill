from flat import Bill, Flatmate
from pdf_report import PdfReport, FileSharer

amount = float(input("Hey user, enter the bill amount: "))
period = input("Enter the bill period - E.g. December 2020: ")

name1 = input("Enter the name of first Flatmate: ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house"
                           " during the bill period? "))
name2 = input("Enter the name of the second Flatmate: ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house"
                           " during the bill period? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{name1} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{name2} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())


