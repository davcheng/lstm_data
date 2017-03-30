def main():
	input = open("generated_list_033117.txt", "r")
	for line in input:
	    if not line.startswith('I') and not line.startswith('Total') and not line.startswith('Free') and not line.startswith('pci') and not line.startswith('major') and not line.startswith('name'):
	        with open("cleansed_generated_list.txt", "a") as output_file:
			output_file.write(line)

if __name__ == "__main__":
	main()
