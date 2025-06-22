from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# OpenAI APIの設定
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

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
def handle_question(question_type):
    st.write(f"{question_type}に関する質問を入力してください。")
    question = st.text_input("質問内容")
    if st.button("実行"):
        st.write(f"あなたの質問: {question}")
        
        # OpenAI APIを使用してアドバイスを生成
        messages = [
            SystemMessage(content=f"あなたはランニングの専門家です。以下の質問に対して専門的なアドバイスを提供してください。"),
            HumanMessage(content=f"質問タイプ: {question_type}\n質問内容: {question}")
        ]
        try:
            response = llm(messages)
            st.write(f"専門家からのアドバイス: {response.content}")
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")

# 質問タイプごとの処理
if selected_questions:
    handle_question(selected_questions)