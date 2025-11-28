"""
Project Analysis Page Module

Provides functionality to analyze GitHub projects and assess contribution readiness.
"""

import streamlit as st


def show_project_analysis_page():
    """Display the project analysis page with input fields and dummy results."""
    st.title("📊 Project Analysis")
    st.markdown("---")
    
    st.markdown("""
    Analyze GitHub projects to understand their complexity, tech stack, and assess 
    your readiness to contribute based on your skill level.
    """)
    
    # Input Form
    st.header("Project Information")
    
    with st.form("project_analysis_form"):
        # GitHub URL input
        github_url = st.text_input(
            "GitHub Repository URL",
            placeholder="https://github.com/username/repository",
            help="Enter the full URL of the GitHub repository you want to analyze"
        )
        
        # Tech stack input
        tech_stack = st.text_input(
            "Tech Stack",
            placeholder="Python, JavaScript, React, Node.js, etc.",
            help="Enter the technologies used in the project (comma-separated)"
        )
        
        # Contribution level slider
        contribution_level = st.slider(
            "Your Contribution Level (0-100)",
            min_value=0,
            max_value=100,
            value=50,
            help="Rate your experience level: 0 = Beginner, 50 = Intermediate, 100 = Expert"
        )
        
        # Submit button
        submitted = st.form_submit_button("Analyze Project")
    
    # Display results if form is submitted
    if submitted:
        st.markdown("---")
        st.header("Analysis Results")
        
        # Validate inputs
        if not github_url:
            st.error("⚠️ Please enter a GitHub repository URL")
        elif not tech_stack:
            st.error("⚠️ Please enter the tech stack")
        else:
            # Display dummy analysis results
            display_dummy_analysis(github_url, tech_stack, contribution_level)


def display_dummy_analysis(github_url, tech_stack, contribution_level):
    """Display dummy analysis results for the project."""
    
    # Project Overview
    st.subheader("🔍 Project Overview")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Project Complexity", "Medium", "+15%")
    with col2:
        st.metric("Active Contributors", "42", "+8")
    with col3:
        st.metric("Open Issues", "23", "-5")
    
    # Tech Stack Analysis
    st.subheader("💻 Tech Stack Analysis")
    tech_list = [tech.strip() for tech in tech_stack.split(",") if tech.strip()]
    
    st.write("**Technologies Detected:**")
    cols = st.columns(min(len(tech_list), 4))
    for idx, tech in enumerate(tech_list[:8]):  # Show max 8 technologies
        with cols[idx % 4]:
            st.info(f"✓ {tech}")
    
    # Contribution Readiness
    st.subheader("🎯 Contribution Readiness Assessment")
    
    # Calculate readiness score (dummy calculation)
    readiness_score = min(100, (contribution_level * 0.7 + 30))
    
    st.progress(readiness_score / 100)
    st.write(f"**Your Readiness Score: {readiness_score:.0f}/100**")
    
    # Provide recommendations based on contribution level
    if contribution_level < 30:
        recommendation = "🌱 **Beginner Level**: Start with 'good first issue' tags. Focus on documentation and simple bug fixes."
        color = "blue"
    elif contribution_level < 70:
        recommendation = "🚀 **Intermediate Level**: You can tackle medium complexity issues. Look for feature enhancements and testing."
        color = "green"
    else:
        recommendation = "⭐ **Advanced Level**: You're ready for complex features, architecture improvements, and mentoring others."
        color = "orange"
    
    st.info(recommendation)
    
    # Suggested First Steps
    st.subheader("📝 Suggested First Steps")
    st.markdown(f"""
    1. **Clone the repository**: `git clone {github_url}`
    2. **Read the documentation**: Check README.md and CONTRIBUTING.md
    3. **Set up the development environment**: Install dependencies and run tests
    4. **Find suitable issues**: Look for issues matching your skill level
    5. **Join the community**: Introduce yourself and ask questions
    """)
    
    # Learning Resources
    st.subheader("📚 Learning Resources")
    with st.expander("Recommended resources to improve your skills"):
        st.markdown("""
        - **Git & GitHub**: Learn version control and collaboration workflows
        - **Code Review Best Practices**: Understand how to give and receive feedback
        - **Project-specific documentation**: Deep dive into the project's architecture
        - **Community guidelines**: Familiarize yourself with the project's contribution guidelines
        """)
    
    st.success("✅ Analysis complete! Use these insights to plan your contribution.")
