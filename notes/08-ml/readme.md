# Simple Machine Learning with Pandas

## Overview

In this module, we delve into the foundational steps of machine learning using the pandas library. By the end, you'll have a grasp on:

- How to prepare your data for analysis.
- Methods to explore and visualize your data.
- Techniques to clean and preprocess the data.
- Ways to create, tune, and evaluate machine learning models.

## Core Concepts

### Data Acquisition

Before diving into analysis or modeling, you need to acquire and load your data. The sample here uses a heart disease dataset from the UCI Machine Learning repository.

Example:

```python
import numpy as np
import pandas as pd
import glob

names = [...]
files = glob.glob('data/processed*.data')
df = pd.concat([pd.read_csv(f, sep=',',names=names, na_values='?',...)])
```

### Data Exploration

To understand the structure and patterns in your data, you should visualize and summarize it.

Examples:

```python
df.dtypes
heart.groupby('num').mean(numeric_only=True)
```

### Data Cleaning

The quality of the data determines the quality of the model. Cleaning includes handling missing values, converting data types, and more.

Example:

```python
def tweak_heart(df): 
  ...
heart = tweak_heart(df)
```

### Model Creation

Using algorithms and libraries like XGBoost, you can train a model on your data.

Example:

```python
import xgboost as xg
from sklearn import model_selection

X_train, X_test, y_train, y_test = ...
xgb = xg.XGBClassifier(...)
xgb.fit(X_train, y_train)
```

### Model Tuning

To improve model performance, you can adjust its parameters. Hyperopt is an optimization tool for this purpose.

Example:

```python
from hyperopt import fmin, tpe, hp, ...
params = {'random_state': 42}
...
best = fmin(...)
```

### Model Evaluation

After tuning, it's essential to evaluate your model on test data and visualize its performance using techniques like confusion matrices.

Example:

```python
xgb_step.score(X_test, y_test)
metrics.ConfusionMatrixDisplay.from_estimator(...)
```