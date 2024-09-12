import pandas as pd

col_names = ['과목번호','과목명','강의실','시간수']
list1 = list([['C1','인공지능개론','R1',3],
              ['C2', '웃음치료', 'R2',2],
              ['C3', '경영학', 'R3', 3],
              ['C4', '3D디자인', 'R4', 4],
              ['C5', '스포츠경영', 'R5', 5],
              ['C6', '예술의 세계', 'R3', 1]
              ])

df = pd.DataFrame(list1, columns=col_names) #//데이터 프레임 생성
print(df)
data = {
    '과목번호' : ['C1','C2','C3','C4','C5','C6'],
    '과목명' :['인공지능개론','웃음치료','경영학','3D디자인','스포츠경영','예술의 세계'],
    '강의실' : ['R1','R2','R3','R4','R2','R3'],
    '시간수' : [3,2,3,4,2,1]
    }

df = pd.DataFrame(data)
print(df, end='\n\n')  
sr_name = df['과목명']  #// 열
print(sr_name, end='\n\n')
sr_no = df.loc[2]   #//행
print(sr_no, end='\n\n')
cell_name = df.loc[2]['과목명']   #//셀     예 df.loc[인덱스이름열이름]
print(cell_name)

df.to_csv('file.csv',index=False)

print("#############################################################")

df['담당교수'] = ['홍길동', '김철수' , '이영희' , '박영수' , '최영희' , '김영수']
print(df, end='\n\n')

df.loc[6] = ['C7', '통계학' , 'R7' , 3, '이철수']
print(df, end='\n\n')

df1 = df.drop(['강의실'], axis=1)
print(df1, end='\n\n')

df2 = df.drop([5], axis=0)
print(df2, end='\n\n')

print('##########################################################')

#범위 찾기
#행 찾기
print(df.loc[0:2], end='\n\n')
print(df.loc[0:2], end='\n\n')
#열찾기
print(df[['과목명','담당교수']], end= '\=nn=')
print(df.loc[:,'강의실' : '담당교수'], end='\n\n')

print("###############################################################")

#조건찾기
#행 찾기

print(df['과목명'] == '경영학' , end='\n\n')