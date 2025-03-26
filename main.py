# main.py
import streamlit as st

def return_home_button():
    """Creates a Home button in the top right corner."""
    col1, col2, col3 = st.columns([4, 1, 1])
    with col3:
        if st.button("Home", key="home_button_unique"):
            st.session_state.page = "home"
            st.rerun()

def home_page():
    """Displays the home page with three application buttons."""
    st.title("Wave Application Launcher")
    st.write("Welcome to the Wave Application Launcher! Select an application below:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Tracker"):
            st.session_state.page = "app1"
            st.rerun()
    
    with col2:
        if st.button("NCR Reporter"):
            st.session_state.page = "app2"
            st.rerun()
    
    with col3:
        if st.button("Slab Cycle Analyzer"):
            st.session_state.page = "app3"
            st.rerun()

def main():
    """Main function to handle page navigation."""
    if 'page' not in st.session_state:
        st.session_state.page = "home"

    with st.container():
        if st.session_state.page == "home":
            home_page()
        elif st.session_state.page == "app1":
            import appp
            return_home_button()
            appp.main()
        elif st.session_state.page == "app2":
            import ncr
            return_home_button()
            ncr.main()
        elif st.session_state.page == "app3":
            import CheckReport
            return_home_button()
            CheckReport.main()

if __name__ == "__main__":
    main()