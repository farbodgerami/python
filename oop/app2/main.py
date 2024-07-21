from fpdf import FPDF


class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    def __init__(self, name, daysinhouse):
        self.name = name
        self.daysinhouse = daysinhouse

    def pays(self, bill, flatmate2):
        weight = self.daysinhouse / (self.daysinhouse + flatmate2.daysinhouse)
        topay = bill.amount * weight
        return topay


class Pdfreport:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=1, align='C', ln=1)

        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150,
                 h=40,
                 txt=str(round(flatmate1.pays(bill, flatmate2), 2)),
                 border=1,
                 ln=1)
        
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150,
                 h=40,
                 txt=str(round(flatmate2.pays(bill, flatmate1), 2)),
                 border=1,
                 ln=1)

        pdf.output(self.filename)

bbill=input('enter the bill amount: ')
u1=input('enter user1:')
u2=input('enter user2:')
thebill = Bill(amount=int(bbill), period='March 2021')
john = Flatmate('John',int(u1))
marry = Flatmate('Marry', int(u2))

print('john pays: ', john.pays(bill=thebill, flatmate2=marry))
print('marry pays: ', marry.pays(bill=thebill, flatmate2=john))

pdfreport = Pdfreport(filename="report.pdf")
pdfreport.generate(flatmate1=john, flatmate2=marry, bill=thebill)
