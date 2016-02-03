def read_file(input_file):
	data_list = []
	with open(input_file, 'rU') as f:
		data_file = csv.DictReader(f)
		for line in data_file:
			data_list.append(line) # Gets you a list of dicts.
	return data_list
# end

def write_csvfile(data_list, output_file):
	# Make header.
	first = data_list[0]
	header = first.keys()

	with open(output_file, 'w') as f:
		file_writer = csv.DictWriter(f, fieldnames=header)
		file_writer.writeheader()
		for line in data_list:
			file_writer.writerow(line)
# end
