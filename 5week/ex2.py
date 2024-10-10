import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import seaborn as sns

def addtext(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] + 0.5, y[i], ha='center')

# 데이터 로드
singer = pd.read_csv('singer_youtube.csv') 
print(singer.head(), end="\n\n")

# 폰트 설정
font_path = "malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font_name)

# 막대 차트
plt.figure(figsize=(15, 10))
plt.bar(singer['name'], singer['youtube count'], color=('red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple', 'black', 'white', 'pink'))
plt.title('youtube countby singer')  # 차트 제목 수정
plt.xlabel('name')  # X축 레이블 수정
plt.ylabel('Youtube count')  # Y축 레이블 수정
addtext(singer['name'], singer['youtube count'])  # X축 값을 singer['name']으로 수정

plt.show()