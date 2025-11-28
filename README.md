# Fit Me Up (Career Lens) 🎯

Open Source project & course to career fit analyzer for junior developers and students.

## Overview

**Fit Me Up (Career Lens)** is a Streamlit-based web application that helps junior developers and students make informed decisions about their career development path. The platform provides intelligent analysis for both GitHub projects and courses.

## Features

### 📊 Project Analysis
- Analyze GitHub projects to understand their complexity and requirements
- Evaluate the tech stack used in open-source projects
- Assess your contribution readiness based on your skill level
- Get personalized recommendations for contributing to projects

### 📚 Course Analysis
- Analyze courses to understand their relevance to your career goals
- Evaluate course content alignment with industry standards
- Get insights on how courses fit your learning path
- Make informed decisions about which courses to take

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Juyoung-Seoul/fit-me-up-careerlens.git
cd fit-me-up-careerlens
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Project Structure

```
fit-me-up-careerlens/
├── app/
│   ├── __init__.py           # Package initialization
│   ├── home.py               # Home page module
│   ├── project_analysis.py   # Project analysis page module
│   └── course_analysis.py    # Course analysis page module
├── app.py                     # Main application entry point
├── requirements.txt           # Python dependencies
└── README.md                 # Project documentation
```

## How to Use

1. **Home Page**: Start here to learn about the platform and its features
2. **Project Analysis**: Enter a GitHub repository URL, tech stack, and your contribution level to get analysis results
3. **Course Analysis**: Enter a course name and description to evaluate its career fit

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
