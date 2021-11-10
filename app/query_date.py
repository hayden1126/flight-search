import re

query_date_list = []

def convert_query_date_to_list(rawText):
    print("input data: {}".format(rawText))

    regex = '\d+'  
    rangeMode = True

    r_list = re.findall(regex, rawText)
    print(r_list)

    if (len(r_list) <= 3):
        rangeMode = False
        endDate = ""

    if rangeMode:
        if int(r_list[0]) < 10 :
            startDate = "0" + r_list[0]
            # print(startDate)
        else:
            startDate = r_list[0]

        if int(r_list[1]) < 10 :
            endDate = "0" + r_list[1]
            # print(endDate)
        else:
            endDate = r_list[1]

        if int(r_list[2]) < 10 :
            if len(r_list[2])>1:
                month = r_list[2]
            else: 
                month = "0" + r_list[2]
            # print(month)
            
        year = r_list[3]
    else:
        if int(r_list[0]) < 10 :
            startDate = "0" + r_list[0]
            # print(startDate)
        else:
            startDate = r_list[0]

        if int(r_list[1]) < 10 :
            if len(r_list[1])>1:
                month = r_list[1]
            else: 
                month = "0" + r_list[1]
            # print(month)
        else:
            month = r_list[1]

        year = r_list[2]

    # print("endDate: {} startDate: {}".format(endDate,startDate))
    
    if rangeMode:
        forLoopLength = int(endDate)-int(startDate) + 1
        for x in range(int(startDate), int(endDate)+1):
            if x < 10:
                d = year + "-" + month + "-" + "0" + str(x)
            else:
                d = year + "-" + month + "-" + str(x)
            query_date_list.append(d)

    print(query_date_list)

    return(query_date_list)



