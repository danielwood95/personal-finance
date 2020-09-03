import math

monthlySavings = 3500
annualInterestRate = 7
yearsSaving = 41
annualSavingsIncrease = 2
monthlyCompound = math.pow((1 + annualInterestRate/100.0),1/12.0)
savings = 10000

print "Total if you invest:"
print '%12s  %12s  %12s' % ("YEAR", "TOTAL", "MONTHLY")
print("------------------------------------------")
for year in range(yearsSaving):
	for months in range(12):
		savings = monthlySavings + (savings * monthlyCompound)
	print '%12s  %12s  %12s' % (year, int(savings), int(monthlySavings))
	# print year, "\t", savings, "\t", monthlySavings
	monthlySavings = monthlySavings * (1 + annualSavingsIncrease/100.0)

print("------------------------------------------\n")

monthlySavings = 1000
noInterest = yearsSaving * 12 * monthlySavings
print "Total if you don't invest: ", noInterest