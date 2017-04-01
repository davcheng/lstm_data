# removes all lines from a file that begin with

def main():
    input = open("cleansed_generated_list_CLEANED.txt", "r")
    for line in input:
    # specify characters that denote lines to remove
    # if not i % 2:
        for x in line.split('  ', 1):
            print(x)
            with open("cleansed_generated_list_CLEANED_2.txt", "a") as output_file:
                output_file.write(x)

if __name__ == "__main__":
    main()

