Visual Test Baseline Manager



\----------------------------------



Student Name: Manalee Tamrakar  

Course: CSE3253 DevOps \[PE6]  

Semester: VI (2025–2026)  

Project Type: Testing  

Difficulty: Intermediate  



\----------------------------------



Project Overview



Problem Statement  

Modern UI testing lacks efficient visual regression tracking. This project provides a system to manage baseline images and detect UI changes using automated comparison.



Objectives  

\- Manage baseline screenshots  

\- Detect UI changes automatically  

\- Enable baseline updates  

\- Integrate with DevOps workflows  



Key Features  

\- Image comparison using Python  

\- Difference detection  

\- Baseline update API  

\- REST API-based testing system  



\----------------------------------



Technology Stack



Core Technologies  

\- Programming Language: Python  

\- Framework: Flask  

\- Image Processing: PIL (Pillow)  



DevOps Tools  

\- Version Control: Git  

\- CI/CD: To be added  

\- Containerization: Docker (In progress)  



\----------------------------------



Getting Started



Prerequisites  

\- Python 3.8+  

\- Git  



Installation  



git clone https://github.com/YOUR-USERNAME/devopsprojectvisualtestbaselinemanager.git  

cd devopsprojectvisualtestbaselinemanager  

pip install flask pillow  

python src/main/app.py  



\----------------------------------



API Endpoints



Compare Images  

POST /compare  



Update Baseline  

POST /update-baseline  



\----------------------------------



Testing



Use curl command:



curl -X POST http://127.0.0.1:5000/compare -F "baseline=@img1.jpg" -F "new=@img2.jpg"  



\----------------------------------



Learnings



\- Implemented visual regression testing  

\- Learned DevOps workflow basics  

\- Built REST API using Flask  



\----------------------------------



Challenges



\- Handling image comparison accuracy  

\- Managing file paths in Windows  

\- Setting up Docker environment  



\----------------------------------



Future Improvements



\- Add frontend interface  

\- Integrate CI/CD pipeline  

\- Improve comparison algorithm  



\----------------------------------



Contact



GitHub: https://github.com/manaleetamrakar

