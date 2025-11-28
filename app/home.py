"""
Home Page Module

Displays the project description and welcome message.
"""

import streamlit as st


def show_home_page():
    """Display the home page with project description."""
    st.title("🎯 Fit Me Up (Career Lens)")
    st.markdown("---")
    
    st.header("Welcome!")
    
    st.markdown("""
    **Fit Me Up (Career Lens)** is an intelligent platform designed to help junior developers 
    and students make informed decisions about their career development path.
    
    ### What We Offer
    
    Our platform provides two key analysis features:
    
    #### 📊 Project Analysis
    - Analyze GitHub projects to understand their complexity and requirements
    - Evaluate the tech stack used in open-source projects
    - Assess your contribution readiness based on your skill level
    - Get personalized recommendations for contributing to projects
    
    #### 📚 Course Analysis
    - Analyze courses to understand their relevance to your career goals
    - Evaluate course content alignment with industry standards
    - Get insights on how courses fit your learning path
    - Make informed decisions about which courses to take
    
    ### How It Works
    
    1. **Navigate** to the analysis page you're interested in using the sidebar
    2. **Input** your project or course information
    3. **Review** the analysis results and recommendations
    4. **Make informed decisions** about your career development
    
    ### Getting Started
    
    Use the navigation menu on the left to explore:
    - **Project Analysis**: Analyze open-source projects and assess your readiness to contribute
    - **Course Analysis**: Evaluate courses and their fit with your career goals
    
    ---
    
    💡 **Tip**: Start by analyzing a GitHub project you're interested in contributing to, 
    or a course you're considering taking!
    """)
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "Made with ❤️ for aspiring developers"
        "</div>",
        unsafe_allow_html=True
    )
