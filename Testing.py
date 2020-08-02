import csv
informations=[]

class information:
    def __init__(self, in_name, in_, in_price, in_rating):
        self.textbook=str(in_textbook)
        self.subject=str(in_subject)
        self.price=str(in_price)
        self.rating=str(in_rating)

def __str__(self):
        return self.textbook

def loadData():
    data=csv.DictReader(open('3.csv'))
    for datum in data:
        books.append(book(datum['Textbook'],datum['Subject'],datum['Price'],datum['Rating']))