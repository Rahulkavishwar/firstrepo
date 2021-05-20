hrs = input(" Enter the Hours : ")
rate = input(" Enter the Rate : ")
hr = float(hrs)
r= float(rate)

def computepay(hr,r) :
    if hr>40 :
        pay = (40*r)+(hr-40)*1.5*r
        return pay
    else :
        pay = hr*r
        return pay

print("Pay",computepay(hr,r))
