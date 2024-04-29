# Practice Exercises for Summarizing Retail Data

## Overview

In this exercise set, you'll get a chance to practice your skills in grouping and aggregating retail data. First, take a moment to review the core concepts that you've been introduced to. Then, proceed with the exercises provided below.

As always, these exercises are for your own understanding and practice. You're encouraged to attempt all of them for better grasp of the topic.

## Core Concepts

### Loading Data with Different Methods

You've seen two methods of loading data: directly from an Excel file and using Feather for faster loading.

Examples:

```python
sales = pd.read_excel('data/Online Retail.xlsx')
```

and 

```python
sales_f = pd.read_feather('data/Online Retail.fth')
```

### Exploratory Data Analysis (EDA)

EDA involves getting a basic understanding of the dataset, its structure, and any patterns or peculiarities within it.

### Grouping Data using pandas

Using `groupby()` in pandas, you can group data based on certain criteria.

Example:

```python
sales.groupby('Country').sum()
```

### Plotting Data

You can visualize aggregated data using different types of plots to derive insights.

Example:

```python
sales.groupby('Country').sum().plot.bar()
```

### Aggregating Data

Aggregating data helps summarize it. Common aggregation functions include `sum()`, `mean()`, `count()`, among others.
