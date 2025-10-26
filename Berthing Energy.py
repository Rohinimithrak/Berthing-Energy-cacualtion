import math
t2_dwt=[25000,50000,80000,100000,125000,225000]#  everything in T M S
t2_ratio=[1.32,1.26,1.25,1.2,1.17,1.15]
dwt=int(input("Enter  DWT   :"))
if(dwt in t2_dwt):
    ind=t2_dwt.index(dwt)
    rat_dtdwt=t2_ratio[ind]
elif(dwt<25000):#for dwt less than 25000
    rat_dtdwt=1.32
elif(dwt>225000):#for greater
    rat_dtdwt=1.15
else:#in between
    for i in t2_dwt:
        if(dwt>i):
            templ=i
    low_i=t2_dwt.index(templ)
    up_i=low_i+1
    temp1=((t2_dwt[up_i]-dwt)*((t2_ratio[low_i]-t2_ratio[up_i])/(t2_dwt[up_i]-t2_dwt[low_i])))
    rat_dtdwt=t2_ratio[up_i]+temp1#1
disp_tonnage=rat_dtdwt*dwt#Tonnes
V=float(input("Enter approachvelocity  (0.4) :"))#m/s
L,B,D=map(float,input("Enter space separated val of len width and moulded depth of vessel \n(250 35 12.5)   :").split())
theta_deg=float(input("Enter approach angle in degree (10)   :"))
theta = math.radians(theta_deg)
g=9.81#m/s^2
den_sea=1.03#t/m^3
fos=float(input("Enter factor of safety(2)   :"))
#addedmass coeff calc
if(dwt>20000):
    cm=1+((3.14*D*D*L)/(4*disp_tonnage))
elif(dwt<20000):
    cm=1+((2*D)/B)
cs=0.9#see later
l=float(input("Enter dist bw CG and point of contact (61.55):"))#meter
r=float(input("Enter radius of longitudinal gyration(62.5)  :"))#meter
ce=((1+(((l/r)**2)*math.sin(theta)**2))/(1+((l/r)**2)))
B_E=cm*ce*cs*(disp_tonnage/g)*((V**2)/2)
print("Berthing energy  = ",B_E,"T-m")
print("Ultimate Berthing energy  = ",B_E*fos,"T-m")



