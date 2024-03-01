

# hackerank link: https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true


from datetime import datetime

Return_date = str(input("Your due date:6/6/2015 \nenter return date:dd/mm/yyyy\n"))
Due_date = "6/6/2015"

Return = datetime.strptime(Return_date, '%d/%m/%Y').date()
Due = datetime.strptime(Due_date, '%d/%m/%Y').date()

Rday = Return.day
Rmonth = Return.month
Ryear = Return.year

Dday = Due.day
Dmonth = Due.month
Dyear = Due.year

print(Return-Due)

if(Return<=Due):
    print(0)
elif(Return>Due and Rmonth==Dmonth and Ryear==Dyear):
    print(15*(Rday-Dday), "hackos")
elif(Return>Due and Rmonth>Dmonth and Ryear==Dyear):
    print(500*(Rmonth-Dmonth) ,"hackos")
elif(Return>Due and Ryear>Dyear):
    print("10000 hackos")
    
