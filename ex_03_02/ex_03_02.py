h = input("Enter Hours: ")
r = input("Enter Rate: ")
try:
    fh = float(h)
    fr = float(r)
except:
    print("Error, please enter numeric input")
    quit()

if fh > 40 :
    be = fr * fh
    af = (fh - 40.0) * (fr * 0.5)
    pa = be + af
else:
    pa = fh * fr
print("pay:",pa)
