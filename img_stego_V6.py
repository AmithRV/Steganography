import time
import cv2
import PIL
from PIL import Image

def binary(n):
    k=7
    i=0
    t=[]
    bi = [0,0,0,0,0,0,0,0]
    while i<8:
        bi[k]=n%2
        n=int(n/2)
        i=i+1
        k=k-1
    for j in bi:
        t.append(j)
    return t


def  dimension(fname):
    filepath = fname
    image = cv2.imread(filepath)

    # get width and height
    height, width = image.shape[:2]

    return width,height

def bin_to_int(bi):
    sum=0
    sum = bi[0]*128+bi[1]*64+bi[2]*32+bi[3]*16+bi[4]*8+bi[5]*4+bi[6]*2+bi[7]*1
    return sum

def read():
    name = input("File name : ")
    
    start = time.time()

    img = PIL.Image.open(name)     #Create a PIL.Image object 
    end = ord('/')
    
    x=0
    y=0
    z =1
    t = img.getpixel( (0,0) )
    r = t[0]
    msg=""
    bi=""
    while r!=end:
        t = img.getpixel( (x,y) )
        r = t[0]    #get the red color at (x,y) position
        temp = binary(r)    #get the binary of red
        bi=bi+str(temp[7])
        #print(r)
        if z%8==0:
            #print("(",r,")")
            z=0

        x=x+1
        y=y+1
        z=z+1
    
    l = len(bi)
    
    i = 0
    k = 0
    t = ""
    q = ""
    final = []
    while i<l-1 :
        msg = msg+str( bi[i] )
        
        
        k=k+1
        if k%8==0:
            q = q+str(bi[i])
            t = q
            final.append(t)
            q=''
        elif k%8!=0:
            q = q+str(bi[i])
        i=i+1

    s=0
    for i in final:
        s = int(i[0])*128+ int(i[1])*64+ int(i[2])*32+ int(i[3])*16+ int(i[4])*8+ int(i[5])*4+ int(i[6])*2+ int(i[7])*1
        print( chr(s),end=""  )
    end = time.time()
    print("\ntime = ",end-start)

def inp():
    name = input("File name : ")
    msg    = input("MESSAGE : ")

    start = time.time()

    w,h = dimension('test.jpg')

    end = ord('/')

    temp=[]
    bi=[]
    x = 0
    y = 0
    
    for i in msg:                               #convert msg to ascii values, ord() generate ascii value of each character
        temp.append(ord(i))     

    img = PIL.Image.open('test.jpg')
    new_r=0
    diff=0
    for j in temp:
        bij = binary(j)
        k = 0

        while k<8:
            t = img.getpixel( (x,y) )
            r = t[0]    #we get the red color value of pixel at (x,y)

            if r==end:
                r=r-2

            bir = binary(r)  #we convert the value of red to binary

            bir[7] = bij[k]     #changing the LSB binary value of RED with binary ASCII value of j
            
            new_r = bin_to_int(bir)
            if new_r==end:
                diff = new_r - r
                r=r-diff
                bir=binary(r)
                bir[7] = bij[k]
                new_r = bin_to_int(bir)

            value = (new_r,t[1],t[2])     # changing the pixel value to new value      
            img.putpixel((x,y), value)
            
            k=k+1
            x=x+1
            y=y+1
            
    t = img.getpixel( (x,y) )
    value = (end,t[1],t[2])     # we mark the end of msg by adding ASCII('/')
    img.putpixel((x,y), value)   
    img.save(name+'.png')
    print("\nFile saved as "+name+".png")

    end = time.time()
    print("\n time = ",end-start)

index =0
while index!=3:
    print("\n")
    print("1. Read")
    print("2. Write")
    print("3. End")
    index = int(input("Index = "))
    
    if index==1:
        read()
    elif index==2:
        inp()
    elif index==3:
        exit()

inp()