# pulls out the reviewText from a dictionary object

import gzip

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def main():
	for review in parse("reviews_Cell_Phones_and_Accessories_5.json.gz"):
		# text to parse
		write_to_file(review['reviewText'])

def write_to_file(text):
	# print(text)
	with open("input.txt", "a") as output_file:
		output_file.write(text)
		output_file.write("\n")

if __name__ =="__main__":
    main()
