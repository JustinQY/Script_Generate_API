import os
from transformers import AutoTokenizer, AutoModelForCausalLM, T5Tokenizer, T5ForConditionalGeneration
from peft import PeftModel
from fastapi import FastAPI
from pydantic import BaseModel
from huggingface_hub import login

login(token=os.getenv("HF_TOKEN"))
print("Hugging Face Successfully Login!")

app = FastAPI()

# Load fine-tuned model and tokenizer
# tokenizer = AutoTokenizer.from_pretrained("./llama2-7b", local_files_only=True)
# base_model = AutoModelForCausalLM.from_pretrained("./llama2-7b", local_files_only=True)
# model = PeftModel.from_pretrained(base_model, "./checkpoint-5400", local_files_only=True)


tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-small")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-small")

# Define data structure of parameters
class PromptInput(BaseModel):
    prompt: str

# define API interface
# @app.post("/generate")
# def generate_script(input: PromptInput):
#     print("Starts Generating!")
#     inputs = tokenizer(input.prompt, return_tensors="pt")
#     print("Inputs Tokenized! Generating Begins~")
#     outputs = model.generate(**inputs, max_new_tokens=200)
#     print("Generating Succeed!")
#     result = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     print("Results formed!")
#     return {"generated_script": result}

@app.post("/generate")
def generate_script(input: PromptInput):
    print("Starts Generating!")
    inputs = tokenizer(input.prompt, return_tensors="pt").input_ids
    print("Inputs Tokenized! Generating Begins~")
    outputs = model.generate(inputs)
    print("Generating Succeed!")
    result = tokenizer.decode(outputs[0])
    print("Results formed!")
    return {"generated_script": result}
