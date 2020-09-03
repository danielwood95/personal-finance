import math
import random 
import matplotlib.pyplot as plt

# Define function to calculate lifetime savings with variable annual interest
def lifetimeSavings():
	monthlyContribution   = 1000    # How much you save each month
	yearsSaving           = 40      # Retirement age - current age
	annualSavingsIncrease = 2       # Annual rate of increase in monthly savings
	initialSavings        = 1000    # How much money you start out with
	avgAnnualGrowthRate   = 8       # From 1957 - 2020 AAGR was 8% including inflation
	variaceInGrowthRate   = 3       # Variance in AAGR allowed (e.g. +/- 3%)
	totalSavings          = initialSavings

	# Simulate each year of investing
	for year in range(yearsSaving):
		# Each year calculate growth rate factoring in variance in growth rate
		annualGrowthRate = avgAnnualGrowthRate + random.uniform(variaceInGrowthRate * -1,variaceInGrowthRate)
		monthlyCompound    = math.pow((1 + annualGrowthRate/100.0),1/12.0)

		# Each month add monthly contribution
		for months in range(12):
			totalSavings = monthlyContribution + (totalSavings * monthlyCompound)

		# Every year, update monthly contribution ammount to include annual savings increase
		monthlyContribution = monthlyContribution * (1 + annualSavingsIncrease/100.0)

	# total savings for retirement
	return totalSavings

# Run 10,000 simulations to show distribution of outcomes depending on annual growth rate
trials = []
for x in xrange(10000):
	trials.append(lifetimeSavings())
num_bins = 100
n, bins, patches = plt.hist(trials, num_bins, facecolor='blue', alpha=0.5)
plt.show()
