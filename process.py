# assign to the variable log_file the return value of the function open.
# This function opens a file and returns it as a list
log_file = open("um-server-01.txt")


# define the function to generate the sales report which takes one argument (parameter)
def generate_sales_reports(log_file):
    # loop through each line of log_file and print the ones that have Mon
    for line in log_file:
        # remove white spaces from line
        line = line.rstrip()
        # slice line from index [0] to index [3] of array
        day = line[0:3]
        # check if day is equals to "Mon" and if it is print the line
        if day == "Mon":
            print(line)


# call the fuction with the argument log_file
generate_sales_reports(log_file)
