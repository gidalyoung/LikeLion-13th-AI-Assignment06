import pandas as pd

# 데이터셋 준비
birth_df = pd.read_csv('birth_rate.csv')
birth_df.head()

birth_25_29 = birth_df.query('연령대 == "25-29세"') # 25~29세 데이터만 필터링
birth_30_34 = birth_df.query('연령대 == "30-34세"') # 30~34세 데이터만 필터링

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'])
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'])

# 코드잇 실행기
plt.rc('font', family='NanumGothic')
# Windows
plt.rc('font', family='Malgun Gothic')

fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세') # 범례를 붙이려면, 각각에 label을 꼭 붙여줘야 함
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세')
ax.legend() # 범례 붙이기

fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세') # 범례를 붙이려면, 각각에 label을 꼭 붙여줘야 함
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세')
ax.legend() # 범례 붙이기
ax.set_title('여성 천명당 출생아수: 연령대별 추이') # 제목 붙이기
ax.set_xlabel('연도') # x축 라벨 붙이기
ax.set_ylabel('여성 천명당 출생아수') # y축 라벨 붙이기

import numpy as np
plt.show()
plt.close(fig)
fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세') # 범례를 붙이려면, 각각에 label을 꼭 붙여줘야 함
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세')
ax.legend() # 범례 붙이기
ax.set_title('여성 천명당 출생아수: 연령대별 추이') # 제목 붙이기
ax.set_xlabel('연도') # x축 라벨 붙이기
ax.set_ylabel('여성 천명당 출생아수') # y축 라벨 붙이기
ax.set_yticks(np.arange(0, 110, 10)) # 0 ~ 100까지 10 간격으로 y축 눈금을 표기

fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세') # 범례를 붙이려면, 각각에 label을 꼭 붙여줘야 함
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세')
ax.legend() # 범례 붙이기
ax.set_title('여성 천명당 출생아수: 연령대별 추이') # 제목 붙이기
ax.set_xlabel('연도') # x축 라벨 붙이기
ax.set_ylabel('여성 천명당 출생아수') # y축 라벨 붙이기
ax.set_yticks(np.arange(0, 110, 10)) # 0 ~ 100까지 10 간격으로 y축 눈금을 표기
ax.set_xticks(birth_25_29['시점'], labels=[f'{i}년' for i in birth_25_29['시점']])
# 'YYYY년'의 형태로 x라벨 업데이트

fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세') # legend를 붙이려면, 각각에 label을 꼭 붙여줘야 함
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세')
ax.legend() # legend 붙이기

ax.set_title('여성 천명당 출생아수: 연령대별 추이') # 제목 붙이기
ax.set_xlabel('연도') # x축 라벨 붙이기
ax.set_ylabel('여성 천명당 출생아수') # y축 라벨 붙이기
ax.set_yticks(np.arange(0, 110, 10)) # 0 ~ 100까지 10 간격으로 y축 눈금을 표기
ax.set_xticks(birth_25_29['시점'], labels=[f'{i}년' for i in birth_25_29['시점']],
rotation=30) # 'YYYY년'의 형태로 x라벨 업데이트, 30도 회전
plt.show()
plt.close(fig)

fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세') # 범례를 붙이려면, 각각에 label을 꼭 붙여줘야 함
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세')
ax.legend() # 범례 붙이기
ax.set_title('여성 천명당 출생아수: 연령대별 추이') # 제목 붙이기
ax.set_xlabel('연도') # x축 라벨 붙이기
ax.set_ylabel('여성 천명당 출생아수') # y축 라벨 붙이기
ax.set_yticks(np.arange(0, 110, 10)) # 0 ~ 100까지 10 간격으로 y축 눈금을 표기
ax.set_xticks(birth_25_29['시점'], labels=[f'{i}년' for i in birth_25_29['시점']],
rotation=30) # 'YYYY년'의 형태로 x라벨 업데이트, 30도 회전
plt.show()
plt.close(fig)

# 상단 및 우측 spine 제거
ax.spines.top.set_visible(False)
ax.spines.right.set_visible(False)

fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세') # 범례를 붙이려면, 각각에 label을 꼭 붙여줘야 함
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세')
ax.legend() # 범례 붙이기
ax.set_title('여성 천명당 출생아수: 연령대별 추이') # 제목 붙이기
ax.set_xlabel('연도') # x축 라벨 붙이기
ax.set_ylabel('여성 천명당 출생아수') # y축 라벨 붙이기
ax.set_yticks(np.arange(0, 110, 10)) # 0 ~ 100까지 10 간격으로 y축 눈금을 표기
ax.set_xticks(birth_25_29['시점'], labels=[f'{i}년' for i in birth_25_29['시점']],
rotation=30) # 'YYYY년'의 형태로 x라벨 업데이트, 30도 회전
plt.show()
plt.close(fig)
# 상단 및 우측 spine 제거
ax.spines.top.set_visible(False)
ax.spines.right.set_visible(False)
ax.grid(axis='y', linestyle=':', color='lightgrey') # y축에만 Grid 추가, 점선 스타일, 연회색

fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세', linewidth=2, linestyle='--') # linewidth, linestyle 설정
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세', color='skyblue', marker='o') # line color & marker 설정
ax.legend() # 범례 붙이기
ax.set_title('여성 천명당 출생아수: 연령대별 추이') # 제목 붙이기
ax.set_xlabel('연도') # x축 라벨 붙이기
ax.set_ylabel('여성 천명당 출생아수') # y축 라벨 붙이기
ax.set_yticks(np.arange(0, 110, 10)) # 0 ~ 100까지 10 간격으로 y축 눈금을 표기
ax.set_xticks(birth_25_29['시점'], labels=[f'{i}년' for i in birth_25_29['시점']],rotation=30) # 'YYYY년'의 형태로 x라벨 업데이트, 30도 회전
# 상단 및 우측 spine 제거
ax.spines.top.set_visible(False)
ax.spines.right.set_visible(False)
ax.grid(axis='y', linestyle=':', color='lightgrey') # y축에만 Grid 추가, 점선 스타일, 연회색

import pandas as pd
plt.show()
plt.close(fig)
sns_df = pd.read_csv('social_media_stocks.csv')
sns_df.head()

# Year 분리
sns_df['Year'] = sns_df['Date'].str.split('-', expand=True)[0]
# 기업별 연도별 평균 주식 종가 계산
sns_close_df = sns_df.groupby(['Year', 'Symbol'])[['Close']].mean().reset_index()
# Meta(Facebook)과 X(Twitter) 데이터 각각 저장
fb_stock_close = sns_close_df.query('Symbol == "FB"')
twtr_stock_close = sns_close_df.query('Symbol == "TWTR"')

