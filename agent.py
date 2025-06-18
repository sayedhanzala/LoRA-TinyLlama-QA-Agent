import json
import os
import sys
import re
from datetime import datetime

from transformers import pipeline, AutoTokenizer
from peft import AutoPeftModelForCausalLM

# Setup paths
ADAPTER_PATH = "adapter"
LOG_PATH = "logs/trace.jsonl"
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

# Load tokenizer & model
tokenizer = AutoTokenizer.from_pretrained(ADAPTER_PATH)
tokenizer.pad_token = tokenizer.eos_token

model = AutoPeftModelForCausalLM.from_pretrained(
    ADAPTER_PATH,
    device_map="auto",
    torch_dtype="auto",
    offload_folder="offload",
)

# Inference pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
)


# Prompt template
def build_prompt(user_input):
    return f"### Question:\n{user_input}\n\n### Answer:\n"


# Extract first command from output
def extract_first_command(text):
    lines = text.strip().splitlines()
    for line in lines:
        if re.match(
            r"^\s*\$?\s*(cd|ls|git|grep|tar|mkdir|rm|mv|cp|python|pip|bash|echo)\b",
            line.strip(),
        ):
            return line.strip().lstrip("$").strip()
    return None


# Logging function
def log_trace(instruction, arg, plan, command=None):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "instruction": arg,
        "generated_plan": plan,
        "dry_run_command": command or "None",
    }
    with open(LOG_PATH, "a") as f:
        f.write(json.dumps(log_entry) + "\n")


# Main entrypoint
def main():
    if len(sys.argv) < 2:
        print("❗ Please provide an instruction as an argument.")
        print("Usage: python agent.py \"create a new git branch\"")
        return

    instruction = " ".join(sys.argv[1:]) + " give me the command"
    arg = " ".join(sys.argv[1:])
    # instruction = input("Enter your CLI instruction: ")

    prompt = build_prompt(instruction)

    print(f"\n📥 Instruction: {arg}")
    output = generator(prompt, return_full_text=False, max_new_tokens=100)[0][
        "generated_text"
    ]

    # Extract answer part only
    answer = output.split("### Answer:")[-1].strip()

    print("\n🤖 Generated Plan:\n" + answer)

    # Dry-run first shell command
    command = extract_first_command(answer)
    if command:
        print(f"\n💡 Dry-run command:\n$ echo {command}")
    else:
        print("\n⚠️ No shell command detected in first line.")

    # Log everything
    log_trace(instruction, arg, answer, command)


if __name__ == "__main__":
    main()
