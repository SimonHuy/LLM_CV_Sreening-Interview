Step 1: Go to https://aistudio.google.com/app/apikey to generate Gemini API key. 
Due to privacy, I am unable to share my API key.

Step 2: Create a .env file where to store API key
GOOGLE_API_KEY = 'place your API key here'

Step 3: The script requires python version == 3.10.0
Create virtual environment and install the required libraries inside requirements.txt

Step 4: To run the script. Type the following line in termninal
& "C:\YourPythonPath\python.exe" -m streamlit run cv_screening.py --server.enableXsrfProtection=false

Notice:
+ Use files in JD and CV folders to input to the app
+ Watch demo video first

Background: 
Interview processes are slow and expensive. Companies spend over $5,000 per hire, most of 
which is time spent by internal recruiting teams and hiring managers interviewing candidates. 
The average length of an interview process is approximately 30 days.  

Objective: 
Build an AI Interview Agent for Candidate Interviewing 
Develop an AI Interview Agent capable of automatically conducting interviews with candidates in 
English, focusing on screening and basic technical questions. The Agent should customize 
questions based on the job requirements and candidate experience, conduct an interview and 
generate an evaluation report. 

Input: 
● Job Description: A text document outlining the company information, responsibilities, 
required skills, and desired experience. 
● Candidate Profile: A text document about the candidate, including experience, skills, 
location, education, etc. 

Description: 
● The Agent should be able to generate questions dynamically based on the job 
description and candidate profile. This includes technical questions, behavioral 
questions, and questions related to the candidate’s past experience. Also ask follow up 
questions based on the candidate’s answer. 
● The Agent should evaluate candidate responses for relevance, correctness, and 
completeness. And send a response back to the candidate. 
● The Agent must include guardrails to ensure it stays within the interviewing context and 
does not answer unrelated questions from candidates. 
● The interview can be conducted in a text-based (chat type) format.