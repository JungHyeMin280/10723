import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 예제 데이터를 위한 DataFrame 생성
data = {
    '지역': ['서울', '부산', '대구', '인천', '광주'],
    '20대_인구': [250000, 80000, 60000, 50000, 40000],
    '전체_인구': [1000000, 500000, 400000, 300000, 200000]
}
df = pd.DataFrame(data)
df['20대_비율'] = df['20대_인구'] / df['전체_인구']

# Streamlit 앱 구현
st.title('20대 인구 비율 원 그래프')

# 지역 선택
selected_region = st.selectbox('지역 선택', df['지역'])

# 선택된 지역의 데이터 추출
selected_data = df[df['지역'] == selected_region].iloc[0]
age_ratio = selected_data['20대_비율']

# 원 그래프 그리기
fig, ax = plt.subplots()
labels = ['20대 인구', '기타']
sizes = [age_ratio, 1 - age_ratio]
colors = ['#ff9999','#66b3ff']

ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# 그래프를 Streamlit 앱에 표시
st.pyplot(fig)

# 추가적인 데이터 출력
st.write(f"선택된 지역: {selected_region}")
st.write(f"20대 인구 비율: {age_ratio:.2%}")
