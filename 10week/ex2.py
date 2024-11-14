import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

w=pd.read_csv('ch5-1.csv')
w_n= w.iloc[:,1:5]  #weight 15

model_lm = smf.ols(formula = 'weight ~ food', data = w_n) ##포뮬러 결과변수 앞에 지정하고 ~ 원인변수 데이터는 위에 잡아놓은거 쓴거임  ##회귀모델 세팅
result_lm = model_lm.fit()  #학습
result_lm.summary()
print(result_lm.summary()) ##결과
##
plt.figure(figsize= (10,7))
plt.scatter(w.food, w.weight, alpha = .5)
plt.plot(w.food, w.food*4.6684 + 78.1551, color ='red')
plt.text(13,130,'weight = 4.6684legg_weight+ 78.1551', fontsize =12)
plt.title('Scatter Plot')
plt.xlabel('food')
plt.ylabel('weight')
plt.show()

















