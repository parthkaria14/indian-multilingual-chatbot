import torch
from transformers import pipeline, MarianMTModel, MarianTokenizer, AutoModelForCausalLM, AutoTokenizer

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
device_id = 0 if device == "cuda" else -1

# Initialize translation models
TRANSLATORS = {
    "en-hi": "Helsinki-NLP/opus-mt-en-hi",
    "hi-en": "Helsinki-NLP/opus-mt-hi-en",
    "en-mr": "Helsinki-NLP/opus-mt-en-mr",
    "mr-en": "Helsinki-NLP/opus-mt-mr-en",
    "en-gu": "Helsinki-NLP/opus-mt-en-guw",
    "gu-en": "Helsinki-NLP/opus-mt-guw-en",
}

translation_pipelines = {}
for key, model in TRANSLATORS.items():
    try:
        translation_pipelines[key] = pipeline(
            "translation",
            model=MarianMTModel.from_pretrained(model).to(device),
            tokenizer=MarianTokenizer.from_pretrained(model),
            device=device_id,
        )
    except Exception as e:
        print(f"Error loading model {model}: {e}")

# Initialize LLaMA model for conversational tasks with system prompts
try:
    chat_model_name = "meta-llama/Llama-3.2-1B"  # Adjusted model for 6GB VRAM
    chat_model = pipeline(
        "text-generation",
        model=AutoModelForCausalLM.from_pretrained(chat_model_name, torch_dtype=torch.float16).to(device),
        tokenizer=AutoTokenizer.from_pretrained(chat_model_name),
        device=device_id,
    )
    system_prompt = (
        "You are a helpful, knowledgeable, and friendly AI assistant capable of understanding and responding to "
        "questions in a wide variety of languages. Always provide accurate and concise answers."
        "your name is llama ai."
    )
except Exception as e:
    print(f"Error loading chatbot model: {e}")
    chat_model = None
    system_prompt = ""
