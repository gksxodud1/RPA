import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w= pd.read_csv('ch5-1.csv')
w_n = w.iloc[:,1:5]
model_lm = smf.ols(formula = 'weight ~ food', data = w_n)
result_lm = model_lm.fit()
result_lm.summary()
print(result_lm.summary())