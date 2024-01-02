# ARP Lab
## A retirement planning laboratory

This package is a retirement modeling framework for exploring the sensitivity of retirement financial decisions. Strictly speaking, it is not a planning tool, but more an environment for exploring *what if* scenarios. It provides different realizations of a financial strategy. One can certainly have a savings plan, but due to the volatility of financial investments, it is impossible to have an exact and certain asset earnings plan. Moreover, it is very likely that tax laws will change in the future. That does not mean that one cannot make decisions. This is where this tool fits it. Given your savings and spending desires, it can generate different future realizations of a given strategy under different market assumptions, helping to better understand one's financial situation.

Many use Excel to build their own plans using different worksheets. But there is only so much that one can do in Excel. This tool brings more capabilities, allowing for better planning by generating future scenarios under different market assumptions and graphing capabilites for comparing the different outcomes. Using this platfom, one can test the robustness of a retirement plan under historical or statistical rates of return and inflation. It can also be used to reproduce the historical success of a 4% withdrawal rate, the effect of a part-time income at retirement, the possibility of purchasing a second house in your 60's, and so on. ARP Lab is currently appropriate for U.S. individuals as federal income tax calculations are automatically performed, but no state income tax are included as of now. If you're in Texas or Washington State, you're all set!

ARP Lab requires some basic programming skills. It is written in Python and designed so that user-friendly functions can be called through an interactive jupyter notebook interface. Therefore, target users need to be young enough to have some basic Python skills (or at least have enough intellectual plasticity left to acquire those skills ;-), while being old enough to contemplate retirement. 

Copyright Martin-D. Lacasse (2023)

Disclaimer: I am not a financial planner. You make your own decisions. This program comes with no garanteee. Use at your own risk.
---------------------------------------------------------------------------------------------------------------------------------

## Capabilities
ARP Lab contains historical data from 1928 to last year and can generate scenarios using this data, or using random data
created from historical statistics. It has many graphing capabilities as well as many heuristics for optimizing wealth over the time span of a scenario. These include smart banking strategies, coordinated assets allocations between types of accounts and between spouses, and a Roth conversion optimizer using a Monte Carlo approach. 

## Rules and assumptions
ARP Lab relies on a few implicit assumptions:

- To minimize income tax, all withdrawals are taken in the following order:
    1) taxable investment accounts (CD's, bank savings accounts, stock investment accounts, etc.);
    2) tax-deferred savings accounts (e.g., 401k, 403b, etc.);
    3) tax-free savings accounts (Roth IRA, Roth 401k, etc.).
- Single and Married Filing Jointly are currently the only two choices for income tax calculations;
- Rates of return provided for the S&P 500 data include dividends;
- No investment administration fees are accounted for;
- No elaborate tax strategies are considered, such as tax-loss harvesting strategy, net unrealized appreciation, or even reduced rates on long-term capital gains;
- Contributions to savings accounts are assumed to be made at half-year, in the hope of averaging periodic contributions made evenly through the year;
- No estate tax calculations are included. Only tax on the tax-deferred portion of the estate is accounted for when reporting estate value in today's $;
- For spouses, surplus over the desired joint income will be deposited in taxable accounts proportionally to that year's spousal income ratio;
- Tax and IRMAA brackets are assumed to follow inflation;
- Social security benefits are assumed to be adjusted for inflation;
- Most importantly, tax rules are projected in the future without any consireration on likely changes to happen with new administrations. As of this release, the tax code of 2017 is assumed to be returning at the expiration of the TCJA after 2025.

## Default values for parameters
When a new plan is created, ARP Lab will list all the default assumptions as a reminder. All these parameters can be changed with simple commands.
The default choices include:

- Assets allocation is 60% S&P 500 and 40% corporate bonds for tax-deferred and tax-free savings accounts;
- Assets allocation is 25% corporate bonds, 55% 10-year Treasury notes, and %25 common assets for taxable investment accounts; 
- Income for surviving spouse will be %60 of the income of the couple; 
- Spousal withdrawals are set to *auto*, allowing coordination between both accounts; 
- Income tax on tax-deferred portion of estate is assumed to be 25% on the taxable portion of the estate; 
- Default rates are average rates over the last 30 years.

These choices have no particular value, except to provide a default case that one can run for demonstration purposes.
It is anticipated that you will change these default values by using `set___()` functions. The *jack+jill* notebook contains configuration examples describing how to make these values
match your own assumptions. These include the following calls:
    `setInitialAR()`, `setFinalAR()`, `setSurvivorFraction()`, `setSpousalSplit()`, `setDeferredTaxRate()`,  `setRates()`, for examples.

## Case studies
ARP Lab comes with a few notebooks as examples:
- [jack+jill](https://github.com/mdlacasse/ARP-Lab/blob/main/jack+jill.ipynb): describes the case of a ficticious couple about to enter retirement. This case introduces most of the capabilities of the ARP Lab platform.
- [bengen_4%](https://github.com/mdlacasse/ARP-Lab/blob/main/bengen_4%.ipynb): reproduces the 4% rule proposed by Bill Bengen in 1994. It uses unrealistically small asset values to avoid triggering income tax.
- [mary+john](https://github.com/mdlacasse/ARP-Lab/blob/main/mary+john.ipynb): explores the case of more elaborate asset allocation coordination schemes and its effect on final wealth.

## Tutorial
The best way to start is to read the file called jack+jill.ipynb. This file is meant to be run in jupyter notebook, but the file can also be read in preview mode. Once familiar with its contents, go to the next section that will get you started.

## Requirements to run this program
ARP Lab is coded in Python and is best run using either the *JupyterLab* or *jupyter* notebook. Therefore, I recommend installing *Anaconda* on your computer. It can be found at anaconda.com. Follow the instruction below to install anaconda on your computer.

The Jupyter Notebook interface is a Web-based application for authoring documents that combine live-code with narrative text, equations and visualizations.

You will also need the capability to read and edit Excel files. One can have an Excel license, or use the LibreOffice free alternative.

The intent of using a notebook is that one can configure calculations that suit one's needs. Moreover, running calculations in JupyterLab is made to be relatively easy. There are many tutorials on that topic and a summary is given [here](https://github.com/mdlacasse/ARP-Lab/blob/main/Jupyter_tutorial.md).

### Getting started
To run the demo version describing a hypothetical case:
1) Start the Anaconda Navigator. This has a green circle representative icon.
2) Launch a JupyterLab session by clicking *Launch* under the *JupyterLab* icon.
3) Using the navigation panel on the left, get to the directory where you unzipped ARP Lab.
4) Open the *jack+jill.ipynb* notebook from the browser interface of JupyterLab.
5) Follow instructions therein.

To edit files and run your own cases:
1) Make a copy of the files *template.ipynb* and *template.xlxs*.
2) Rename the copied files to something relevant to your case, say *kim+sam.ipynb* and *kim+sam.xlsx* if you are Kim and Sam.
3) Edit each tab of the *kim+sam.xlsx* file to reflect your names, wages, contributions, and large financial events (a.k.a., big-ticket items).
4) Open *kim+sam.ipynb* notebook in the JupyterLab interface.
5) Add the additional information and assumption required to run a case;
6) Give me some feedback for improvement.

