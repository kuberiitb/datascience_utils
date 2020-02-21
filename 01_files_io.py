# reading from csv
# input is file_ = '*.csv'
# output is list of dict
inputList = [x for x in csv.DictReader(open(file_,'r'))] 

# reading from csv.gz
# resultFile = '*.csv.gzip'
# output is list of dict
inputTrx = [json.loads(x) for x in gzip.open( resultFile )] 

# writing to csv file
headerDict = OrderedDict([(x, None) for x in 'col1,col2,col3'.split(',')])
with open('test_big.csv','w') as fout:
    dw = csv.DictWriter(fout, delimiter=',',fieldnames=headerDict, quoting =csv.QUOTE_ALL)
    dw.writeheader()
        for item in inputList:
        dw.writerow(item) # item is dict

# writing to csv.gz file
with gzip.open(os.path.join(backupPath, "backup.csv.gz"),'w') as outFile:
    for lJ in inList:
        row = json.dumps(lJ)
        outFile.write(row)
        outFile.write('\n')


## Write using csv module
### Write into CSV files with csv.writer()
import csv
row_list = [["SN", "Name", "Contribution"],
             [1, "Linus Torvalds", "Linux Kernel"],
             [2, "Tim Berners-Lee", "World Wide Web"],
             [3, "Guido van Rossum", "Python Programming"]]
with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"]) # header
    for row_ in row_list:
        writer.writerow(row_)  #one line at a time

### Write CSV files with quotes using list of list with csv.writerows()
import csv
row_list = [
    ["SN", "Name", "Quotes"],
    [1, "Buddha", "What we think we become"],
    [2, "Mark Twain", "Never regret anything that made you smile"],
    [3, "Oscar Wilde", "Be yourself everyone else is already taken"]
]
with open('quotes.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=';')
    writer.writerows(row_list)
    
