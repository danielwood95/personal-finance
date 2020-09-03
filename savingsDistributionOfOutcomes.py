import math
import numpy as np
import random 
import matplotlib.pyplot as plt

# Define function to calculate lifetime savings with variable annual interest
def lifetimeSavings():
	monthlySavings = 6000
	yearsSaving = 40
	annualSavingsIncrease = 2
	savings = 200000
	avgAnnualInterestRate = 9
	variaceInInterest = 2
	for year in range(yearsSaving):
		annualInterestRate = avgAnnualInterestRate + random.uniform(variaceInInterest * -1,variaceInInterest)
		monthlyCompound = math.pow((1 + annualInterestRate/100.0),1/12.0)
		for months in range(12):
			savings = monthlySavings + (savings * monthlyCompound)
		monthlySavings = monthlySavings * (1 + annualSavingsIncrease/100.0)
	return savings

# Run 10,000 trials
trials = []
for x in xrange(10000):
	trials.append(lifetimeSavings())
num_bins = 100
n, bins, patches = plt.hist(trials, num_bins, facecolor='blue', alpha=0.5)
plt.show()


# monthlySavings = 6000
# yearsSaving = 40
# annualSavingsIncrease = 2
# savings = 200000
# avgAnnualInterestRate = 9
# variaceInInterest = 3

# print "Total if you invest:"
# print '{0:>10} {1:>10} {2:>10}'.format("YEAR", "TOTAL", "MONTHLY")
# print("------------------------------------------")
# for year in range(yearsSaving):
# 	annualInterestRate = 7 + random.uniform(variaceInInterest * -1,variaceInInterest)
# 	monthlyCompound = math.pow((1 + annualInterestRate/100.0),1/12.0)
# 	for months in range(12):
# 		savings = monthlySavings + (savings * monthlyCompound)
# 	print '{0:>10} {1:>10} {2:>10}'.format(year, int(savings), int(monthlySavings))
# 	monthlySavings = monthlySavings * (1 + annualSavingsIncrease/100.0)

# print("------------------------------------------\n")

# monthlySavings = 6000
# noInterest = yearsSaving * 12 * monthlySavings
# print "Total if you don't invest: ", noInterest