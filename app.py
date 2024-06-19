import streamlit as st
import openai

# Securely set your OpenAI API key (do not hardcode it in the script)
openai.api_key = st.secrets["openai"]["api_key"]


# Function to translate Pangyo dialect to standard Korean using GPT-4 chat model
def translate_jargon(jargon):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that translates Pangyo dialect to standard Korean."},
        {"role": "user", "content": f"번역: {jargon}\n표준어:"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=1000,
        temperature=0.7,
    )
    translation = response.choices[0].message['content'].strip()
    return translation

# Streamlit app setup
st.set_page_config(page_title="판교어 번역기", page_icon=":speech_balloon:", layout="wide")

# Header and Subheader
st.title("판교어 번역기")
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextArea textarea {
        background-color: #f8f9fa;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.header("환영합니다!")
st.subheader("이 앱은 판교어를 표준 한국어로 번역해줍니다.")

# User input
jargon = st.text_area("판교어를 입력하세요:", height=200)

# Add some space before the button
st.markdown("<br>", unsafe_allow_html=True)

# Translate button
if st.button("번역하기"):
    if jargon.strip():
        translated_text = translate_jargon(jargon)
        st.markdown(f"### 번역 결과:\n\n{translated_text}")
    else:
        st.warning("입력란에 텍스트를 입력해주세요.")

# Footer
st.markdown(
    """
    <style>
    footer {
        visibility: hidden;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4CAF50;
        color: white;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>© 2024 github.com/KeonhoChu. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)