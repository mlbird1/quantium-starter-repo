#task 1

import csv


with open ('data/daily_sales_data_0.csv','r') as r_data0:
    csv_r = csv.reader(r_data0)
    next(csv_r)
    for line in csv_r:
        price = float(line[1].lstrip("$"))
        quantity = float(line[2])
        sales = price*quantity
        write_row = [sales, line[3], line[4]]

       

        with open ('data/new_daily_sales_data_0.csv', 'w') as new_data0:
            fieldnames = ['sales', 'date', 'region']  
            csv_w = csv.writer(new_data0, delimiter=',')
            csv_w.writerow(fieldnames)
            for line in csv_r:
                if line[0]=='pink morsel':
                        csv_w.writerow(write_row)
               

           



                    



    

