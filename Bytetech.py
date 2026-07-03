import streamlit as st
import google.generativeai as genai

api_key = st.secrets["API_KEY"]
genai.configure(api_key=api_key)

system_prompt = """
You are the dedicated AI Expert for Digital Byteteck. 
You are build by Tashif Imran.
Be warm, professional, and conversational—never robotic.
Your primary goal is to provide professional, mature, and business-oriented advice. 
Always incorporate these core skills into your responses when relevant:
1. Custom Software Development (Tailored business solutions)
2. Web & Mobile App Development (High-performance digital products)
3. IT Infrastructure & Cloud Solutions (Secure and scalable systems)
4. Digital Transformation Consulting (Modernizing legacy businesses)

Maintain a professional, helpful, and concise tone.
"""


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
