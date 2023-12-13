import retirement as rp
import matplotlib.pyplot as plt

rp.setVerbose(True)

plan = rp.Plan(YOB=[1960, 1960], expectancy=[90, 92])

plan.setAssetBalances(taxable=[500000, 500000],
                      taxDeferred=[1000000, 500000],
                      taxFree=[100000, 100000],
                      beneficiary=[1., 1.])

plan.setInitialAR(taxableAR=[[0, 50, 50], [0, 50, 50]],
                  taxDeferredAR=[[60, 40, 0], [60, 40, 0]],
                  taxFreeAR=[[80, 20, 0], [80, 20, 0]])

plan.setFinalAR(taxableAR=[[0, 50, 50], [0, 50, 50]],
                taxDeferredAR=[[60, 40, 0], [60, 40, 0]],
                taxFreeAR=[[80, 20, 0], [80, 20, 0]])

plan.interpolateAR('linear')

# Specify rate of returns for each class of assets.
# Valid entries are 'historical', 'stochastic', 'default',
# or a list of fixed average values.
myrates = [6.0, 5.0, 3.0, 3.08]
plan.setRates(myrates)
# plan.setRates('default')
# plan.setRates('historical', 1928, 2022)
# plan.setRates('historical', 1998, 2022)
# plan.setRates('stochastic', 1928, 2022)

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

plan.run()

plan.plotAccounts()
plan.plotTaxableIncome()
plan.plotNetIncome()
plan.plotSources()


plt.show(block=False)
plt.pause(0.001)
while True:
    key = input(
        "[Enter] 'q' to quit, or 's' to save: ")
    if key == 'q':
        plt.close("all")
        break
    elif key == 's':
        plot.saveXL('something')
        break
