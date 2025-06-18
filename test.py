from transformers import AutoTokenizer, pipeline
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM

# Define base model and adapter paths
base_model = "TinyLlama/TinyLlama_v1.1"
adapter_path = "adapter"  # LoRA folder

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model)
tokenizer.pad_token = tokenizer.eos_token  # Fix padding

# Load base model
base = AutoModelForCausalLM.from_pretrained(
    base_model, device_map="cpu", torch_dtype="auto", offload_folder="offload"
)

# Load LoRA adapter on top of base
model = PeftModel.from_pretrained(base, adapter_path)

# Create text-generation pipeline
generator = pipeline(
    "text-generation", model=model, tokenizer=tokenizer, device_map="auto"
)

# Inference
prompt = "### Question:\nHow to list files in a directory?\n\n### Answer:\n"
output = generator(prompt, max_new_tokens=100)[0]["generated_text"]
print(output)
