import sys

from collections import defaultdict, Counter
from decimal import Decimal
from datetime import datetime, date


category_amount = defaultdict(lambda: Decimal(0))
description_amount = defaultdict(lambda: Decimal(0))

def parse_file(file):
	with open(file, "r") as f:
		f.readline()
		for line in f.readlines():
			entrydate, account, category, amount, currency1, converted_amount, currency2, description = line.split(";")
			date = datetime.strptime(entrydate, "%d/%m/%Y")
			if date < date.today():
				category_amount[category] += Decimal(amount.replace(",", ""))
				description_amount[description.strip()] += Decimal(amount.replace(",", ""))


def print_most_common():
	catcount = Counter(category_amount)
	descount = Counter(description_amount)

	print("======================")
	print("Most common categories")
	print("======================")
	print(catcount.most_common(10))

	print("========================")
	print("Most common descriptions")
	print("========================")
	print(descount.most_common(10))


if __name__ == "__main__":
	file = sys.argv[1]
	parse_file(file)
	print_most_common()