
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model_name = "facebook/blenderbot-400M-distill"

# Load model (download on first run and reference local installation for consequent runs)
model_name = "facebook/blenderbot-400M-distill"
#alternative: model_name = "facebook/blenderbot-1B-distill"  
#Cansu's Note: 400M hallicunates a lot so it is better to use another model. 
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

conversation_history = []

while True:
    # Create conversation history string
    history_string = "\n".join(conversation_history)
    # Get the input data from the user
    input_text = input("> ")
    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history_string, input_text, return_tensors="pt")
    # Generate the response from the model
    outputs = model.generate(
    **inputs,
    max_new_tokens=50,
    do_sample=True,
    top_k=50,
    top_p=0.95,
    temperature=0.8,
    repetition_penalty=1.2
)
    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
    
    print(response)
    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)