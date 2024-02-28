import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

##PART 1
dataWHO = np.genfromtxt('LifeExpectancyData.csv', delimiter= ',', usecols = (3,21), skip_header = 1)


##PART 2
data = dataWHO[~np.isnan(dataWHO).any(axis=1)]
school = data[:,1 ]
life = data[:,0]

##PART 3
#polynomial fits
d1 = Polynomial.fit(school,life, deg = 1, window = [min(school),max(school)])
d2 = Polynomial.fit(school,life, deg = 2, window = [min(school),max(school)])  #FIX: CHANGED TO A POLYNOMIAL

pnts = np.linspace(min(school), max(school) + 1, 200)
best_fit1 = np.array(list(map(lambda x : d1(x), pnts)))
best_fit2 = np.array(list(map(lambda x : d2(x), pnts)))

##PART 4
A = np.array([school,life])
AT = A.transpose()

ATA = AT@A


cATA = np.linalg.cond(ATA)
errATA = cATA * (10**-16)

print(f"The worst case for ATA is {errATA}, losing that much accuracy")


##PLOT
plt.plot(school, life, "*")
plt.plot(pnts, best_fit1)
plt.plot(pnts, best_fit2)
plt.legend([ 'School(x) vs Life Expectancy(y)', 'linear', 'quadratic'])
fileName = "regression_graph.pdf"
plt.savefig(fileName)

plt.show()



