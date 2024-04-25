import streamlit as st
import pandas as pd


st.title('Streamlit 연습문제')

st.header('뉴스 데이터 kor_news_20240326.xlsx를 이용하여 스트림릿으로 구현하기')

st.divider()

st.subheader('''  
1. 뉴스데이터를 dataframe으로 표시하기    
3. 분류 컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기  
4. 제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로 
   경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기
''')

df = pd.read_excel('data/kor_news_240326.xlsx')
st.dataframe(df,
             use_container_width=True,
             hide_index=True)

@st.cache_data
def load_data(file_path):
    df = pd.read_excel(file_path)
    return preprocess(df)

news = load_data(file_path)
st.dataframe(news)



st.subheader('2. 뉴스데이터의 url 컬럼을 실제 뉴스기사 페이지로 이동하도록 적절한 column configuration 사용')

# st.data_editor(df,
#              column_config={
#                  'URL' : st.column_config.LinkColumn(
#                      help = 'Search portal site!',
#                      max_chars = 100,
#                      validate='^https://www\.[a-z]+\.[a-z]+',
#                      display_text = for i in df.URL
#                  )
#              })