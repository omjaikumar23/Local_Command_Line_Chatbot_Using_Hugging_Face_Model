from transformers import pipeline

def load_model_pipeline():
    """
    Load Hugging Face BlenderBot model using text2text-generation pipeline.
    """
    model_name = "facebook/blenderbot-400M-distill"
    chat_pipeline = pipeline("text2text-generation", model=model_name)
    return chat_pipeline
