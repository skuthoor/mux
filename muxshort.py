a = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
b = [0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1]
c = [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1]
d = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
y1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
n=int(input('enter the min terms'))
minterms = list()
for i in range(0,n) :
     minterms.append(int(input())) #inputing minterms
     
#print(minterms)  #min terms printed
out = dict()
for i in range(0,16):
	out[i] = 0
     
for i in minterms :   #assigning the output values
    y1[i] = 1
    out[i] = 1
print(out) #output in dict

print(y1,'\n') #output in list

print('A','B','C','D','Y')
for i in range(0,16) :
     print(a[i] , b[i] , c[i] , d[i] , y1[i] )

y1 = tuple(y1)

q = [1,2,3,4,5,6]
for k in q :  #process
    y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    gand = 0
    gnot = 0
    gor = 0
    xor = 0
    xnor = 0 
    if k == 1 :
        print('for select line AB')
        y = y1

        f1 = 'C'
        f2 = 'C*'
        f3 = 'D'
        f4 = 'D*'

    elif k == 2 :
        print('for select line AC')
        y[0] = y1[0]
        y[1] = y1[1]
        y[2] = y1[4]
        y[3] = y1[5]
        y[4] = y1[2]
        y[5] = y1[3]
        y[6] = y1[6]
        y[7] = y1[7]
        y[8] = y1[8]
        y[9] = y1[9]
        y[10] = y1[12]
        y[11] = y1[13]
        y[12] = y1[10]
        y[13] = y1[11]
        y[14] = y1[15]
        y[15] = y1[14]

        f1 = 'B'
        f2 = 'B*'
        f3 = 'D'
        f4 = 'D*'        

    elif k == 3 :
        #for select line AD
        print('for the select line AD')

        y[0] = y1[0]
        y[1] = y1[2]
        y[2] = y1[4]
        y[3] = y1[6]
        y[4] = y1[1]
        y[5] = y1[3]
        y[6] = y1[5]
        y[7] = y1[7]
        y[8] = y1[8]
        y[9] = y1[10]
        y[10] = y1[12]
        y[11] = y1[14]
        y[12] = y1[9]
        y[13] = y1[11]
        y[14] = y1[13]
        y[15] = y1[15]
 
        f1 = 'B'
        f2 = 'B*'
        f3 = 'C'
        f4 = 'C*'

    elif k == 4 :
        #for select line BC
        print('for select line BC')

        y[0] = y1[0]
        y[1] = y1[1]
        y[2] = y1[8]
        y[3] = y1[9]
        y[4] = y1[2]
        y[5] = y1[3]
        y[6] = y1[12]
        y[7] = y1[13]
        y[8] = y1[4]
        y[9] = y1[6]
        y[10] = y1[12]
        y[11] = y1[14]
        y[12] = y1[5]
        y[13] = y1[7]
        y[14] = y1[13]
        y[15] = y1[15]

        f1 = 'A'
        f2 = 'A*'
        f3 = 'D'
        f4 = 'D*'
    elif k == 5 :
        #for select line BD
        print('for select line BD')

        y[0] = y1[0]
        y[1] = y1[2]
        y[2] = y1[8]
        y[3] = y1[10]
        y[4] = y1[1]
        y[5] = y1[3]
        y[6] = y1[9]
        y[7] = y1[11]
        y[8] = y1[4]
        y[9] = y1[5]
        y[10] = y1[12]
        y[11] = y1[14]
        y[12] = y1[6]
        y[13] = y1[7]
        y[14] = y1[13]
        y[15] = y1[15]

        f1 = 'A'
        f2 = 'A*'
        f3 = 'C'
        f4 = 'C*'       

    elif k == 6 :
        #for selct line CD
        print('for selct line CD')

        y[0] = y1[0]
        y[1] = y1[4]
        y[2] = y1[8]
        y[3] = y1[12]
        y[4] = y1[1]
        y[5] = y1[5]
        y[6] = y1[9]
        y[7] = y1[13]
        y[8] = y1[2]
        y[9] = y1[6]
        y[10] = y1[10]
        y[11] = y1[14]
        y[12] = y1[3]
        y[13] = y1[7]
        y[14] = y1[11]
        y[15] = y1[15]

        f1 = 'A'
        f2 = 'A*'
        f3 = 'B'
        f4 = 'B*'  
    

    p = [0,4,12,8]
    for i in p :
        if i == 0 :
            j = 0
        elif i == 4 :
            j = 1
        elif i == 12 :
            j = 2
        elif i == 8:
            j = 3

        if y[i+0] == y[i+1] == y[i+3] == y[i+2] == 1 :
            f = 'Vcc'
            print('I',[j] ,'=', f)

        elif (((y[i+0] == 1) & (y[i+1] == 1)) & ((y[i+3] == 1) & (y[i+2] == 0))) :
            f = 'C* + D'
            #print('I',[j] ,'=', 'gnd')
            print('I',[j] ,'=', f2 , '+' , f3)
            gor = gor + 1
            gnot = gnot + 1

        elif (((y[i+0] == 1) & (y[i+1] == 1)) & ((y[i+3] == 0) & (y[i+2] == 1))) :
            f = 'C* + D*'
            print('I',[j] ,'=', f2, '+', f4 )
            gor = gor + 1
            gnot = gnot + 2

        elif (((y[i+0] == 1) & (y[i+1] == 0)) & ((y[i+3] == 1) & (y[i+2] == 1))) :
            f = 'C + D*' 
            print('I',[j] ,'=', f1, '+', f4)
            gor = gor + 1
            gnot = gnot + 1

        elif (((y[i+0] == 0) & (y[i+1] == 1)) & ((y[i+3] == 1) & (y[i+2] == 1))) :
            f = 'C + D'
            print('I',[j] ,'=', f1, '+', f3)
            gor = gor + 1

        elif (((y[i+0] == 1) & (y[i+1] == 1)) & ((y[i+3] == 0) & (y[i+2] == 0))) :
            f ='C*'
            print('I',[j] ,'=', f2)
            gnot = gnot + 1

        elif (((y[i+0] == 1) & (y[i+1] == 0)) & ((y[i+3] == 0) & (y[i+2] == 1))) :
            f = 'D*'
            print('I',[j] ,'=', f4)
            gnot = gnot + 1

        elif (((y[i+0] == 1) & (y[i+1] == 0)) & ((y[i+3] == 1) & (y[i+2] == 0))) :
            f = 'C*.D* + C.D'
            print('I',[j] ,'=', f2 + f3, '+', f1 + f3)
            xnor = xnor + 1

        elif (((y[i+0] == 0) & (y[i+1] == 1)) & ((y[i+3] == 1) & (y[i+2] == 0))) :
            f = 'D'
            print('I',[j] ,'=', f3)

        elif (((y[i+0] == 0) & (y[i+1] == 1)) & ((y[i+3] == 0) & (y[i+2] == 1))) :
            f = 'C*.D + C.D*'
            print('I',[j] ,'=', f2 + f3, '+', f1 + f4)
            xor = xor + 1

        elif (((y[i+0] == 0) & (y[i+1] == 0)) & ((y[i+3] == 1) & (y[i+2] == 1))) :
            f = 'C'
            print('I',[j] ,'=', f1)

        elif (((y[i+0] == 1) & (y[i+1] == 0)) & ((y[i+3] == 0) & (y[i+2] == 0))) :
            f = 'C*.D*'
            print('I',[j] ,'=', f2 + f4)
            gand = gand + 1
            gnot = gnot + 2

        elif (((y[i+0] == 0) & (y[i+1] == 1)) & ((y[i+3] == 0) & (y[i+2] == 0))) :
            f = 'C*.D'
            print('I',[j] ,'=', f2 + f3)
            gand = gand + 1
            gnot = gnot + 1

        elif (((y[i+0] == 0) & (y[i+1] == 0)) & ((y[i+3] == 1) & (y[i+2] == 0))) :
            f = 'C.D'
            print('I',[j] ,'=', f1 + f3)
            gand = gand + 1

        elif (((y[i+0] == 0) & (y[i+1] == 0)) & ((y[i+3] == 0) & (y[i+2] == 1))) :
            f = 'C.D*'
            print('I',[j] ,'=', f1 + f4)
            gand = gand + 1
            gnot = gnot + 1

        elif (((y[i+0] == 0) & (y[i+1] == 0)) & ((y[i+3] == 0) & (y[i+2] == 0))) :
            f = 'gnd'
            print('I',[j] ,'=', 'gnd')    

    gates = [0,0,0,0,0,0,0]
    gates[k] = gand + gor + gnot + xnor + xor
    print('total no.of gates required is:', gates[k])    



