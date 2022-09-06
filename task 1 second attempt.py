#task 1 second attempt

#task 1

import csv
rowvG = 0

def read(rowv):
    with open ('data/daily_sales_data_0.csv','r') as r_data0:
        csv_r = csv.reader(r_data0)
        next(csv_r)
        for line in csv_r:
            price = float(line[1].lstrip("$"))
            quantity = float(line[2])
            sales = price*quantity
            global write_row 
            write_row = [sales, line[3], line[4]]
            if line[0] == 'pink morsel':
                pmrows = []
                rowv = rowv +1
                pmrows[rowv] = {csv_r.line_num}
                with open ('data/new_daily_sales_data.csv', 'w') as nu_data:
                    csv_w = csv.writer(nu_data, delimiter=',')
                    for line in csv_r:
                        csv_w.writerow(line)
            
read(rowvG)
            



                

                    



    





                
            
            

            
            
                

                
                
            


               