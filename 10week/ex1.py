import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w=pd.read_csv('ch5-1.csv')
w_n= w.iloc[:,1:5]  #weight 15

model_lm = smf.ols(formula = 'weight ~ egg_weight', data = w_n) ##포뮬러 결과변수 앞에 지정하고 ~ 원인변수 데이터는 위에 잡아놓은거 쓴거임  ##회귀모델 세팅
result_lm = model_lm.fit()  #학습
result_lm.summary()
print(result_lm.summary()) ##결과

plt.figure(figsize= (10,7))
plt.scatter(w.egg_weight, w.weight, alpha = .5)
plt.plot(w.egg_weight, w.egg_weight*2.3371 - 14.5475, color ='red')
plt.text(66,132,'weight = 2.337legg_weight- 14.5475', fontsize =12)
plt.title('Scatter Plot')
plt.xlabel('egg_weight')
plt.ylabel('weight')
plt.show()