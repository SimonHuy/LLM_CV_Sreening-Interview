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