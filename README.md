# 🧠 Reflection Agent (LangGraph + LangChain)

This project is a simple **AI reflection loop agent** that improves Twitter posts using an iterative generate → critique → refine workflow.

It uses:
- LangGraph (for orchestration)
- LangChain (for prompt + LLM chaining)
- Groq LLM (fast inference)

---

## 🚀 What This Project Does

Given a tweet, the system:

1. **Generates** an improved version  
2. **Reflects** on it (critiques + suggestions)  
3. **Refines** the tweet again  
4. Repeats this loop multiple times  
5. Stops after a few iterations  

👉 Result: progressively better, more polished tweets

---

## 🧩 Project Structure
- main.py # Graph logic + execution
- chains.py # LLM chains (generation + reflection)
- pyproject.toml # Dependencies (Poetry)
- poetry.lock


---

## ⚙️ How It Works

### 1. `chains.py` (LLM Logic)

Defines two core chains:

- **Generation Chain**
  - Writes or improves a tweet
  - Acts like a Twitter tech influencer

- **Reflection Chain**
  - Critiques the tweet
  - Suggests improvements (style, virality, clarity)

Both chains use:
- `ChatPromptTemplate`
- `ChatGroq` as the LLM

---

### 2. `main.py` (Agent Graph)

Uses **LangGraph** to create a loop: GENERATE → REFLECT → GENERATE → ... → END


#### Key Components:

- **State (`MessageGraph`)**
  - Stores conversation messages
  - Automatically appends new messages (no overwrite)

- **Nodes**
  - `generation_node` → calls generation chain
  - `reflection_node` → calls reflection chain

- **Flow Control**
  - Loop continues until message count > 6
  - Then graph stops

---

## 🔁 Execution Flow

1. Input tweet is passed as a message
2. Graph starts at `GENERATE`
3. Output goes to `REFLECT`
4. Feedback is added to conversation
5. Loop continues
6. Final improved result is returned

---

## 🛠️ Setup & Installation

### 1. Install dependencies (Poetry)
```bash
poetry install
```
### 2. Activate environment
```bash
poetry shell
```
### 3. Add environment variables
- Create a .env file: using .env.example
GROQ_API_KEY=your_api_key_here
LANGCHAIN_API_KEY=your_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=reflection agent

### 4. Run the Project
```bash
python main.py
```

## 📈 Output
- Improved tweet versions
- Iterative refinement
- Final optimized tweet

## 💡 Key Concepts
- LangGraph loops (stateful AI workflows)
- Message passing state
- Reflection-based agents
- Prompt engineering for iteration

## 🔐 Notes
- .env is ignored (do not commit API keys)
- Uses Groq instead of OpenAI for cost efficiency

## 🎯 Future Improvements
- Add UI (Streamlit / FastAPI)
- Add memory persistence
- Control iteration count dynamically
- Support multiple content types (blogs, LinkedIn posts)


## 👤 Author
Vinay — building real-world AI systems 🚀

