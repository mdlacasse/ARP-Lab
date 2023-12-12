import retirement as rp

plan = rp.Plan(YOB=[1958, 1961], expectancy=[91, 92])

rp.setVerbose(True)

plan.setAssetBalances(taxable=[500000, 500000],
                      taxDeferred=[1000000, 500000],
                      taxFree=[100000, 100000],
                      beneficiary=[1., 1.])

plan.setAssetRatios(taxableR=[[0, .5, .5], [0, .5, .5]],
                    taxDeferredR=[[.6, .4, 0.], [.6, .4, 0]],
                    taxFreeR=[[.8, .2, 0], [.8, .2, 0]])

# Specify rate of returns for each class of assets.
# Valid entries are 'historical', 'stochastic', or a list of average values.
myrates = [0.09, 0.04, 0.03, 0.038]
plan.setRates(None)

# Enter desired value for net income in retirementi, and spending profile.
plan.setDesiredIncome(150000, 'smile')

# How to handle withdrawals between spouses.
plan.setSpousalSplit('auto')

# Now enter fixed income.\n",
plan.setPension([0, 10000], [65, 65])

# And social security income.
plan.setSocialSecurity([40000, 30000], [70, 70])

# Name of spreadsheet containing financial events (contributions, etc).
plan.readContributions('timeHorizon.xlsx')
