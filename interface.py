from model_loader import load_model_pipeline
from chat_memory import ChatMemory
from transformers import AutoTokenizer

def main():
    print("Starting Local CLI Chatbot. Type /exit to quit.\n")

    model_name = "facebook/blenderbot-400M-distill"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    chatbot = load_model_pipeline()
    memory = ChatMemory(max_turns=5)

    def get_truncated_prompt(memory, max_input_tokens=128):
        # Join full history
        full_prompt = memory.get_context() + "\nBot:"
        # Tokenize with truncation
        encoded = tokenizer(full_prompt, max_length=max_input_tokens, truncation=True, return_tensors="pt")
        # Decode tokens back to text prompt safely
        truncated_prompt = tokenizer.decode(encoded.input_ids[0], skip_special_tokens=True)
        return truncated_prompt

    while True:
        user_input = input("User: ").strip()
        if user_input.lower() == "/exit":
            print("Exiting chatbot. Goodbye!")
            break

        memory.add_user_message(user_input)
        prompt = get_truncated_prompt(memory, max_input_tokens=128)

        response = chatbot(prompt, max_length=100, do_sample=True, top_p=0.9, top_k=50)[0]['generated_text']
        memory.add_bot_message(response)

        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
