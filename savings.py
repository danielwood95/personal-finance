import math

monthlyContribution = 1000   # How much you save each month
annualInterestRate = 7      # Annual growth rate
yearsSaving = 40            # Retirement age - current age
annualSavingsIncrease = 2   # Annual rate of increase in monthly savings
initialSavings = 10000
totalSavings = initialSavings
monthlyCompound = math.pow((1 + annualInterestRate/100.0),1/12.0)


print "Total if you invest:"
print '%12s  %12s  %12s' % ("YEAR", "TOTAL", "MONTHLY")
print("------------------------------------------")
for year in range(yearsSaving):
	for months in range(12):
		totalSavings = monthlyContribution + (totalSavings * monthlyCompound)
	print '%12s  %12s  %12s' % (year, int(totalSavings), int(monthlyContribution))
	monthlyContribution = monthlyContribution * (1 + annualSavingsIncrease/100.0)

print("------------------------------------------\n")

monthlyContribution = 1000
totalSavingsWithoutInvesting = yearsSaving * 12 * monthlyContribution
print "Total if you don't invest: ", totalSavingsWithoutInvesting
