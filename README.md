# ARP Lab
## A retirement planning laboratory

This package is a retirement modeling framework for exploring the sensitivity of retirement financial decisions. Strictly speaking, it is not a planning tool, but more an environment for exploring what if scenarios. It provides different realizations of a financial strategy. One can certainly have a savings plan, but due to the volatility of financial investments, it is impossible to have an exact and certain asset earnings plan. Moreover, it is very likely that tax laws will change in the future. That does not mean one cannot make decisions. This is where this tool fits it. Given your savings and spending desires, it can generate different future realizations of your strategy under different market assumptions, helping to better understand one's financial situation.

This is a tool for helping retirement planning. It generates future scenarios under different assumptions. Using this platfom, one can test the robustness of a retirement plan under historical or statistical rates of return and inflation. It can also be used to test the success of a 4% withdrawal rate, the effect of a part-time income at retirement, the possibility of purchasing of a second house in your 60's, and so on. Income tax calculations for the US federal tax are included, but no state income tax calculations are (yet) included. If you're in Texas or Washington State, you're all set!

Copyright Martin-D. Lacasse (2023)

Disclaimer: I am not a financial planner. You make your own decisions. This program comes with no garanteee. Use at your own risk.
---------------------------------------------------------------------------------------------------------------------------------

## Rules and assumptions
ARP Lab relies on a few implicit assumptions:

- To minimize income tax, all withdrawals are taken in the following order:
    1) taxable investment accounts (CD's, bank savings accounts, stock investment accounts, etc.);
    2) tax-deferred savings accounts (e.g., 401k, 403b, etc.);
    3) tax-free savings accounts (Roth IRA, Roth 401k, etc.).
- Single and Married Filing Jointly are currently the only two choices for income tax calculations;
- Rates of return provided for the S&P 500 data include dividends;
- No investment administration fees are accounted for;
- No elaborate tax strategies are considered, such as tax-loss harvesting strategy, net unrealized appreciation, or even reduced rates on long-term capital gains.
- Contributions are assumed to be made at half-year, in the hope of averaging periodic contributions made evenly through the year.
- No estate tax calculations are included. Only tax on the tax-deferred portion of the estate is accounted for when reporting estate value in today's $.
- For spouses, surplus over the desired joint income will be deposited in taxable accounts proportionally to that year's spousal income ratio.
- Tax and IRMAA brackets are assumed to follow inflation.
- Social security are assumed to be adjusted for inflation.

## Default values for parameters
When a new plan is created, ARP Lab will list all the default assumptions as a reminder that they might need to be changed.
The default choices include:
- Assets allocation is 60% S&P 500 and 40% corporate bonds for tax-deferred and tax-free savings accounts;
- Assets allocation is 25% corporate bonds, 55% 10-yeay Treasury bonds, and %25 common assets for taxable investment accounts;
- Income for surviving spouse will be %60 of the income of the couple;
- Spousal withdrawals are set to *auto*, allowing coordination between both accounts.
- Income tax on estate is assumed to be 25% on the taxable portion of the esate.
- Default rates are average rates over the last 30 years.

These choices have no particular value, except to provide a default case that one can run for demonstration purposes.
It is anticipated that you will change these default values by using `set___()` functions. The *jack+jill* notebook contains configuration examples describing how to make these values
match your own assumptions.

## Requirements to run this program
ARP Lab is coded in Python and is best run using either the *jupyterlab* or *jupyter* notebook. Therefore, I recommend installing *Anaconda* on your computer. It can be found at anaconda.com.

### Getting started
To run the demo version describing a hypothetical case:
1) Start the Anaconda Navigator.
2) Launch a JupyterLab session.
3) Open the *jack+jill.ipynb* notebook from the browser interface of JupyterLab.

To edit files and run your own cases:
1) Make a copy of the files *template.ipynb* and *template.xlxs*.
2) Rename the copied files to something relevant to your case, say *kim+sam.ipynb* and *kim+sam.xlsx* if you are Kim and Sam.
3) Edit each tab of the *kim+sam.xlsx* file to reflect your names, wages, contributions, and large financial events (a.k.a., big-ticket items).
4) Open *kim+sam.ipynb* notebook in the JupyterLab interface.
5) Add the additional information and assumption required to run a case.

