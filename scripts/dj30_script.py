from momentum_app.models import DJ30

import csv
import json
from scripts import defs


def run():
    DJ30.objects.all().delete()

    with open('scripts/DJ30.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            symbol = row[1]
            name = row[0]
            mom = defs.get_avg_momentum(row[1])
            ep = defs.get_ep(row[1])

            d = DJ30(symbol=symbol, name=name, avg_momentum=mom, ep=ep)
            d.save()
