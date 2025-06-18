### 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/sayedhanzala/fenrir-task.git
cd fenrir-task
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **(Optional) Run on Google Colab**

> Recommended for GPU usage. Use the `notebook.ipynb` provided and ensure runtime is set to **GPU (T4)**.

---

### 📂 Directory Structure

```
.
├── data/
│   └── qa_data.json                 # ≥150 validated Q&A pairs, used tldr repository as a source
├── lora-tinyllama/                  # LoRA adapter directory (≤ 500MB)
├── agent.py                         # Inference script
├── TinyLlama_QnA.ipynb              # Training & inference notebook
├── eval_static.md                   # Static evaluation with comparison table
├── eval_dynamic.md                  # Dynamic evaluation with ROUGE-L scores
├── report.md                        # One-page summary
├── README.md                        # This file
└── requirements.txt                 # Python dependencies
```

---

### 🏋️ Model Training

1. **Dataset:** Located at `data/qa_data.json` with 150+ Q&A pairs, used [tldr](https://github.com/tldr-pages/tldr) repository as a source
2. **Base Model:** `TinyLlama/TinyLlama_v1.1`
3. **Finetuning Method:** LoRA with PEFT library (4-bit quantization)
4. **Training:** Run the cells in `TinyLlama_QnA.ipynb` or adapt the same logic in a `.py` script.

---

### 🤖 Running the Agent

After training:

```bash
python agent.py
```

- A text input will appear in the terminal.
- Write your question in the text input.
- Press enter to get the fine-tuned model’s response.

---

### 📊 Evaluation

- **Static Evaluation:** See `eval_static.md` for prompt-wise base vs fine-tuned outputs.
- **Dynamic Evaluation:** See `eval_dynamic.md` for ROUGE-L metrics and quality scores.

---

### 📹 Demo Video

Loom/MP4 link: [\[Video\]](https://www.loom.com/share/28469253202b4fc1ab6fba84c4bf0d01?sid=610bf449-c6f6-4dbd-b554-7cc58de6a310)

---