#salary inn HRA AND DA
name=input("enter the name of employee")
salary=int(input("enter the salary"))
if (salary<3000):
    hra=salary*10/100
    da=salary*5/100
    print(name,"your salary is",salary)
    print("HRA is =",hra)
    print("DA is =",da)
else:
    if(salary<5000):
        hra=salary*20/100
        da=salary*15/100
        print(name,"your salary is",salary)
        print("HRA is =",hra)
        print("DA is =",da)
    else:
        if(salary<7000):
            hra=salary*30/100
            da=salary*25/100
            print(name,"your salary is",salary)
            print("HRA is =",hra)
            print("DA is =",da)
        else:
            if(salary<9000):
                hra=salary*40/100
                da=salary*35/100
                print(name,"your salary is",salary)
                print("HRA is =",hra)
                print("DA is =",da)
            else:
                hra=salary*45/100
                da=salary*40/100
                print(name,"your salary is",salary)
                print("HRA is =",hra)
                print("DA is =",da)
netsalary = salary + hra + da
print("your net salary is",netsalary)
