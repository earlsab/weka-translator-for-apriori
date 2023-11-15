# EARLAN JOSH Q. SABILLANO
# github.com/earlsab
import csv

# Converts
# | 1 | 2 | 3 | 4 |
# milk,bread,?,?

# Into
# | Milk | Bread |...
# TRUE, TRUE, ?,?

# CONFIGURATION
unique_items = []
ignore_items = [' ','', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
true_value = 't'
false_value = '?'
input_file = 'basket.csv'
output_file = 'output.csv'


#####

row_count = 0
column_count = 0
with open(input_file) as csv_file_reader:
    csv_reader = csv.reader(csv_file_reader, delimiter=',')

    # Read Unique Items
    for row in csv_reader:
        row_count += 1
        for item in row:
            column_count += 1
            if (not item in unique_items) and (not item in ignore_items):
                unique_items.append(item)

print(unique_items)
print(f'Processed {row_count} rows, and {column_count} items')

with open(input_file) as csv_file_reader:
    with open(output_file, 'w', newline='') as csv_file_writer:
        # Headers
        csv_reader2 = csv.reader(csv_file_reader, delimiter=',')
        csv_writer = csv.writer(csv_file_writer, lineterminator='\n')
        csv_writer.writerow(unique_items)
        row_count = 0
        for row in csv_reader2:
            row_staging = []
            row_count += 1

            for index in range(0, len(unique_items)):
                if row_count != 1:  # Ignore first row
                    if unique_items[index] in row:
                        row_staging.append(true_value) 
                    else:
                        row_staging.append(false_value) 
       
            csv_writer.writerow(row_staging)




