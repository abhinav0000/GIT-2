import datetime as dt 
print("enter 1st person's DOB as asked below :\n")
year=int(input("year: "))
month=int(input("\nmonth: "))
day=int(input("\nday: "))
hour=int(input("\nhour"))
minute=int(input("\nminutes: "))

a=dt.datetime(year,month,day,hour,minute)

print("enter 2st person's DOB as asked below :\n")
year2=int(input("year: "))
month2=int(input("\nmonth: "))
day2=int(input("\nday: "))
hour2=int(input("\nhour: "))
minute2=int(input("\nminutes: "))

b=dt.datetime(year2,month2,day2,hour2,minute2)

if(a>b):
    c=a-b
   
    print(c)
else:
    c=b-a
    
    print(c)