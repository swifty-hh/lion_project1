import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from st_pages import add_page_title, hide_pages
plt.rcParams['font.family'] ='Malgun Gothic'

# 사이드바에 위젯 추가
with st.sidebar:
  selected = option_menu(
    menu_title = "Main Menu",
    options = ["Projects","Analysis of AI","Contact"],
    icons = ["book","robot", "envelope"],
    menu_icon = "app-indicator",
    default_index = 0,
  )

# 선택된 옵션에 따른 화면 출력
if selected == "Analysis of AI":
    # 제목
    st.title('범죄 발생 빈도에 대한 데이터 분석')
    st.write('')
    st.write('')
    # 데이터 소개
    st.header(':male-teacher: 데이터 소개')
    st.write('''
    이 데이터는 다양한 장소에서 발생한 범죄 유형과 그 빈도를 나타내는 통계입니다. 각 열은 특정 장소(예: 아파트, 단독주택, 고속도로 등)를 나타내며, 각 행은 범죄 유형(예: 강도, 방화, 절도범죄 등)을 나타냅니다. 데이터를 통해 우리는 범죄 발생률이 장소에 따라 어떻게 달라지는지, 그리고 어떤 유형의 범죄가 특정 장소에서 더 자주 발생하는지 파악할 수 있습니다.
    ''')

    # 주요 발견
    st.header(':mag: 주요 발견')
    st.write('''
    - 절도범죄가 모든 장소에서 가장 높은 발생 빈도를 보이며, 특히 노상, 슈퍼마켓, 아파트, 단독주택에서 높은 수치를 나타냅니다.
    - 폭행은 노상, 아파트, 단독주택에서 높은 발생률을 보이며, 인간 간의 충돌이 자주 발생할 수 있음을 의미합니다.
    - 교통범죄는 고속도로와 노상에서 압도적으로 높은 수치를 보여, 교통 관련 법규 위반 또는 사고가 자주 발생함을 나타냅니다.
    - 마약범죄와 성풍속범죄는 아파트와 단독주택에서 상대적으로 높은 발생률을 보이며, 개인의 사생활과 관련이 깊습니다.
    - 횡령과 사기는 아파트, 단독주택, 그리고 노상에서 높은 빈도를 보여, 다양한 환경에서 폭넓게 일어날 수 있음을 시사합니다.
    ''')

    # 분석의 의의
    st.header(':star: 분석의 의의')
    st.write('''
    이 데이터 분석을 통해 우리는 범죄 예방과 대응 전략을 개발할 때 장소와 범죄 유형을 고려해야 함을 알 수 있습니다. 예를 들어, 절도범죄의 높은 발생률을 감안할 때, 공공 장소와 주거지역에서의 보안 강화가 중요합니다. 또한, 특정 장소에서 빈번하게 발생하는 범죄 유형을 파악하여 그에 맞는 예방책을 마련하는 것도 중요합니다.
    ''')

    # 앱 제목 설정
    st.header(':male-police-officer: 구현 전략 제안')

    # 전략 내용 작성
    st.write('''
    이러한 분석 결과를 바탕으로, 다음과 같은 구체적인 대응 전략을 제시합니다.

    1. 보안 카메라와 경보 시스템 설치: 절도범죄가 높은 장소에 보안 카메라와 경보 시스템을 설치하여 범죄 예방에 기여할 수 있습니다. 특히, 상업 지역과 주거 지역에서 이러한 시스템의 설치는 범죄를 사전에 방지하고, 발생 시 신속한 대응을 가능하게 합니다.
    2. 교통법규 교육 및 단속 강화: 교통범죄가 높은 고속도로와 노상에서는 교통법규에 대한 교육을 강화하고, 법규 위반에 대한 단속을 철저히 함으로써 사고 및 범죄 발생률을 낮출 수 있습니다.
    3. 마약 및 성풍속범죄에 대한 교육 및 상담 프로그램 제공: 아파트와 단독주택에서 높은 발생률을 보이는 마약범죄와 성풍속범죄를 예방하기 위해, 관련 교육 및 상담 프로그램을 제공하여 주민들의 인식을 개선하고, 문제를 조기에 발견하여 대응할 수 있도록 합니다.
    4. 횡령 및 사기 범죄에 대한 금융 교육: 아파트, 단독주택, 그리고 노상에서 발생하는 횡령 및 사기 범죄를 줄이기 위해, 금융 교육을 통해 사람들이 이러한 범죄의 표적이 되지 않도록 하는 방안을 모색합니다. 이를 통해 개인이 자신의 재산을 보호하는 방법을 배우고, 사기를 예방할 수 있습니다.

    위 제안된 전략들은 범죄 예방 및 대응에 있어서 중요한 역할을 할 수 있으며, 지속적인 모니터링과 평가를 통해 전략의 효과를 검증하고 필요에 따라 조정해야 합니다.
    ''')
    st.write('사용된 AI: 뤼튼 (https://wrtn.ai/)')
elif selected == "Projects":
    # 데이터 정의
    df = pd.read_excel('data.xlsx')

    # 스트림릿 타이틀
    st.title("범죄 유형별 발생 장소")

    # 데이터프레임을 스트림릿에 표시
    st.dataframe(df)

    # 차트를 그리기 위한 데이터 선택
    selected_crime = st.selectbox("차트에 표시할 범죄 유형을 선택하세요.", df["범죄 분류"].unique())

    # 선택된 범죄 유형에 해당하는 데이터 필터링
    filtered_df = df[df["범죄 분류"] == selected_crime].melt(id_vars=["범죄 분류"], var_name="장소", value_name="건수")

    # 맷플롯립을 사용하여 차트 생성
    plt.figure(figsize=(10, 8))
    plt.bar(filtered_df["장소"], filtered_df["건수"])
    plt.xlabel("장소")
    plt.ylabel("건수")
    plt.title(f"{selected_crime} 발생 장소별 건수")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # 스트림릿에 차트 표시
    st.pyplot(plt)

    st.write('출처: https://www.data.go.kr/data/3074463/fileData.do')
elif selected == "Contact":
    st.write("# THANK YOU!!!")
    st.markdown("---")
    hide_pages(["Thank you!"])

    st.markdown("#### 📬 Get In Touch With Me!")

    contact_form = """
    <form action="https://formsubmit.co/hhj5621na@gmail.com" method="POST" enctype="multipart/form-data">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="text" name="_subject" placeholder="Subject">
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <input type="file" class="img_btn" name="Upload Image" accept="image/png, image/jpeg">
        <br>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)



    hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")

    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    st.markdown("---")
    st.success("""
    홍한준
    - 깃헙: https://github.com/swifty-hh
    """)