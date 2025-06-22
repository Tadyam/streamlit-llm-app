from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

messages = [
    SystemMessage(
        content="あなたはランニングの専門家です。ユーザーからの質問に対して、専門的なアドバイスを提供してください。"
    ),
    HumanMessage(
        content="ランニングに関する質問を入力してください。"
    )
]

# Streamlitアプリケーションの設定
st.title("ランニング質問アプリ")
st.write("このアプリは、ランニングに関する質問をします。")
st.write("入力フォームに質問を入力し、「実行」ボタンを押すことで、専門家からのアドバイスを受けることができます。")

selected_questions = st.radio(
    "質問を選択してください",
    ("ランニングのフォーム", "ランニングのペース", "ランニングの距離", "ランニングの栄養", "ランニングの怪我予防")
)

st.divider()

# 質問ごとのアドバイスを提供する関数
def handle_question(question_type, advice):
    st.write(f"{question_type}に関する質問を入力してください。")
    question = st.text_input("質問内容")
    if st.button("実行"):
        st.write(f"あなたの質問: {question}")
        st.write(f"専門家からのアドバイス: {advice}")

# 質問タイプごとの処理
question_advice_map = {
    "ランニングのフォーム": "フォームを改善するためには、姿勢を正し、足の着地を意識しましょう。",
    "ランニングのペース": "ペースを維持するためには、心拍数を意識し、一定のリズムで走ることが重要です。",
    "ランニングの距離": "距離を伸ばすためには、徐々に距離を増やし、休息日を設けることが大切です。",
    "ランニングの栄養": "栄養を補うためには、バランスの取れた食事と水分補給が重要です。",
    "ランニングの怪我予防": "怪我を予防するためには、適切なウォームアップとクールダウン、そしてストレッチが重要です。",
}

if selected_questions in question_advice_map:
    handle_question(selected_questions, question_advice_map[selected_questions])