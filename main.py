import streamlit as st
import google.generativeai as gemini

gemini.configure(api_key="AIzaSyBeJtlvS9r5apzbdQGqsuM2JZJZjVdcTqI")

st.write("you need to press r or reload the page, after the questions, to get the response from the bot")

# Initialize session state for storing chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat history (messages from both the user and assistant)
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Get user input through the chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add the user message to the messages list
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Generate a response from the assistant (you can customize this logic)
    bot_response = f"Bot: {gemini.GenerativeModel('gemini-1.5-pro').generate_content(user_input).text}"  # Reversing the user input as an example
    
    # Add the assistant response to the messages list
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    # Force Streamlit to update the UI (refresh)

