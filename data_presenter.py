# 1. Create a new file called data_presenter.py.

# 2. Open the CupcakeInvoices.csv.

open_file = open('CupcakeInvoices.csv')

# 3. Loop through all the data and print each row.

for line in open_file:
	print(line) #prints it raw, as seen in the csv

# 4. Loop through all the data and print the type of cupcakes purchased.

for line in open_file:
	line = line.strip() #getting rid of whitespace
	values = line.split(',') #splitting the lines at the commas and storing them in values
	for value in values: #looping through values (each line from open_file)
		print(value[2])

# 5. Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
for line in open_file:
	line = line.strip()
	values = line.split(',')
	for value in values:
		total_invoice = round(float(value[4], 2)
		print(total_invoice)

# 6. Loop through all the data, and print out the total for all invoices combined.
total_all_invoices = 0	
for line in open_file:
	line = line.strip()
	values = line.split(',')
	for value in values:
		total_invoice = round(float(value[4], 2)
		total_all_invoices = total_all_invoices + total_invoice
print(total_all_invoices)

#7. Close your open file.
open_file.close()


#Challenge: Do some research and see if you can limit your floats to never exceed to characters after the decimal point
#in this case, round(value, 2) would work best. Assuming the totals dont mind it being rounded.
#round(float(value[4], 2)




#INSERT key to stop the auto delete.