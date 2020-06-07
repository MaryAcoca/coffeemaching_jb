import math

def month_count():
    i = interest/(12*100)
    n = math.ceil(math.log((A/(A-i*P)), 1+i))
    n_years = int(n//12)
    n_months = math.ceil(n%12)
    if n_years == 0:
        print(f'You need {n_months} months to repay this credit!')
    elif n_years > 1 and n_months == 0:
        print(f'You need {n_years} years to repay this credit!')
    else:
        print(f'You need {n_years} years and {n_months} months to repay this credit!')

def monthly_payment():
    i = interest/(12*100)
    A = ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1)) * P
    print (f'Your annuity payment = {math.ceil(A)}')

def principal():
    i = interest/(12*100)
    P = A/((i*math.pow((1+i), n))/(math.pow((1+i), n)-1))
    print(f"Your credit principal = {math.ceil(P)}!")


calculate = input("""What do you want to calculate? 
type "n" - for count of months, 
type "a" - for annuity monthly payment,
type "p" - for credit principal:""")
if calculate == "n":
    P = int(input("Enter credit principal:"))
    A = float(input("Enter monthly payment:"))
    interest = float(input("Enter credit interest:"))
    month_count()
elif calculate == "a":
    P = int(input("Enter credit principal:"))
    n = int(input("Enter count of periods:"))
    interest = float(input("Enter credit interest:"))
    monthly_payment()
elif calculate == "p":
    A = float(input("Enter monthly payment:"))
    n = int(input("Enter count of periods:"))
    interest = float(input("Enter credit interest:"))
    principal()




     


#elif calculate == "m":
#    monthly_payment = int(input("Enter monthly payment:"))
#    months = principal/monthly_payment
#    m_round = math.ceil(months)
#    if months == 1:
#        print("It takes 1 month to repay the credit")
#    else:
#        print (f"It takes {m_round} months to repay the credit")
#elif calculate == "p":
#    month_count = int(input("Enter count of months:"))
#    payment = math.ceil(principal/month_count)
#    lastpayment = math.ceil(principal - (month_count - 1) * payment)
#    if payment == lastpayment:
#        print (f'Your monthly payment = {payment}')
#    else:
#        print (f"Your monthly payment = {payment} with last month payment = {lastpayment}")