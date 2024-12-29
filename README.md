OVERVIEW
The Indian Multilingual Chatbot is a conversational AI application designed to interact with users in multiple languages, including English, Hindi, Marathi, and Gujarati. It utilizes advanced translation models and a state-of-the-art language model to provide accurate and context-aware responses.

FEATURES
Multilingual Support: Communicate in various languages.
Translation Capabilities: Automatically translates user input to English and responses back to the user's language.
Conversational AI: Powered by the LLaMA model for generating human-like responses.
Web Interface: User-friendly interface built with Streamlit for easy interaction.

PROJECT STRUCTURE
multilingual-chatbot/
│
├── backend/
│ ├── __init__.py
│ ├── app.py # FastAPI application
│ ├── chatbot.py # Chatbot logic and response handling
│ ├── models.py # Model initialization and pipelines
│ ├── utils.py # Utility functions for translation and response generation
│ └── requirements.txt # Backend dependencies
│
├── frontend/
  ├── app.py # Streamlit frontend application
  └── requirements.txt # Frontend dependencies



INSTALLATION

Backend:
1.Navigate to the backend directory.
2.Install the required packages: pip install -r requirements.txt

Frontend:
1.Navigate to the frontend directory.
2.Install the required packages : pip install -r requirements.txt

RUNNING THE APP
1.Start the Backend
2.Navigate to the backend directory.
3.Run the FastAPI application: uvicorn app:app --reload

1.Start the Frontend
2.Navigate to the frontend directory.
3.Run the Streamlit application: streamlit run app.py


USAGE
Open your web browser and go to http://localhost:8501 to access the chatbot interface.
Select your preferred language and start chatting with the bot.

CONTRIBUTING
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.


ACKNOWLEDGEMENTS

Hugging Face Transformers for providing the models and pipelines.
FastAPI for the backend framework.
Streamlit for the frontend framework.


