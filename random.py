#%%
import numpy as np 
import random 
import matplotlib.pyplot as plt
import array
import math
parray_x=[]
parray_y=[]
#-----------------------------------------------------------------------------------
def compare_position(farray_x=[],farray_y=[],parray_x=[],parray_y=[]):
 a=0
 
 while a<=99:
   array_x=random.uniform(1,100)
   array_y=random.uniform(1,100)
   choose_x_a=float(farray_x[a])
   choose_x_b=array_x
   choose_y_a=float(farray_y[a])
   choose_y_b=array_y
   radius=math.sqrt((choose_x_a-choose_x_b)**2+(choose_y_a-choose_y_b)**2)
   while  radius>=10: 
     array_x=random.uniform(1,100)
     array_y=random.uniform(1,100)
     choose_x_a=float(farray_x[a])
     choose_x_b=array_x
     choose_y_a=float(farray_y[a])
     choose_y_b=array_y
     radius=math.sqrt((choose_x_a-choose_x_b)**2+(choose_y_a-choose_y_b)**2)
   parray_x.append(array_x)
   parray_y.append(array_y)
   if a==99:
     return parray_x,parray_y
     break
   a+=1
  
#-----------------------------------------------------------------------------
class randomposition():
 array_x=[random.uniform(1,100)]
 array_y=[random.uniform(1,100)]
 def  random_position(array_x=[],array_y=[]):
   array_x.append(random.uniform(1,100))
   array_y.append(random.uniform(1,100))
   return array_x,array_y
 i=0
 count=99
 while i<=count:
   random_position(array_x,array_y)
   i+=1
 plt.scatter(array_x,array_y)
#----------------------------------------------------------------------------------------
first=randomposition()
#---------------------------------------------------------------------------------------
print(first.array_x)
print(first.array_y)
plt.scatter(first.array_x,first.array_y)
plt.savefig("firstdot.png")
plt.close()

compare_position(first.array_x,first.array_y,parray_x,parray_y)
print(parray_x)
print(parray_y)
plt.scatter(parray_x,parray_y)
plt.savefig("seconddot.png")
plt.close()


def compare_radius(color,people,array_x,array_y):
  a=people
  b=0
  while b<=99:
   while  a==b and b !=99:
     b+=1
   choose_x_a=float(array_x[a])
   choose_x_b=float(array_x[b])
   choose_y_a=float(array_y[a])
   choose_y_b=float(array_y[b])
   radius=math.sqrt((choose_x_a-choose_x_b)**2+(choose_y_a-choose_y_b)**2)
   if radius<=10: 
     plt.plot([array_x[a],array_x[b]],[array_y[a],array_y[b]],color=color)
     b+=1
   b+=1
  
#---------------------------------------------------------------------------------
people3=0
while people3<=99:
 color=np.random.rand(3)
 compare_radius(color,people3,first.array_x,first.array_y)
 people3+=1
plt.scatter(first.array_x,first.array_y)
plt.savefig("first.png")
plt.close()

 
people2=0
while people2<=99:
 color=np.random.rand(3)
 compare_radius(color,people2,parray_x,parray_y)
 people2+=1
plt.scatter(parray_x,parray_y)
plt.savefig("second.png")
plt.close()


 






















 # %%
newx

# %%
