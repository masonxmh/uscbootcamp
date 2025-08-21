import os
import csv

budget_data_csv = os.path.join("employee_data.csv")
#open&read csv

with open(budget_data_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #read the header row first 
    next (csv_reader)
    #read through each row of data after the header
    
    emp_list=[]
    fname_list=[]
    lname_list=[]
    dob_list=[]
    ssn_list=[]
    ssn = str()
    hidessn = str()
    state_list=[]
    
    us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
    
    for row in csv_reader:
        
        # generate emp id list
        emp_list.append(row[0])
        
        # generate new name list
        name = row[1].split(" ")
        fname_list.append(name[0])
        lname_list.append(name[1])
        #generate new DOB list
        dob = row[2].replace('-','/')
        dob_list.append(dob)
        
        #generate new SSN list
        ssn = row[3]
        #hidessn = '*' '*' '*' '-' '*' '*' '-'+ssn[7:]
        hidessn ='***-**-'+ssn[7:]
        ssn_list.append(hidessn)
        #State list
        state_list.append(us_state_abbrev[row[4]])
        employees_info=zip(emp_list,fname_list,lname_list,dob_list,ssn_list,state_list)
        
        
output_file = os.path.join("summary.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Emp ID", "First Name","Last Name","DOB", "SSN", "State"])

    writer.writerows(employees_info)
        
        
        
                  
        