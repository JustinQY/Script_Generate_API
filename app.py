from transformers import (AutoTokenizer, AutoModelForCausalLM)
from peft import PeftModel
from fastapi import FastAPI
from pydantic import BaseModel
from huggingface_hub import login

hf_token = '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'

login(token=hf_token)
print("Hugging Face Successfully Login!")

app = FastAPI()

# Load fine-tuned model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf", use_auth_token=True)
base_model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf", use_auth_token=True)
model = PeftModel.from_pretrained(base_model, "./checkpoint-5400", local_files_only=True)


# Define data structure of parameters
class PromptInput(BaseModel):
    prompt: str

# define API interface
@app.post("/generate")
def generate_script(input: PromptInput):
    print("Starts Generating!")
    inputs = tokenizer(input.prompt, return_tensors="pt")
    print("Inputs Tokenized! Generating Begins~")
    outputs = model.generate(**inputs)
    print("Generating Succeed!")
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Results formed!")
    return {"generated_script": result}
