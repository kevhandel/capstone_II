
<img src='figs/rookie_10.png'>
### CNNs in the Frequency Domain

<p>&nbsp;

### Motivation and Background...

* Data on the amounts of each chemical traveling in any of the 60+ streams are delivered through self-reporting.
* Complete sets are available for years 1987 - 2016, inclusive.

* Do fates of chemicals predictable and reliably evolve over time?
* Can identified trends be correlated with enhanced Federal and/or local environmental regulations?  Might we become able to better predict the effect of future proposed regulation?
* Is the early data detectably padded due to the very lax reporting standards
which, anecdotally, resulted in over-reporting of certain hazardous chemicals?
* Are trends toward more society-wide recycling apparent in industry as well?

The primary goal was to plot a few fates of select chemicals in order to test for industry-wide evolution in chemical fate.
Quantification would involve Hypothesis Testing.

As the database contains no information regarding environmental regulation, regression testing to model the effects
of regulations would require merging this data with a secondary regulations database.
<p>&nbsp;

### Investigation...

* We found many rows with NaN values.  As these appeared to exist due to the expansion in the reporting options from original conception,
no data imputation was warranted at the early stage of exploration.
We then split the dataframe into 613 dataframes each of which housed the data for a unique chemical, and stored these as csv files.
* Each dataframe contained the 66 columns related to fate, and the file names were coded according to chemical name, which meant that the future process of querying any given chemical could be fairly well automated.  A lookup function initially queried the monster file for chemical names, and then stored these in a separate tiny file to be accessed at the startup of each session.
<p>&nbsp;

### Start the EDA...

<p>&nbsp;

### Graphing by the 1000's...
<table>
</table>

<p>&nbsp;

### Gathering Data...
<p>&nbsp;


### Results...
<p>&nbsp;

### Looking Ahead...

<p>&nbsp;

### Data Sources...
Many Thanks to:
