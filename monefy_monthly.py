import csv
import sys
from collections import Counter
from decimal import Decimal

def process(filename, month_count):
  ct = Counter()

  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
      ct.update({row[2]: Decimal(row[3].replace(",", ""))})

  for category, amount in ct.most_common(100)[::-1]:
    print(f"{category}: {(amount / Decimal(month_count)).quantize(Decimal("0.01"))}")



if __name__ == "__main__":
  filename = sys.argv[1]
  month_count = int(sys.argv[2])
  process(filename, month_count)
