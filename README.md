#  Agents of Justice

**Agents of Justice** is a courtroom simulation system powered by Large Language Models (LLMs). It brings to life a virtual courtroom where intelligent agents take on roles such as Judge, Plaintiff, Defendant, Defense Lawyer, and Prosecuting Lawyer. The goal is to create an interactive and intelligent legal simulation that mimics real-world judicial proceedings.

---

##  Overview

The simulation proceeds in four key phases:

1. **Opening Statements** – Each lawyer presents a brief overview of their case.
2. **Witness Interrogation & Argumentation** – Agents present arguments, question witnesses, and counter opposing claims.
3. **Closing Statements** – A final plea summarizing their stance and evidence.
4. **Judge's Ruling** – The Judge agent evaluates the arguments and delivers a verdict.

---

##  Features

- Role-based LLM agents with contextual memory
- Dynamic courtroom interactions and dialogue
- Modular and extendable simulation structure
- Dataset-driven case generation
- Structured legal proceedings with multi-phase execution

---

##  Project Structure

```
Agents-of-Justice/
├── agents/                 # Code for each courtroom agent
│   ├── judge.py
│   ├── plaintiff.py
│   └── defense.py
├── data/                   # CSV or JSON case data
│   └── data.csv
├── prompts/                # Prompt templates for each role
├── simulations/            # Scripts to run specific trial scenarios
├── utils/                  # Helper and utility functions
├── gradio_app.py           # Entry point to run the courtroom simulation through gradio
├── requirements.txt        # Python dependencies
└── README.md               # You're reading it
```

---

##  Installation

1. **Clone the repository:**

```
git clone https://github.com/your-username/agents-of-justice.git
cd agents-of-justice
```

2. **Install dependencies:**

```
pip install -r requirements.txt
```

3. **Run the simulation:**

```
python main.py
```

---

## Built by:

**Naman Shetty** ([LinkedIn](https://www.linkedin.com/in/naman-v-shetty))
---
