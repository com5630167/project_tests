from netCDF4 import Dataset
import numpy as np
import json

def Dec_year(year,var):
   y = str(year)
   m1 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'01.nc', 'r')
   m2 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'02.nc', 'r')
   m3 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'03.nc', 'r')
   m4 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'04.nc', 'r')
   m5 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'05.nc', 'r')
   m6 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'06.nc', 'r')
   m7 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'07.nc', 'r')
   m8 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'08.nc', 'r')
   m9 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'09.nc', 'r')
   m10 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'10.nc', 'r')
   m11 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'11.nc', 'r')
   m12 = Dataset('/home/thiranan/Climate Data/Exp_03_mm_ATM.197'+y+'12.nc', 'r')
#print(v.variables)
   lons = m1.variables['lon']
   lats = m1.variables['lat']
   times = m1.variables['time']
   ts1 = m1.variables[var]
   ts2 = m2.variables[var]
   ts3 = m3.variables[var]
   ts4 = m4.variables[var]
   ts5 = m5.variables[var]
   ts6 = m6.variables[var]
   ts7 = m7.variables[var]
   ts8 = m8.variables[var]
   ts9 = m9.variables[var]
   ts10 = m10.variables[var]
   ts11 = m11.variables[var]
   ts12 = m12.variables[var]

   temp_avg1 = np.average(ts1,axis=2)
   temp_avg2 = np.average(ts2,axis=2)
   temp_avg3 = np.average(ts3,axis=2)
   temp_avg4 = np.average(ts4,axis=2)
   temp_avg5 = np.average(ts5,axis=2)
   temp_avg6 = np.average(ts6,axis=2)
   temp_avg7 = np.average(ts7,axis=2)
   temp_avg8 = np.average(ts8,axis=2)
   temp_avg9 = np.average(ts9,axis=2)
   temp_avg10 = np.average(ts10,axis=2)
   temp_avg11 = np.average(ts11,axis=2)
   temp_avg12 = np.average(ts12,axis=2)
   
   if(var == 'ts'):
       for i in range(1):
            tem_a1 = temp_avg1[i]-273.15
            tem_a2 = temp_avg2[i]-273.15
            tem_a3 = temp_avg3[i]-273.15
            tem_a4 = temp_avg4[i]-273.15
            tem_a5 = temp_avg5[i]-273.15
            tem_a6 = temp_avg6[i]-273.15
            tem_a7 = temp_avg7[i]-273.15
            tem_a8 = temp_avg8[i]-273.15
            tem_a9 = temp_avg9[i]-273.15
            tem_a10 = temp_avg10[i]-273.15
            tem_a11 = temp_avg11[i]-273.15
            tem_a12 = temp_avg12[i]-273.15

   if(var == 'pr'):
       for i in range(1):
            tem_a1 = temp_avg1[i]*3600
            tem_a2 = temp_avg2[i]*3600
            tem_a3 = temp_avg3[i]*3600
            tem_a4 = temp_avg4[i]*3600
            tem_a5 = temp_avg5[i]*3600
            tem_a6 = temp_avg6[i]*3600
            tem_a7 = temp_avg7[i]*3600
            tem_a8 = temp_avg8[i]*3600
            tem_a9 = temp_avg9[i]*3600
            tem_a10 = temp_avg10[i]*3600
            tem_a11 = temp_avg11[i]*3600
            tem_a12 = temp_avg12[i]*3600


   
   temp = []

   temp.append(sum(tem_a1)/len(tem_a1))
   temp.append(sum(tem_a2)/len(tem_a2))
   temp.append(sum(tem_a3)/len(tem_a3))
   temp.append(sum(tem_a4)/len(tem_a4))
   temp.append(sum(tem_a5)/len(tem_a5))
   temp.append(sum(tem_a6)/len(tem_a6))
   temp.append(sum(tem_a7)/len(tem_a7))
   temp.append(sum(tem_a8)/len(tem_a8))
   temp.append(sum(tem_a9)/len(tem_a9))
   temp.append(sum(tem_a10)/len(tem_a10))
   temp.append(sum(tem_a11)/len(tem_a11))
   temp.append(sum(tem_a12)/len(tem_a12))

   c = np.array(temp)
   y197 = [float(Decimal("%.2f" % e)) for e in c]

 
   return y197



def cal_year(var):
   y197 = []
   for i in range(0, 10):
       y = Dec_year(i,var)
       y197.append(sum(y)/len(y))
   c = np.array(y197)
   y197 = [float(Decimal("%.2f" % e)) for e in c]
   return y197

def cal_month(var):
   mon_avg = []
   y0 = Dec_year(0,var)
   y1 = Dec_year(1,var)
   y2 = Dec_year(2,var)
   y3 = Dec_year(3,var)
   y4 = Dec_year(4,var)
   y5 = Dec_year(5,var)
   y6 = Dec_year(6,var)
   y7 = Dec_year(7,var)
   y8 = Dec_year(8,var)
   y9 = Dec_year(9,var)
 

   for i in range(0, 12):
       mon_avg.append((y0[i]+y1[i]+y2[i]+y3[i]+y4[i]+y5[i]+y6[i]+y7[i]+y8[i]+y9[i])/9)

   c = np.array(mon_avg)
   mon_avg = [float(Decimal("%.2f" % e)) for e in c]

   return mon_avg

def data_set(var):
   mon_avg = []
   y0 = Dec_year(0,var)
   y1 = Dec_year(1,var)
   y2 = Dec_year(2,var)
   y3 = Dec_year(3,var)
   y4 = Dec_year(4,var)
   y5 = Dec_year(5,var)
   y6 = Dec_year(6,var)
   y7 = Dec_year(7,var)
   y8 = Dec_year(8,var)
   y9 = Dec_year(9,var)
 

   for i in range(0, 12):
       mon_avg.append(y0[i])
       mon_avg.append(y1[i])
       mon_avg.append(y2[i])
       mon_avg.append(y3[i])
       mon_avg.append(y4[i])
       mon_avg.append(y5[i])
       mon_avg.append(y6[i])
       mon_avg.append(y7[i])
       mon_avg.append(y8[i])
       mon_avg.append(y9[i])

   c = np.array(mon_avg)
   mon_avg = [float(Decimal("%.2f" % e)) for e in c]

   return mon_avg

def data_year():
   mon_avg = []
   for i in range(0, 10):
       for j in range(0, 12):
           if j <= 9:
               mon_avg.append("197"+str(i)+"-0"+str(j)+"-00")
           elif j >= 10:
               mon_avg.append("197"+str(i)+"-"+str(j)+"-00")
   return mon_avg

def dat(x):
    data = data_set(x)
    year = data_year()
    set_d = []
    for i in range(0,len(data)):
        set_d.append([year[i],data[i]])
    return set_d

def mon(x):
    data = cal_month(x)
    month = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    set_d = []
    for i in range(0,len(data)):
        set_d.append([month[i],data[i]])
    return set_d

