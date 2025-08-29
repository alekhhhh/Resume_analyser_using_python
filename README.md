📄 Resume Analyzer (Python)

A lightweight Resume Analyzer built in Python that scans resumes in PDF or TXT format and checks for key programming skills. This tool is useful for students, recruiters, and developers who want a quick way to identify relevant skills in a resume.

✨ Features

Supports PDF and TXT resumes

Detects skills like: Python, Java, HTML, CSS, C, C++, SQL

Displays which skills are FOUND or NOT FOUND

Shows the total number of matched skills

🛠️ Tech Stack

Python 3

PyPDF2 (for PDF text extraction)

🚀 How to Run

Clone the repository

git clone https://github.com/your-username/Resume_analyser_using_python.git
cd Resume_analyser_using_python

Install dependencies

pip install PyPDF2

Run the script
python resume_analyzer.py
When prompted, enter the filename (e.g., resume.pdf or resume.txt).

Example Output
✌️ PYTHON FOUND!!
😒 JAVA NOT FOUND!!
✌️ HTML FOUND!!
😒 CSS NOT FOUND!!
✌️ C FOUND!!
✌️ C++ FOUND!!
😒 SQL NOT FOUND!!

TOTAL SKILLS MATCHED: 4 out of 7

🔮 Future Scope
Add support for DOCX resumes
Expand the skill list
Export results to CSV/JSON

 License
This project is licensed under the MIT License.
