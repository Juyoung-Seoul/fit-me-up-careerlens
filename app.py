"""
Fit Me Up (Career Lens) - Main Application Entry Point

A Streamlit web app to analyze GitHub projects and courses for career fit.
"""

import streamlit as st
from app.home import show_home_page
from app.project_analysis import show_project_analysis_page
from app.course_analysis import show_course_analysis_page


def main():
    """Main application entry point."""
    st.set_page_config(
        page_title="Fit Me Up (Career Lens)",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Home", "Project Analysis", "Course Analysis"]
    )
    
    # Display selected page
    if page == "Home":
        show_home_page()
    elif page == "Project Analysis":
        show_project_analysis_page()
    elif page == "Course Analysis":
        show_course_analysis_page()


if __name__ == "__main__":
    main()