import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(1, 2)
fig, axes = plt.subplots(1, 2)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
# ax1: Meta(Facebook)의 연도별 평균 주식 종가
ax1.plot(fb_stock_close['Year'], fb_stock_close['Close'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
# ax1: Meta(Facebook)의 연도별 평균 주식 종가
ax1.plot(fb_stock_close['Year'], fb_stock_close['Close'])

# ax2: X(Twitter)의 연도별 평균 주식 종가
ax2.plot(twtr_stock_close['Year'], twtr_stock_close['Close'])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
# ax1: Meta(Facebook)의 연도별 평균 주식 종가
ax1.plot(fb_stock_close['Year'], fb_stock_close['Close'], color='teal', marker='o')
# ax2: X(Twitter)의 연도별 평균 주식 종가
ax2.plot(twtr_stock_close['Year'], twtr_stock_close['Close'])
## ax1 그래프 커스터마이징
ax1.set_title('Yearly Average Close Price of FB')
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Stock Close Price')
ax1.grid(axis='y', linestyle='--', color='lightgrey')
ax1.spines[['top', 'right']].set_visible(False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
# ax1: Meta(Facebook)의 연도별 평균 주식 종가
ax1.plot(fb_stock_close['Year'], fb_stock_close['Close'], color='teal', marker
='o')
# ax2: X(Twitter)의 연도별 평균 주식 종가
ax2.plot(twtr_stock_close['Year'], twtr_stock_close['Close'], color='palevioletred', marker='o')
## ax1 그래프 커스터마이징
ax1.set_title('Yearly Average Close Price of FB')
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Stock Close Price')
ax1.grid(axis='y', linestyle='--', color='lightgrey')
ax1.spines[['top', 'right']].set_visible(False)
## ax2 그래프 커스터마이징
ax2.set_title('Yearly Average Close Price of TWTR')
ax2.set_xlabel('Year')
ax2.set_ylabel('Average Stock Close Price')
ax2.grid(axis='y', linestyle='--', color='lightgrey')
ax2.spines[['top', 'right']].set_visible(False)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# ax1: Meta(Facebook)의 연도별 평균 주식 종가
axes[0].plot(fb_stock_close['Year'], fb_stock_close['Close'], color='teal', marker='o')
# ax2: X(Twitter)의 연도별 평균 주식 종가
axes[1].plot(twtr_stock_close['Year'], twtr_stock_close['Close'], color='palevioletred', marker='o')
axes[0].set_title('Yearly Average Close Price of FB')
axes[1].set_title('Yearly Average Close Price of TWTR')
for ax in axes:
 ax.set_xlabel('Year')
 ax.set_ylabel('Average Stock Close Price')
 ax.grid(axis='y', linestyle='--', color='lightgrey')
 ax.spines[['top', 'right']].set_visible(False)

snap_stock_close = sns_close_df.query('Symbol == "SNAP"')
fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(8, 9))
fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(8, 9))

# ax1: Meta(Facebook)의 연도별 평균 주식 종가
ax1.plot(fb_stock_close['Year'], fb_stock_close['Close'])
# ax2: X(Twitter)의 연도별 평균 주식 종가
ax2.plot(twtr_stock_close['Year'], twtr_stock_close['Close'])
# ax3: Snap의 연도별 평균 주식 종가
ax3.plot(snap_stock_close['Year'], snap_stock_close['Close'])

fig, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, figsize=(8, 9), constrained_layout=True)
# ax1: Meta(Facebook)의 연도별 평균 주식 종가
ax1.plot(fb_stock_close['Year'], fb_stock_close['Close'], color='teal', marker='o')
# ax2: X(Twitter)의 연도별 평균 주식 종가
ax2.plot(twtr_stock_close['Year'], twtr_stock_close['Close'], color='palevioletred', marker='o')
# ax3: Snap의 연도별 평균 주식 종가
ax3.plot(snap_stock_close['Year'], snap_stock_close['Close'], color='goldenrod', marker='o')
# Figure 차원의 전체 제목, x & y 라벨 추가
fig.suptitle('Yearly Average Close Price', fontsize=16)
fig.supxlabel('Year')
fig.supylabel('Averaged Stock Close Price')

## ax1 그래프 커스터마이징
ax1.set_title('FB', loc='left')
ax1.grid(axis='y', linestyle='--', color='lightgrey')
## ax2 그래프 커스터마이징
ax2.set_title('TWTR', loc='left')
ax2.grid(axis='y', linestyle='--', color='lightgrey')
## ax3 그래프 커스터마이징
ax3.set_title('SNAP', loc='left')
ax3.grid(axis='y', linestyle='--', color='lightgrey')

fig, ax = plt.subplots()
ax.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세', linewidth=2, linestyle='--') # linewidth, linestyle 설정
ax.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세', color='skyblue', marker='o') # line color & marker 설정
ax.legend() # 범례 붙이기
ax.set_title('여성 천명당 출생아수: 연령대별 추이') # 제목 붙이기
ax.set_xlabel('연도') # x축 라벨 붙이기
ax.set_ylabel('여성 천명당 출생아수') # y축 라벨 붙이기
ax.set_yticks(np.arange(0, 110, 10)) # 0 ~ 100까지 10 간격으로 y축 눈금을 표기
ax.set_xticks(birth_25_29['시점'], labels=[f'{i}년' for i in birth_25_29['시점']],
rotation=30) # 'YYYY년'의 형태로 x라벨 업데이트, 30도 회전
plt.show()
plt.close(fig)
# 상단 & 우측 spine 제거
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
ax.grid(axis='y', linestyle=':', color='lightgrey') # y축에만 Grid 추가, 점선 스타일, 연회색

plt.plot(birth_25_29['시점'], birth_25_29['여성 천명당 출생아수'], label='25~29세', linewidth=2, linestyle='--') # linewidth, linestyle 설정
plt.plot(birth_30_34['시점'], birth_30_34['여성 천명당 출생아수'], label='30~34세', color='skyblue', marker='o') # line color & marker 설정
plt.legend() # legend 붙이기
plt.title('여성 천명당 출생아수: 연령대별 추이') # 제목 붙이기
plt.xlabel('연도') # x축 라벨 붙이기
plt.ylabel('여성 천명당 출생아수') # y축 라벨 붙이기

