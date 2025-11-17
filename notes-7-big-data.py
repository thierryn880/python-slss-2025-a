# big data
# author: Thierry Narcisse
# nov 17 2025

# open flies using python
# read data in files
# interpret the data we read


def main():
    # Get the file
    path = "data/sfu_best_cmpt120.csv"
    file = open(path)
    # Read the file
    header_row = file.readline()

    # Read the rest of the file
    for line in file:
        print(line)

    file.close()


if __name__ == "__main__":
    main()
