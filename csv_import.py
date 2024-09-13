import csv
def csv_reader(pin_from_pic):
    PO_list = []
    file1 = csv.reader(open("pincode.csv","r",encoding='latin-1'),delimiter=",")
    found=0
    pincode1 = str(pin_from_pic)
    for row in file1:
        if pincode1 == str(row[1]):
            found=1
            global district
            district = row[8]
            PO_list.append(row[0])
            global state
            state = row[9]
            global division
            division = row[4]
            global talukname
            talukname = row[7]
    if(found==1):
        list1 = [pincode1,district,PO_list,state,division,talukname]
        return(list1)
    else:
        list2 = [pincode1,"not found","not found","not found","not found","not found"]
        return(list2)

csv_reader("505004")