plt.yticks(np.arange(0, 110, 10)) # 0 ~ 100까지 10 간격으로 y축 눈금을 표기
plt.xticks(birth_25_29['시점'], labels=[f'{i}년' for i in birth_25_29['시점']], rotation=30) # 'YYYY년'의 형태로 x라벨 업데이트, 30도 회전
plt.grid(axis='y', linestyle=':', color='lightgrey') # y축에만 grid 추가, 점선 스타일, 연회색

plt.figure(figsize=(12, 4))
# 좌측: Meta(Facebook)의 연도별 평균 주식 종가
plt.subplot(1, 2, 1) # nrows=1 ncols=2, index=1
plt.plot(fb_stock_close['Year'], fb_stock_close['Close'])
# 우측: X(Twitter)의 연도별 평균 주식 종가
plt.subplot(1, 2, 2) # nrows=1 ncols=2, index=2
plt.plot(twtr_stock_close['Year'], twtr_stock_close['Close'])

# Object-oriented 방식: subplots()로 figure와 두 개의 axes를 모두 생성해둔 후,하나씩 작업
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
plt.show()
plt.close(fig)
ax1.plot(fb_stock_close['Year'], fb_stock_close['Close'])
ax2.plot(twtr_stock_close['Year'], twtr_stock_close['Close'])

# State-based 방식: 그때그때 subplot을 생성하기 전에 plt.subplot()을 적어줘야함
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(fb_stock_close['Year'], fb_stock_close['Close'])
plt.subplot(1, 2, 2)
plt.plot(twtr_stock_close['Year'], twtr_stock_close['Close'])

plt.figure(figsize=(12, 4))
# 좌측: Meta(Facebook)의 연도별 평균 주식 종가
plt.subplot(1, 2, 1) # nrows=1 ncols=2, index=1
plt.plot(fb_stock_close['Year'], fb_stock_close['Close'])
# 우측: X(Twitter)의 연도별 평균 주식 종가
plt.subplot(1, 2, 2) # nrows=1 ncols=2, index=2
plt.plot(twtr_stock_close['Year'], twtr_stock_close['Close'])
# 그래프 커스터마이징
plt.title('제목 추가')
plt.xlabel('x라벨 추가')
plt.ylabel('y라벨 추가')
plt.grid(axis='y', linestyle=':')

plt.figure(figsize=(12, 4))
# 좌측: Meta(Facebook)의 연도별 평균 주식 종가
plt.subplot(1, 2, 1) # nrows=1 ncols=2, index=1
plt.plot(fb_stock_close['Year'], fb_stock_close['Close'], color='teal', marker
='o')
plt.show()
plt.close(fig)
plt.title('Yearly Average Close Price of FB')
plt.xlabel('Year')
plt.ylabel('Average Stock Close Price')
plt.grid(axis='y', linestyle='--', color='lightgrey')
# 우측: X(Twitter)의 연도별 평균 주식 종가
plt.subplot(1, 2, 2) # nrows=1 ncols=2, index=2
plt.plot(twtr_stock_close['Year'], twtr_stock_close['Close'], color='palevioletred', marker='o')
plt.title('Yearly Average Close Price of TWTR')
plt.xlabel('Year')
plt.ylabel('Average Stock Close Price')
plt.grid(axis='y', linestyle='--', color='lightgrey')

fig, axes = plt.subplots(1, 2, figsize=(12, 4))
# ax1: Meta(Facebook)의 연도별 평균 주식 종가
axes[0].plot(fb_stock_close['Year'], fb_stock_close['Close'], color='teal', marker='o')
# ax2: X(Twitter)의 연도별 평균 주식 종가
axes[1].plot(twtr_stock_close['Year'], twtr_stock_close['Close'], color='palevioletred', marker='o')
axes[0].set_title('Yearly Average Close Price of FB')
axes[1].set_title('Yearly Average Close Price of TWTR')
for ax in axes:
 ax.set_xlabel('Year')
 ax.set_ylabel('Average Stock Close Price')
 ax.grid(axis='y', linestyle='--', color='lightgrey')
 ax.spines[['top', 'right']].set_visible(False)