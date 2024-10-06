from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MODEL_NAME = "meta-llama/Llama-3.2-3B-Instruct"

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    return model, tokenizer

def generate_response(model, tokenizer, input_text, max_length=100):
    inputs = tokenizer(input_text, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=max_length)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response