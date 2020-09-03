import math
import random 

# Accounts
_401k              = 0   # Pre-tax retirement account (taxed on withdrawls)
roth401k           = 0   # After-tax retirement account (taxed on contributions)
brokerageTotal     = 0   # After-tax brokerage account (gains taxed at long-term capital gains tax rate)
brokeragePrincipal = 0   # After-tax brokerage principal (total brokerage contributions, no gains)

# Contributions
annualContribution  = 19500.0                    # Before tax (max contribution allowed is 19500 in 2020)
monthlyContribution = annualContribution / 12.0  # Before tax
yearsSaving         = 40                         # 65 - current age

# Growth
avgAnnualGrowthRate = 8.0  # From 1957 - 2020 AAGR was 10% - 2% inflation = 8%
variaceInGrowthRate = 0    # Variance in AAGR (e.g. +/- 3%)

# Tax rates
currentEffectiveIncomeTaxRate = 21.45  	# 2020 effective tax rate (not highest tax bracket)
longTermCapitalGain           = 15.0    # Long term capital gains rate (held stock over 1 year)
futureEffectiveIncomeTaxRate  = 28.0    # Effective tax rate in year of retirement
effectiveTaxRate              = currentEffectiveIncomeTaxRate

# Simulate lifetime savings for each account
for year in range(yearsSaving):

	# Calculate a growth rate for year based on avg and variance
	annualGrowthRate = avgAnnualGrowthRate + random.uniform(variaceInGrowthRate * -1,variaceInGrowthRate)
	monthlyCompound  = math.pow((1 + annualGrowthRate/100.0),1/12.0)

	# Add monthly contribution to each account
	for months in range(12):
		# Calculate updated value of 401k
		_401k                 = monthlyContribution + (_401k * monthlyCompound)

		# Calculate updated value of roth401k
		afterTaxContribution = monthlyContribution * (1 - (effectiveTaxRate/100))
		roth401k             = afterTaxContribution + (roth401k * monthlyCompound)

		# Calculate updated value of brokerage account
		afterTaxContribution = monthlyContribution * (1 - (effectiveTaxRate/100))
		brokerageTotal       = afterTaxContribution + (brokerageTotal * monthlyCompound)
		brokeragePrincipal   = afterTaxContribution + brokeragePrincipal 

	# Recalculate tax rate for the next year
	changeInTaxRate  = (futureEffectiveIncomeTaxRate - currentEffectiveIncomeTaxRate) / yearsSaving
	effectiveTaxRate = effectiveTaxRate + changeInTaxRate
 
	# Print snapshot of each account every year
	# print '%12s  %12s  %12s  %12s' % (year, int(_401k), int(roth401k), int(brokerageTotal))

# Show account values at retirement
print "401k:                ", _401k * (1 - (futureEffectiveIncomeTaxRate/100)) # Taxed at future effective income tax rate
print "roth401k:            ", roth401k											# Not taxed
brokerageGains = brokerageTotal - brokeragePrincipal 							# Calculate gains in brokerage account
print "brokerage before tax:", brokerageTotal									# Brokerage gains taxed at long-term capital gains tax rate
print "brokerage gains:     ", brokerageGains
print "brokerage principal:  ", brokeragePrincipal
print "brokerage after tax: ", brokerageTotal - (brokerageGains * (longTermCapitalGain/100))







