"""
Course Analysis Page Module

Provides functionality to analyze courses and assess their fit with career goals.
"""

import streamlit as st


# Scoring constants for course fit calculation
FIT_SCORE_MAX = 95  # Maximum achievable fit score
FIT_SCORE_BASE = 60  # Base fit score
FIT_SCORE_PER_TOPIC = 8  # Points added per detected topic
FIT_SCORE_DESCRIPTION_DIVISOR = 50  # Divisor for description length bonus
FIT_SCORE_DESCRIPTION_MAX = 15  # Maximum bonus from description length


def show_course_analysis_page():
    """Display the course analysis page with input fields and dummy results."""
    st.title("📚 Course Analysis")
    st.markdown("---")
    
    st.markdown("""
    Analyze courses to understand their relevance to your career goals and 
    how they align with industry standards.
    """)
    
    # Input Form
    st.header("Course Information")
    
    with st.form("course_analysis_form"):
        # Course name input
        course_name = st.text_input(
            "Course Name",
            placeholder="e.g., Full Stack Web Development Bootcamp",
            help="Enter the name of the course you want to analyze"
        )
        
        # Course description input
        course_description = st.text_area(
            "Course Description",
            placeholder="Provide a brief description of the course content, topics covered, and learning objectives...",
            help="Enter a description of what the course covers",
            height=150
        )
        
        # Submit button
        submitted = st.form_submit_button("Analyze Course")
    
    # Display results if form is submitted
    if submitted:
        st.markdown("---")
        st.header("Analysis Results")
        
        # Validate inputs
        if not course_name:
            st.error("⚠️ Please enter a course name")
        elif not course_description:
            st.error("⚠️ Please enter a course description")
        else:
            # Display dummy analysis results
            display_dummy_course_analysis(course_name, course_description)


def display_dummy_course_analysis(course_name, course_description):
    """Display dummy analysis results for the course."""
    
    # Course Overview
    st.subheader("🔍 Course Overview")
    st.write(f"**Analyzing:** {course_name}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Career Relevance", "87%", "+12%")
    with col2:
        st.metric("Industry Demand", "High", "↑")
    with col3:
        st.metric("Skill Level", "Intermediate", "")
    
    # Content Analysis
    st.subheader("📖 Content Analysis")
    
    # Detect keywords (dummy analysis based on common terms)
    description_lower = course_description.lower()
    detected_topics = []
    
    topic_keywords = {
        "Web Development": ["web", "html", "css", "javascript", "frontend", "backend"],
        "Data Science": ["data", "machine learning", "python", "analytics", "statistics"],
        "Cloud Computing": ["cloud", "aws", "azure", "devops", "kubernetes", "docker"],
        "Mobile Development": ["mobile", "ios", "android", "react native", "flutter"],
        "Database": ["database", "sql", "mongodb", "postgresql", "mysql"],
        "Security": ["security", "authentication", "encryption", "cybersecurity"],
    }
    
    for topic, keywords in topic_keywords.items():
        if any(keyword in description_lower for keyword in keywords):
            detected_topics.append(topic)
    
    if detected_topics:
        st.write("**Key Topics Covered:**")
        cols = st.columns(min(len(detected_topics), 3))
        for idx, topic in enumerate(detected_topics):
            with cols[idx % 3]:
                st.success(f"✓ {topic}")
    else:
        st.info("No specific technical topics detected. General course content.")
    
    # Career Fit Assessment
    st.subheader("🎯 Career Fit Assessment")
    
    # Calculate fit score based on detected topics and description length
    description_bonus = min(len(course_description) // FIT_SCORE_DESCRIPTION_DIVISOR, FIT_SCORE_DESCRIPTION_MAX)
    fit_score = min(FIT_SCORE_MAX, FIT_SCORE_BASE + len(detected_topics) * FIT_SCORE_PER_TOPIC + description_bonus)
    
    st.progress(fit_score / 100)
    st.write(f"**Overall Fit Score: {fit_score:.0f}/100**")
    
    # Provide recommendations based on fit score
    if fit_score >= 80:
        recommendation = "🌟 **Highly Recommended**: This course aligns excellently with current industry demands and career growth."
        st.success(recommendation)
    elif fit_score >= 60:
        recommendation = "👍 **Good Fit**: This course provides valuable skills that are relevant to your career path."
        st.info(recommendation)
    else:
        recommendation = "💡 **Consider Alternatives**: While useful, you might want to explore other courses more aligned with your goals."
        st.warning(recommendation)
    
    # Skills You'll Gain
    st.subheader("🛠️ Skills You'll Gain")
    
    dummy_skills = []
    if "Web Development" in detected_topics:
        dummy_skills.extend(["HTML/CSS", "JavaScript", "Responsive Design", "Web APIs"])
    if "Data Science" in detected_topics:
        dummy_skills.extend(["Python Programming", "Data Analysis", "Machine Learning", "Visualization"])
    if "Cloud Computing" in detected_topics:
        dummy_skills.extend(["Cloud Architecture", "CI/CD", "Container Orchestration", "Infrastructure as Code"])
    if "Database" in detected_topics:
        dummy_skills.extend(["Database Design", "Query Optimization", "Data Modeling"])
    
    # Add generic skills if none detected
    if not dummy_skills:
        dummy_skills = ["Problem Solving", "Critical Thinking", "Project Management", "Technical Communication"]
    
    cols = st.columns(2)
    for idx, skill in enumerate(dummy_skills[:8]):  # Show max 8 skills
        with cols[idx % 2]:
            st.markdown(f"- ✓ {skill}")
    
    # Career Paths
    st.subheader("🚀 Potential Career Paths")
    with st.expander("See career opportunities after completing this course"):
        career_paths = {
            "Web Development": ["Full Stack Developer", "Frontend Developer", "Backend Developer", "UI/UX Developer"],
            "Data Science": ["Data Scientist", "Machine Learning Engineer", "Data Analyst", "AI Researcher"],
            "Cloud Computing": ["Cloud Architect", "DevOps Engineer", "Site Reliability Engineer", "Cloud Consultant"],
            "Mobile Development": ["Mobile App Developer", "iOS Developer", "Android Developer", "Cross-platform Developer"],
        }
        
        shown_paths = set()
        for topic in detected_topics:
            if topic in career_paths:
                for path in career_paths[topic]:
                    if path not in shown_paths:
                        st.markdown(f"- 🎯 {path}")
                        shown_paths.add(path)
        
        if not shown_paths:
            st.markdown("- 🎯 Software Developer")
            st.markdown("- 🎯 Technical Specialist")
            st.markdown("- 🎯 Technology Consultant")
    
    # Estimated Time Investment
    st.subheader("⏱️ Estimated Learning Path")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("**Estimated Duration**: 8-12 weeks")
    with col2:
        st.info("**Time Commitment**: 10-15 hours/week")
    
    # Next Steps
    st.subheader("📝 Recommended Next Steps")
    st.markdown("""
    1. **Research the course provider**: Check reviews and ratings from past students
    2. **Review the curriculum**: Ensure it covers topics relevant to your goals
    3. **Check prerequisites**: Make sure you have the required background knowledge
    4. **Plan your schedule**: Allocate dedicated time for learning and practice
    5. **Set learning goals**: Define what you want to achieve by completing this course
    """)
    
    st.success("✅ Analysis complete! Use these insights to make an informed decision.")
