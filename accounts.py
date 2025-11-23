import csv

data = [
    {'ACC_ID': '1001', 'NAME': 'ANMOL', 'ACC_NUMBER': '10196', 'PIN': '1204', 'BALANCE': '56880.00'},
    {'ACC_ID': '1002', 'NAME': 'RAM', 'ACC_NUMBER': '19567', 'PIN': '1946', 'BALANCE': '28400.00'},
    {'ACC_ID': '1003', 'NAME': 'SHYAM', 'ACC_NUMBER': '78546', 'PIN': '1256', 'BALANCE': '17000.00'},
    {'ACC_ID': '1004', 'NAME': 'ROHAN', 'ACC_NUMBER': '62345', 'PIN': '1241', 'BALANCE': '19800.00'},
    {'ACC_ID': '1005', 'NAME': 'SHANPREET', 'ACC_NUMBER': '17249', 'PIN': '1232', 'BALANCE': '1700.00'},
    {'ACC_ID': '1006', 'NAME': 'NAMAN', 'ACC_NUMBER': '18349', 'PIN': '1198', 'BALANCE': '15000.00'},
    {'ACC_ID': '1007', 'NAME': 'PUSHKAR', 'ACC_NUMBER': '19624', 'PIN': '1143', 'BALANCE': '15700.00'},
    {'ACC_ID': '1008', 'NAME': 'GYAN', 'ACC_NUMBER': '18567', 'PIN': '1982', 'BALANCE': '12380.00'},
    {'ACC_ID': '1009', 'NAME': 'ROHIT', 'ACC_NUMBER': '56832', 'PIN': '1221', 'BALANCE': '145000.00'},
    {'ACC_ID': '1010', 'NAME': 'RAMAN', 'ACC_NUMBER': '19074', 'PIN': '1217', 'BALANCE': '18000.00'},
]

fieldnames = ['ACC_ID', 'NAME', 'ACC_NUMBER', 'PIN', 'BALANCE']
file_name = 'accounts.csv'

with open(file_name, mode='w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader() # Write the header row
    writer.writerows(data) # Write all the data rows

print(f"File '{file_name}' created successfully.")
