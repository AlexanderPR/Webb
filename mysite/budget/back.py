import csv
import os
from budget.models import Stock_history

def handle_uploaded_file(f):
    with open('media/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def read_file(file):
    i = 0
    with open('media/' + file.name) as f:
        reader = csv.reader(f)
        for row in reader:
            if i > 0:
                try:
                    p = Stock_history(
                        _name = file.name,
                        _date = row[0],
                        _open = row[1],
                        _high = row[2],
                        _low = row[3],
                        _close = row[4],
                        _adj_close = row[5],
                        _volume = row[6]
                    )
                    p.save()
                except:
                    pass
            i += 1