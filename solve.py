import numpy as np
import math
x = []
y = []
for i in range(5):
	print('please insert {} th x coordinate:'.format(i+1))
	xi = input()
	print('your input is :{}'.format(xi))
	print('\n')
	print('please insert {} th y coordinate:'.format(i+1))
	yi = input()
	print('your input is :{}'.format(yi))
	print('------------------\n')
	x.append(float(xi))
	y.append(float(yi))

# x = [0.375,0.170,-0.085,-0.015,0.335]
# y = [0.057,-0.143,-0.038,-0.108,0.247]

A1 = []
B1 = []
C1 = []
A2 = []
B2 = []
C2 = []

XO = []
YO = []

deltaR = []
deltaR_sort = []
value_max = []

XO_result_list = []
YO_result_list = []

R = []
for i in range(5):
	for j in range(5):
		for k in range(5):
			if (i != j) and (j != k) and (i != k):
				print(i,j,k)

				x1 = x[i]
				y1 = y[i]
				x2 = x[j]
				y2 = y[j]
				x3 = x[k]
				y3 = y[k]

				A1=(2*(x2-x1))
				B1=(2*(y2-y1))
				C1=(x2**2 + y2**2 -x1**2 -y1**2)
				A2=(2*(x3-x2))
				B2=(2*(y3-y2))
				C2=(x3**2 + y3**2 -x2**2 - y2**2)


				XO.append((C1*B2-C2*B1)/(A1*B2-A2*B1))
				YO.append((A1*C2-A2*C1)/(A1*B2-A2*B1))

print(XO)
print(YO)

XO_mean = np.mean(XO)
YO_mean = np.mean(YO)
# XO_mean = float(XO_mean)
# YO_mean = float(YO_mean)
print(len(XO))
for i in range(len(XO)):
	deltaR.append((XO[i]-XO_mean)**2+(YO[i]-YO_mean)**2)
	deltaR_sort.append((XO[i]-XO_mean)**2+(YO[i]-YO_mean)**2)
deltaR_sort.sort()

print(deltaR)
print(deltaR_sort)

for i in range(30):
	value_max.append(deltaR_sort[-i-1])

print(value_max)

print('xxxx')
print(XO)
for i in range(len(XO)):
	# for j in range(len(value_max)):
	if (XO[i]-XO_mean)**2+(YO[i]-YO_mean)**2 in value_max:
		continue
	else:
		XO_result_list.append(XO[i])
		YO_result_list.append(YO[i])
print(XO_result_list)
XO_result= np.mean(XO_result_list)
YO_result= np.mean(YO_result_list)

print('\n center X ')
print(round(XO_result,5))
print(' center y')
print(round(YO_result,5))
for i in range(5):
	R.append(math.sqrt(((x[i]-XO_result)**2+(y[i]-YO_result)**2)))
print('\nradius ：')
print(R)
print('\naverage radius：')
print(round(np.mean(R),8))
print('\nvariance ：')
print(round(np.var(R),8))

fw = open('points.txt','a')
fw.write('\n')
for _ in x:
	fw.write(str(_))
	fw.write('\t')
fw.write('\n')
for _ in y:
	fw.write(str(_))
	fw.write('\t')
fw.close()

print('press any button to stop')
mm = input()