Visual Test Baseline Manager

--------------------------------------------------

Visual Test Baseline Manager is a system designed to detect visual changes in UI by comparing screenshots. It helps identify visual regressions in automated testing workflows.

--------------------------------------------------

Project Overview

The system compares baseline images with new test images using image processing techniques. It detects differences and highlights them, enabling efficient UI testing.

--------------------------------------------------

Technologies Used

• Python  
• Flask  
• Pillow (PIL)  
• Docker  
• Git  

--------------------------------------------------

Objectives

• Manage baseline screenshots  
• Detect UI changes automatically  
• Enable baseline updates  
• Support DevOps-based workflows  

--------------------------------------------------

Key Features

• Image comparison using pixel difference  
• Automatic detection of visual changes  
• Baseline update functionality  
• REST API-based system  

--------------------------------------------------

Getting Started

Prerequisites

• Python 3.8+  
• Git  
• Docker (optional)  

Installation

git clone https://github.com/YOUR-USERNAME/devopsprojectvisualtestbaselinemanager.git  
cd devopsprojectvisualtestbaselinemanager  
pip install flask pillow  
python src/main/app.py  

--------------------------------------------------

Docker Setup

Run using Docker:

docker compose up --build  

Access application at:  
http://localhost:8080  

--------------------------------------------------

API Endpoints

POST /compare  
Compare baseline and new image  

POST /update-baseline  
Update baseline image  

--------------------------------------------------

Testing

Example curl command:

curl -X POST http://127.0.0.1:5000/compare -F "baseline=@img1.jpg" -F "new=@img2.jpg"  

--------------------------------------------------

Project Structure

src/ → Application code  
docs/ → Documentation  
infrastructure/ → Docker setup  
pipelines/ → CI/CD (optional)  
tests/ → Test cases  
monitoring/ → Monitoring configs  

--------------------------------------------------

Documentation

Project Plan → docs/projectplan.md  
Design Document → docs/designdocument.md  
User Guide → docs/userguide.md  
API Documentation → docs/apidocumentation.md  

--------------------------------------------------

Challenges

• Docker configuration issues  
• Port mapping and container access  
• File handling in Windows  

--------------------------------------------------

Learnings

• Implemented visual regression testing  
• Learned containerization using Docker  
• Understood DevOps workflow  

--------------------------------------------------

Future Improvements

• Add frontend UI  
• Integrate CI/CD pipeline  
• Improve image comparison accuracy  

--------------------------------------------------

Contact

GitHub: https://github.com/manaleetamrakar
