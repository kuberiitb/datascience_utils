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
