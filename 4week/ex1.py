import pandas as pd

##data를 데이터 프레임으로 만드시오.
data = {'이름' : ['Kim','Park', 'Lee','Ho'],
        '국어' : [90,58,88,100],
        '영어' : [100,60,80,70],
        '수학' : [55,65,76,88]}


#1에서 만든 데이터 프레임을 출력하시오.
print("1>--------------------------------------------")
df = pd.DataFrame(data)
print(df, end="\n\n")

name =df['이름']
print(name, end="\n\n")

parkscore =df.loc[1]
parkscore = df.loc[df['이름'] == 'Park']
print(parkscore, end="\n\n")