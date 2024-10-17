
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns

hat = pd.read_csv('6week\ch4-2.csv')  # 변수에 데이터셋 입력
print(hat.describe(), end="\n\n") #기술통계값 구현 코드

font_path = "6week\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

#상자차트 그리기 
plt.figure(figsize=(10, 17))
plt.subplot(1,2,1)
plt.hist(hat.weight, bins = 7)
plt.title('b 부화장 병아리 무게 분포 현황', fontsize = 17)
plt.xlabel('병아리 무게(g)')
plt.ylabel('마릿수')

sns.histplot(hat.weight)

#plt.show()




#plt.figure(figsize=(8,10))
plt.subplot(1,2,2)
plt.boxplot(hat.weight)
plt.title('B hatchery chick weight box', fontsize =17)
plt.ylabel('weight(g)')
plt.show()