from momentum_app.models import SP500

import json
from scripts import defs

def run():
    SP500.objects.all().delete()

    with open('scripts/SP500_components_raw.json', 'r') as f:
        file = f.read()
    data = json.loads(file)
    for item in data:
        symbol = item["Symbol"]
        name = item["Name"]
        momentum = defs.get_avg_momentum(item["Symbol"])
        mom_12_2 = defs.get_momentum_12_2(item["Symbol"])
        ep = defs.get_ep(item["Symbol"])
        low = defs.get_low_range(item["Symbol"])

        s = SP500(symbol=symbol, name=name, avg_momentum=momentum,
            momentum_12_2=mom_12_2, ep=ep, low_range=low)
        s.save()
