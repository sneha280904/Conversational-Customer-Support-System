from transformers import pipeline

# Load GPT-Neo with text-generation pipeline
chat_pipeline = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')

def handle_query(user_message):
    try:
        # More specific instruction to the model
        prompt = f"""
        You are an assistant that provides clear and factual information about public figures.
        The user will ask about famous personalities, and you should answer with a short, factual description.
        User: {user_message}
        Bot:
        """
        
        print(f"Prompt sent to model:\n{prompt}")  # Debugging

        # Generate the response with a controlled token limit and longer response
        response = chat_pipeline(prompt, max_new_tokens=75, num_return_sequences=1)
        raw_text = response[0]['generated_text']

        print(f"Raw response from model:\n{raw_text}")  # Debugging

        # Extract the bot's reply after "Bot:"
        if "Bot:" in raw_text:
            bot_reply = raw_text.split("Bot:")[1].strip()
        else:
            bot_reply = "I'm sorry, I couldn't process your request at the moment."

        print(f"Extracted bot reply:\n{bot_reply}")  # Debugging

        return bot_reply
    except Exception as e:
        print(f"Error in handle_query: {e}")
        return "I'm sorry, I couldn't process your request at the moment."