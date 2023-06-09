import streamlit as st
import webbrowser

# Custom CSS
pink_style = """
<style>
body {
    background-color: white;
}

.sidebar .sidebar-content {
    background-color: #FF69B4 !important;
    color: white;
}

.sidebar .sidebar-content .sidebar-collapse-control {
    color: white;
    font-weight: bold;
    font-size: 24px;
}

.sidebar .sidebar-content a {
    color: white;
    font-weight: bold;
    font-size: 18px;
}

.sidebar .sidebar-content a:hover {
    color: #FF69B4;
    background-color: white;
}
</style>
"""

# Login Page
def login():
    st.title("ศูนย์การแพทย์กาญจนาภิเษก")
    st.header("งานสารบรรณ")
    st.markdown(pink_style, unsafe_allow_html=True)

    password = st.text_input("Password", type="password")
    if password == "Nongwin":
        st.success("Login successful!")
        return True
    else:
        st.error("Incorrect password.")
        return False

# Transcribe Page
def home():
    st.title("Home")
    st.write("This is the Home page.")

def transcribe():
    st.title("Transcribe")
    st.write("This is the Transcribe page.")

# Convert Page
def convert():
    st.title("Convert")
    st.write("This is the Convert page.")

# Denoise Page
def keep():
    st.title("Keep")
    st.write("This is the Keep page.")

# Tempo Page
def tempo():
    st.title("Tempo")
    st.write("This is the Tempo page.")

# Main App
def main():
    if not login():
        return

    # Sidebar menu
    st.sidebar.title("โปรดเลือกเมนู")
    menu_item = st.sidebar.selectbox("", ["Home","Transcribe", "Convert", "Denoise", "Tempo"])

    if menu_item == "Home":
        home()
    elif menu_item == "Transcribe":
        webbrowser.open_new_tab("https://drkamthorn-whisperai.streamlit.app/")
    elif menu_item == "Convert":
        webbrowser.open_new_tab("https://drkamthorn-docconvert-app-kjr9mv.streamlit.app/") 
    elif menu_item == "Keep":
        webbrowser.open_new_tab("https://drkamthorn-arch2-kep-m36e8h.streamlit.app/")
    elif menu_item == "Tempo":
        tempo()

# Run the app
if __name__ == "__main__":
    main()