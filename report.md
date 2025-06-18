### 📌 Project Summary – Fenrir AI/ML Internship Task

#### 🧠 Objective

Fine-tune a small open-weights LLM on a custom dataset of Q&A prompts and evaluate improvements in generation quality.

#### 🧰 Base Model

- **Model:** TinyLlama_v1.1
- **Format:** 4-bit quantized with LoRA (Low-Rank Adaptation)

#### 📚 Dataset

- **Source:** Custom JSON with ≥150 validated technical Q&A pairs
- **Topics:** Git, Python, pip, virtual environments, shell commands, etc.

#### 🏋️‍♂️ Training

- **Hardware:** Google Colab (T4 GPU)
- **Adapter:** LoRA (stored under 500 MB)
- **Duration:** 1 epoch
- **Tools:** PEFT, bitsandbytes, transformers

#### 📊 Evaluation

- **Static:** Manual comparison between base and fine-tuned outputs on 5 main prompts + 2 edge cases
- **Dynamic:** ROUGE-L scoring
  - Base ROUGE-L avg: **0.507**
  - Fine-tuned ROUGE-L avg: **0.586**

#### ✅ Results

- Fine-tuned model provides more specific, accurate, and structured answers
- Adapter remains lightweight and deployable

#### 🛠 Inference

Run via:

```bash
python agent.py
```

- A text input will appear in the terminal.
- Write your question in the text input.
- Press enter to get the fine-tuned model’s response.

#### 📽 Demo Video

> See Loom/MP4 submission for walkthrough and live testing

#### 🚀 Impact

- Demonstrates low-resource fine-tuning and evaluation pipeline
- Readily deployable as a lightweight Q&A assistant

---