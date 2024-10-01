a = input("Enter Hours: ")
b = input("Enter Rate: ")

try:
    c = float(a)
    d = float(b)
except:
    print("Error, pleasee enter numeric")
    quit()

print(c, d)
if c > 40 : 
    reg = c * d
    otp = (d - 40.0) * (c * 0.5)
    xp = reg + otp
else:
    xp = d + c
print("Pay: ", xp )