def parseFile(filename):
	with open(filename) as data_file:
		content = data_file.readlines()
		darkest_data = parseString(''.join(content).strip())
	return darkest_data


def parseString(data_string):
	darkest_data = dict()
	lines = data_string.split('\n')
	for line in lines:
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
		darkest_data[category[:len(category) - 1]] = category_dict
	cleanupDict(darkest_data)
	return darkest_data


def cleanupDict(darkest_data):
	for category, category_values in darkest_data.items():
		for sub_category, values in category_values.items():
			darkest_data[category].update(
				{sub_category: cleanupValues(values)})


def cleanupValues(values):
	if isinstance(values[0], str):
		if len(values) > 1 and values[0].startswith('"') and not values[1].startswith('"'):
			temp = ' '.join(values)
			values = []
			values.append(temp)
	values = [str(x).strip('"') for x in values]
	return [setType(value) for value in values]


def setType(value):
	try:
		if value == str(float(value)):
			return float(value)
		return int(value)
	except ValueError:
		if value == 'True' or value == 'False':
			return value == 'True'
		else:
			return str(value)


def displayDarkest(darkest_data):
	for category, category_values in darkest_data.items():
		print(category)
		for sub_category, values in category_values.items():
			print('\t' + sub_category)
			for value in values:
				print('\t\t' + str(value))
