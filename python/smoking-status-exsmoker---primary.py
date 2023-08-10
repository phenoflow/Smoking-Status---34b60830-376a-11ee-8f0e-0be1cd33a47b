# Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas, 2023.

import sys, csv, re

codes = [{"code":"1377","system":"readv2"},{"code":"1378","system":"readv2"},{"code":"1379","system":"readv2"},{"code":"137A.00","system":"readv2"},{"code":"137B.00","system":"readv2"},{"code":"137F.00","system":"readv2"},{"code":"137N.00","system":"readv2"},{"code":"137O.00","system":"readv2"},{"code":"137S.00","system":"readv2"},{"code":"137j.00","system":"readv2"},{"code":"13WK.00","system":"readv2"},{"code":"H310100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('smoking-status-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["smoking-status-exsmoker---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["smoking-status-exsmoker---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["smoking-status-exsmoker---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
