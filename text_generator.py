<<<<<<< HEAD
# program to loop through a program and capture all outputs and store in a text file

=======
>>>>>>> 27632da34db1df044a40621c5271fd2846b8961c
import subprocess

def main():
	generated_result = subprocess.Popen(['python', 'sample.py'], stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
	out = generated_result.communicate()[0]
	write_to_file(out)

def write_to_file(text):
	with open("generated_list.txt", "a") as output_file:
		output_file.write(text)
		# output_file.write("\n")

if __name__ == "__main__":
	for x in xrange(500): 
<<<<<<< HEAD
		main()
=======
		main()
>>>>>>> 27632da34db1df044a40621c5271fd2846b8961c
