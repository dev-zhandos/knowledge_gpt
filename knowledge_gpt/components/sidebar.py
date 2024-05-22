import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## Қалай қолдану керек\n"
            "1. Төменде өзіңіздің [OpenAI API кілтіңізді] [OpenAI API key](https://platform.openai.com/account/api-keys) енгізіңіз🔑\n"  # noqa: E501
            "2. PDF, DOCX немесе TXT файлды жүктеңіз📄\n"
            "3. Құжат туралы сұрақ қойыңыз💬\n"
        )
        api_key_input = st.text_input(
            "OpenAI API кілтіңіз",
            type="password",
            placeholder="OpenAI API кілтіңізді мұнда қойыңыз (sk-...)",
            help="API кілтіңізді https://platform.openai.com/account/api-keys сайтынан ала аласыз.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

        st.markdown("---")
        st.markdown("# Бағдарлама туралы")
        st.markdown(
            "📖PedagogGPT сізге құжаттарыңыз туралы сұрақ қоюға "
            "және бірден сілтемелермен нақты жауап алуға мүмкіндік береді. "
        )
        st.markdown("## Найман Биболдың диссертациялық жұмысы")
        st.markdown(
            "Жұмыс заңмен қорғалған. Ескертусіз көшіру заңмен қудаланады. "  # noqa: E501
        )
        st.markdown("---")

        faq()
