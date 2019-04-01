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
                        name = file.name,
                        date = row[0],
                        p_open = row[1],
                        high = row[2],
                        low = row[3],
                        close = row[4],
                        adj_close = row[5],
                        volume = row[6]
                    )
                    p.save()
                except:
                    pass
            i += 1