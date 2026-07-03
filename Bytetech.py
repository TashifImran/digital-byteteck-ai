import streamlit as st
import google.generativeai as genai

api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)

system_prompt = """
You are the dedicated AI Expert for Digital Byteteck, developed by Tashif Imran. 
Be warm, professional, and conversational—never robotic. 
You represent Digital Byteteck, an agency specializing in Digital Marketing (including SEO & Copywriting), Web Development, and tailored software solutions. 
    
When helping clients, always be ready to provide strategic advice on:
- Digital Growth: SEO, Copywriting, and Marketing strategies.
- Technical Solutions: Custom Software, Web & Mobile App Development.
- Infrastructure: IT & Cloud Solutions and Digital Transformation.
    
Always keep your tone helpful, concise, and focused on delivering real results for the client."""


model = genai.GenerativeModel(
    model_name="models/gemini-3.5-flash",
    system_instruction=system_prompt
)

st.title("ByteTeck Expert Assistant")

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

for message in st.session_state.chat_session.history:
    with st.chat_message(message.role):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("How can I help you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.session_state.chat_session.send_message(prompt)
        st.markdown(response.text)
