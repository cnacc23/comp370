import argparse
import csv 
from datetime import datetime 


#function to keep track of complaint type 
def complaint_type(file, start_date, end_date):

    date_format = "%m/%Y"

    complaint_count = {}
    for row in file:
        created_date = datetime.strptime(row[1][:3]+row[1][6:10], date_format)
   
        if start_date <= created_date <= end_date:
            complaint = row[5]
            borough = row[25]
    
            #key is complaint per borough (what we want to track)
            key = (complaint, borough)
        
            #either initialize key or increase its counter 
            if key not in complaint_count:
                complaint_count[key] = 1
            else:
                complaint_count[key] += 1
        
    return complaint_count

#find the most abundant complaint over input time interval 
def find_most_abundant(d):
    most_abundant_val = max(d.values())
    print("The most abundant complaint is: ", max(d)[0], "with ", most_abundant_val, " complaints")



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help= "input the file you wish to parse")
    parser.add_argument("-s", help= "input the start date of the range in MM/YYYY format")
    parser.add_argument("-e", help= "input the end date of the range in MM/YYYY format")
    parser.add_argument("--o", help= "input the optional output file")
    args = parser.parse_args()

    #open and read file 
    fname = args.i
    reader = csv.reader(open(fname, 'r'))

    date_format= "%m/%Y"

    #store start and end dates 
    start_date = datetime.strptime(args.s, date_format)
    end_date = datetime.strptime(args.e, date_format)

    
    #obtain complaint, borough, count
    complaint_count = complaint_type(reader, start_date, end_date)
    
    
    #check if output file exists 
    if args.o:
        with open(args.o, 'w', newline= '') as output_file:
            writer = csv.writer(output_file)

            #header 
            writer.writerow(['borough', 'complaint type', 'count'])

            #now write each row of results 
            for (borough, complaint), count in complaint_count.items():
                writer.writerow([borough, complaint, count])

    #if no output file exists, write to stdout
    else:
        print('borough, complaint, count')
        for key in complaint_count:
            print(key[0], "," + key[1], ",", complaint_count[key])

    #find most abundant complaint 
    find_most_abundant(complaint_count)




if __name__ == "__main__":
    main()