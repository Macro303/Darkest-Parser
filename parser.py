def main():
	darkest_data = parseFile("test.darkest")
	displayDarkest(darkest_data)


def parseFile(filename):
	output_dict = {}
	with open(filename) as data_file:
		content = data_file.readlines()
		for line in content:
			category_data = line.split()
			category_dict = {}
			key = None
			values = []
			for x in range(1, len(category_data)):
				if category_data[x].strip().startswith('.'):
					key = category_data[x].strip()[1:]
				else:
					values.append(category_data[x].strip())
				if (x + 1) < len(category_data) and category_data[x + 1].strip().startswith('.'):
					category_dict[key] = values
					values = []
			category_dict[key] = values
			category = category_data[0].strip()
			output_dict[category[:len(category) - 1]] = category_dict
	return output_dict


def displayDarkest(darkest_data):
	for category, category_values in darkest_data.items():
		print(category)
		for sub_category, values in category_values.items():
			print('\t' + sub_category)
			for value in values:
				print('\t\t' + value)


if __name__ == '__main__':
	main()
