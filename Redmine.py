#!/usr/bin/env python
# coding: utf-8


#Ticker(이슈) Type
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import seaborn as sns

# 한글깨짐 방지 및 폰트 설정 (맑은고딕)
font_location = 'C:/Windows/Fonts/MALGUNSL.TTF' 
font_name = font_manager.FontProperties(fname=font_location).get_name()
rc('font',family=font_name)

df = pd.read_csv('issues.csv', encoding='cp949')
# df

#그래프 설정
ax2 = plt.subplots()
ax2 = sns.countplot(x='유형', data=df, palette='Set1')
ax2.set_title('<이슈 유형>',size = 15)
ax2.set_xlabel('', size = 10)
ax2.set_ylabel('', size=10, rotation=0)


#축 텍스트 크기 및 색상조절
plt.xticks(color='black', fontsize =13)
plt.yticks(color='black', fontsize =11.5)


#y축 범위를 지정
# plt.axis([0, 5, 0, 20])  # X, Y축의 범위: [xmin, xmax, ymin, ymax]
plt.ylim([0, 1000]) 



#Count 표시
for p in ax2.patches:
    left, bottom, width, height = p.get_bbox().bounds
    plt.annotate(f"{int(height)}",(left+width/2, height+30), ha = 'center', size =13, color = 'Black')

    
    
plt.savefig('ex.png', dpi=200)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




