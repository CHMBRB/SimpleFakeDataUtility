#!/usr/bin/env python3
from pandas import DataFrame
from pathlib import Path
from datetime import time
from models.FakerClasses import FakePerson, FakeContactDetail
from models.DataClasses import LaborDetail

# adjust the number of required entries to meet your data sampling needs
number_of_records = 100

# determine if tab-delimited csv or excel output format
excel_file_format = 0

# hardcoded data output directory
output_path = Path('./data/')

# dates for FakeLaborDetail
# expand to cover more quarters for resampling
dates_range = [
    "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
    "2023-02-01", "2023-02-02", "2023-02-03", "2023-02-04", "2023-02-05",
    "2023-03-01", "2023-03-02", "2023-03-03", "2023-03-04", "2023-03-05",
    "2023-04-01", "2023-04-02", "2023-04-03", "2023-04-04", "2023-04-05",
    "2023-07-01", "2023-07-02", "2023-07-03", "2023-07-04", "2023-07-05",
    "2023-12-01", "2023-12-02", "2023-12-03", "2023-12-04", "2023-12-05",
]

if __name__ == "__main__":
    # create empty lists for storing generated data
    person_list = []
    contact_detail_list = []
    labor_detail_list = []

    # declare an integer to use for unique id field on labor detail
    labor_detail_id = 0

    for i in range(number_of_records):
        # instantiate new FakeRecords
        p = FakePerson(i)
        cd = FakeContactDetail(i)
        # append FakeRecords data to our respective lists
        person_list.append(p.__dict__)
        contact_detail_list.append(cd.__dict__)

        for item in dates_range:
            el = LaborDetail()
            el.id = labor_detail_id
            el.person_id = i
            el.current_date = item
            el.time_in = time(9, 0, 0).strftime("%H:%M:%S")
            el.time_out = time(17, 0, 0).strftime("%H:%M:%S")
            labor_detail_list.append(el.__dict__)
            # update the unique id for the next iteration
            labor_detail_id += 1

    # convert the records to pandas DataFrame objects
    dfA = DataFrame(person_list)
    dfB = DataFrame(contact_detail_list)
    dfC = DataFrame(labor_detail_list)

    # write the generated records to a file
    if (excel_file_format):
        # attempting to write to the same workbook will overwrite data
        dfA.to_excel(output_path.joinpath('Person.xlsx'), index=False)
        dfB.to_excel(output_path.joinpath('ContactDetail.xlsx'), index=False)
        dfC.to_excel(output_path.joinpath('LaborDetail.xlsx'), index=False)
    else:
        # csv may contain only one sheet
        dfA.to_csv(output_path.joinpath('Person.csv'), sep='\t', index=False)
        dfB.to_csv(output_path.joinpath('ContactDetail.csv'), sep='\t', index=False)
        dfC.to_csv(output_path.joinpath('LaborDetail.csv'), sep='\t', index=False)