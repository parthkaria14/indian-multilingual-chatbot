from .models import translation_pipelines, chat_model, system_prompt

def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    """
    Translate text between source and target languages.
    """
    key = f"{source_lang}-{target_lang}"
    if key in translation_pipelines:
        try:
            translated = translation_pipelines[key](text)[0]["translation_text"]
            print(f"Translated '{text}' from {source_lang} to {target_lang}: {translated}")
            return translated
        except Exception as e:
            print(f"Error during translation: {e}")
            return text
    print(f"No translation pipeline for {source_lang}-{target_lang}. Returning original text.")
    return text

def get_chatbot_response(user_input: str) -> str:
    """
    Generate a chatbot response in English using LLaMA with a system prompt.
    """
    try:
        # Combine system prompt with user input
        prompt = f"{system_prompt}\nUser: {user_input}\nAssistant:"
        
        # Generate response
        response = chat_model(
            prompt,
            max_length=200,
            num_return_sequences=1,
            pad_token_id=chat_model.tokenizer.eos_token_id,
            truncation=True,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            top_k=50,
        )[0]["generated_text"]
        
        # Extract the assistant's response
        bot_response = response.split("Assistant:")[-1].strip()
        return bot_response
    except Exception as e:
        print(f"Error generating chatbot response: {e}")
        return "Sorry, I couldn't generate a response."
