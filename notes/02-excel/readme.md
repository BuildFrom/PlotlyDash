# Practice Exercises for Working with Excel in Python

## Overview

In this exercise section, you'll get to apply what you've learned about working with Excel files in Python. These exercises are designed to reinforce the main concepts you've learned in the sample. Ensure you go through each step, and remember, practice is the key to mastering any skill.

## Core Concepts

### Loading Excel files

Python, with the help of libraries like `pandas`, can read Excel files directly into DataFrames.

Example:
```python
import pandas as pd
df = pd.read_excel('data/adult.xlsx', index_col=0)
```

### Writing Excel files

`pandas` can also write DataFrames to Excel files. You can further customize the appearance of the Excel file with `XlsxWriter`.

Example:
```python
writer = pd.ExcelWriter('data/pandas_output.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
```

### Finding missing data

You can detect missing data in your DataFrame, calculate the mean of missing data in columns, and visualize the distribution of missing data.

Examples:
```python
df.isna()
df.isna().sum()
```

### Analyzing Text data

`pandas` allows you to filter and visualize text (string) data in your DataFrame.

Examples:
```python
df.education.value_counts().plot.barh()
```

### Numerical Analysis

Correlations between numerical columns, histograms, and scatter plots can be made to analyze relationships and distributions.

Examples:
```python
df.corr()
df.age.hist(bins=20)
```

### Creating scatter plots

Scatter plots can visualize relationships between two numerical columns.

Example:
```python
df.plot.scatter(x='education-num', y='capital-gain')
```