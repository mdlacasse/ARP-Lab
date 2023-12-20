# ARP Lab
## A retirement planning laboratory

This is a tool for helping retirement planning. It generates future scenarios under different assumptions. Using this platfom, one can test the robustness of a retirement plan under historical or statistical rates of return and inflation. It can also be used to test the success of a 4% withdrawal rate, the effect of a part-time income at retirement, the possibility of purchasing of a second house in your 60's, and so on. Income tax calculations for the US federal tax are included, but no state income tax calaculations are (yet) included. If you're in Texas or Washington State, good for you!

Copyright Martin-D. Lacasse (2023)

Disclaimer: I am not a financial planner. You make your own decisions. This program comes with no garanteee. Use at your own risk.
---------------------------------------------------------------------------------------------------------------------------------

## Assumptions
ARP Lab relies on a few implicit assumptions:

- All withdrawals are taken in the following order:
    1) taxable investment accounts (CD's, bank savings accounts, stock investment accounts, etc.);
    2) tax-deferred savings accounts (e.g., 401k, 403b, etc.);
    3) tax-free savings accounts (Roth IRA, Roth 401k, etc.);
- Single and Married filing jointly are currently the only two choices for income tax calculations;
- Rates of return provided for the S&P500 include dividends;
- No investment administration fees have been accounted for;
- Contributions are assumed to be made at half-year, averaging periodic contributions evenly made through the year.
- No estate tax calculations are included.

## Default values
When a new plan is created, ARP Lab will list all the default assumptions as a reminder that they might need to be changed.
The default choices include:
- Assets allocation is 60% S&P500 and 40% corporate bonds for tax-deferred and tax-free savings accounts;
- Assets allocation is 25% corporate bonds, 55% 10-yeay Treasury bonds, and %25 common assets for taxable investment accounts;
- Income for surviving spouse will be %60 of the income of the couple;
- Spousal withdrawals are set to *auto*, allowing coordination between both accounts.
- Income tax on estate is assumed to be 25% on the taxable portion of the esate.
- Default rates are average rates over the last 30 years.


These choices have no particular value, except to provide a default case that one can run for demonstration purposes.
It is anticipated that you will change these default values by using `set___()` functions. The *jack+jill* notebook contains configuration examples describing how to make these values
match your own assumptions.


## Requirements
ARP Lab is coded in Python and is best run using *jupyterlab* or *jupyter* notebook. Therefore, I recommend installing *Anaconda* on your computer. It can be found at anaconda.com.

### Getting started
To run the demo:
1) Start the Anaconda Navigator.
2) Launch a JupyterLab session.
3) Open the *jack+jill.ipynb* notebook from the browser interface of JupyterLab.

To edit and run your own cases:
1) Make a copy of the files *template.ipynb* and *template.xlxs*.
2) Rename the copied files to something relevant to your case, say *kim+sam.ipynb* and *kim+sam.xlsx*.
3) Edit the *kim+sam.xlsx* to reflect your names, wages, contributions, and large financial events (a.k.a., big-ticket items).
4) Open *kim+sam.ipynb* notebook in the JupyterLab interface.

