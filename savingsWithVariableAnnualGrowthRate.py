import math
import random 

monthlyContribution   = 1000    # How much you save each month
yearsSaving           = 40      # Retirement age - current age
annualSavingsIncrease = 2       # Annual rate of increase in monthly savings
initialSavings        = 10000   # How much money you start out with
avgAnnualGrowthRate   = 8       # From 1957 - 2020 AAGR was 8% including inflation
variaceInGrowthRate   = 3       # Variance in AAGR allowed (e.g. +/- 3%)
totalSavings          = initialSavings

print "Total if you invest:\n"
print '{0:>5} {1:>15} {2:>25}'.format("YEAR", "TOTAL SAVINGS", "MONTHLY CONTRIBUTION")
print("-----------------------------------------------------------------------")

# Simulate each year of investing
for year in range(yearsSaving):
	# Each year calculate growth rate factoring in variance in growth rate
	annualGrowthRate = avgAnnualGrowthRate + random.uniform(variaceInGrowthRate * -1,variaceInGrowthRate)
	monthlyCompound    = math.pow((1 + annualGrowthRate/100.0),1/12.0)

	# Each month add monthly contribution
	for months in range(12):
		totalSavings = monthlyContribution + (totalSavings * monthlyCompound)
	print '{0:>5} {1:>15} {2:>25}'.format(year, int(totalSavings), int(monthlyContribution))

	# Every year, update monthly contribution ammount to include annual savings increase
	monthlyContribution = monthlyContribution * (1 + annualSavingsIncrease/100.0)

print("-----------------------------------------------------------------------\n")

# Calculate how much money you'll have if you don't invest savings
monthlyContribution = 6000
noInterest = yearsSaving * 12 * monthlyContribution
print "Total if you don't invest: ", noInterest