import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns

def addtext(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] + 0.5, y[i], ha='center')

# 데이터 로드
hat = pd.read_csv('ch4-1.csv') 
print(hat.head(), end="\n\n")

# 폰트 설정
font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 막대 차트
plt.figure(figsize=(15, 10))
plt.bar(hat['hatchery'], hat['chick'], color=('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple'))
plt.title('Hatchery Statistics')
plt.xlabel('Hatchery')
plt.ylabel('Chick Count')
addtext(hat['hatchery'], hat['chick'])
plt.show()  # 막대 차트 표시 후 닫으면 다음 차트로 넘어감

# 파이차트
print("########## Drawing pie chart")
pct = hat['chick'] / hat['chick'].sum()
col7 = sns.color_palette('pastel', len(hat))

plt.figure(figsize=(10, 7))
plt.pie(pct, labels=hat['hatchery'], colors=col7, autopct='%1.1f%%', startangle=90)
plt.title('Proportion of Chicks by Hatchery')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()  # 파이 차트 표시

# 선 그래프
plt.figure(figsize=(10, 7))
plt.plot(hat['hatchery'], hat['chick'], marker='*', color='y', linestyle='--', linewidth=4)
plt.title('Chick Hatching Status by Hatchery')
plt.xlabel('Hatchery')
plt.ylabel('Number of Hatching')
plt.grid(True)
plt.legend(['Number of Hatching'], fontsize=10, loc='best')
plt.show()  # 선 그래프 표시