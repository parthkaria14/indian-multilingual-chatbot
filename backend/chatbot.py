from .utils import translate_text, get_chatbot_response

def chatbot_response(user_input: str, language_code: str) -> str:
    """
    Process user input and return a chatbot response in the specified language.
    """
    try:
        # Log original input
        print(f"Original input: {user_input} (Language: {language_code})")

        # Translate input to English
        if language_code != "en":
            user_input = translate_text(user_input, language_code, "en")
            print(f"Translated input to English: {user_input}")

        # Generate chatbot response in English
        english_response = get_chatbot_response(user_input)
        print(f"Chatbot response in English: {english_response}")

        # Translate response back to the user's language
        if language_code != "en":
            final_response = translate_text(english_response, "en", language_code)
            print(f"Translated response to {language_code}: {final_response}")
            return final_response

        return english_response
    except Exception as e:
        print(f"Error processing chatbot response: {e}")
        return "I'm sorry, I couldn't process your request."
