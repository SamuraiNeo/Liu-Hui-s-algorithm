import math

n = [6]                     #how many n
twon = [12]                 #how many 2n
a = [1]                     #lenght of n
x = [0.5176381]             #lenght of 2n
pn = [2.598076]             #area of n
ptwon = [3]                 #area of 2n
dtwon = [0.401924]          #difference between floor from pi and ceil from pi
pdtwon = [3.401924]

ac = input("Input the accuracy of approximation\n>>> ")

for i in range(int(ac)-1):
    n.append(n[i]*2)
    twon.append(twon[i]*2)
    a.append(x[i])
    d = (1-math.sqrt(1-(1/4)*x[i]*x[i]))*(1-math.sqrt(1-(1/4)*x[i]*x[i]))
    vsn = math.sqrt(d+(1/4)*x[i]*x[i])
    x.append(vsn)
    pn.append((n[i]/4)*(1/(math.tan(math.pi/n[i])))*a[i]*a[i])
    ptwon.append((twon[i]/4)*(1/(math.tan(math.pi/twon[i])))*x[i]*x[i])
    dtwon.append(dtwon[i]/4)
    pdtwon.append(ptwon[i]+dtwon[i])

#print(n)
#print(twon)
#print(a)
#print(x)
#print(pn)
#print(ptwon)


for j in range(int(ac)):
    print("###################################################################################")
    
    print("===================================================================================")
    print("Accuracy:                            "+str(int(j)+1))
    print("===================================================================================")
    
    print("Quantity of walls:                                   " + str(n[j]))
    print("Quantity of walls *2:                                " + str(twon[j]))
    print("Lenght of wall:                                      " + str(a[j]))
    print("Lenght of wall (double n):                           " + str(x[j]))
    print("Area of n - shape:                                   " + str(pn[j]))
    print("Area of 2n - shape     --> floor(PI):                " + str(ptwon[j]))
    print("Difference between floor from Pi and ceil from Pi:   " + str(dtwon[j]))
    print("Area of 2n+D - shape   --> ceil(PI):                 " + str(pdtwon[j]))

    print("###################################################################################")
    print("")
