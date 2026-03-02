# 🤖 RM-AgenticAI-LangGraph

## Next-Gen AI-Powered Investment Advisor with Multi-Agent Intelligence

**RM-AgenticAI-LangGraph** is a cutting-edge financial advisory platform that leverages **multi-agent AI** and **state-of-the-art open-source LLMs** to deliver personalized investment insights, automated risk analysis, and context-aware recommendations — all through an interactive chat experience.

---

## 🌟 Key Highlights

* **WhatsApp-style AI Chat Assistant**
  Chat with an AI advisor just like messaging a human. It remembers **context across conversations**, understands slightly off-topic questions, and provides **intelligent, precise answers**.

* **Zero-Cost Open-Source LLM**
  Uses **Ollama’s LLaMA 3** model for inference — completely free, with advanced prompting to rival proprietary closed-source LLMs.

* **Multi-Agent Architecture**
  Dedicated agents for every aspect of financial advisory, working together seamlessly.

* **Real-Time, Personalized Insights**
  Automated risk profiling, goal success prediction, persona classification, and portfolio optimization.

* **End-to-End Workflow Automation**
  From prospect selection to AI-driven meeting preparation — everything is fully orchestrated.

---

## 🏗️ Architecture

### Multi-Agent System

| Agent                            | Responsibility                        |
| -------------------------------- | ------------------------------------- |
| 🔍 **Data Analyst Agent**        | Validates and processes client data   |
| 📊 **Risk Assessment Agent**     | ML-driven risk profiling              |
| 🎯 **Goal Planning Agent**       | Predicts investment goal success      |
| 👤 **Persona Agent**             | Behavioral and persona classification |
| 💼 **Product Specialist Agent**  | Personalized product recommendations  |
| 📈 **Portfolio Optimizer Agent** | Optimizes asset allocation            |
| ⚠️ **Compliance Agent**          | Ensures regulatory compliance         |
| 📋 **Meeting Coordinator Agent** | Generates intelligent meeting guides  |
| 🤖 **RM Assistant Agent**        | Context-aware AI chat advisor         |

### Workflow Overview

```
Data Input → Validation → Risk & Goal Analysis → Persona Classification
                                ↓
Portfolio Optimization ← Product Recommendation ← Compliance Check
                                ↓
Meeting Guide Generation → Interactive RM Assistant
```

---

## 🚀 Features

### Core Capabilities

* **Automated Risk Profiling**: Classify Low / Moderate / High risk automatically
* **Goal Success Prediction**: Estimate probability of achieving financial objectives
* **Persona Classification**: GenAI-driven behavioral insights
* **Product Recommendation**: Intelligent, context-aware matches with justification
* **Intelligent Meeting Preparation**: Auto-generated discussion guides
* **Interactive Chat Assistant**: Real-time, WhatsApp-style RM assistant

### Advanced Features

* **Context Memory Across Chats**: Remember past interactions to provide relevant answers
* **Parallel Processing**: Multi-prospect analysis at once
* **Conditional Workflows**: Adaptive paths based on client profile
* **Performance Monitoring**: Track agent efficiency and decision accuracy
* **Audit Trails**: Full traceability of all recommendations and actions

---

## 📁 Project Structure

```
RM-AgenticAI-LangGraph/
├── main.py                     # Streamlit application
├── config/                     # Logging & settings
├── langraph_agents/            # Multi-agent implementations
├── models/                     # ML models and encoders
├── data/                       # Input, training, and evaluation datasets
├── legacy/                     # Previous implementation
└── tests/                      # Unit & integration tests
```

---

## 🛠️ Installation

```bash
git clone https://github.com/Arpit-Dubey07/RM-AgenticAI-LangGraph.git
cd RM-AgenticAI-LangGraph
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Add API keys if needed
streamlit run app.py
```

---

## ⚙️ Configuration

```env
# OpenAI / Gemini keys (optional)
GEMINI_API_KEY_1=your_gemini_api_key_here

# LangSmith (monitoring)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key

# App Settings
LOG_LEVEL=INFO
ENABLE_MONITORING=true
```

---

## 🧪 Usage

1. **Select Prospect** – Load available clients
2. **Automated Analysis** – Multi-agent system processes data
3. **Review Insights** – Risk, goal, and persona evaluation
4. **Product Recommendations** – AI-driven suggestions
5. **Meeting Preparation** – Auto-generated discussion guides
6. **Interactive Chat** – WhatsApp-style AI advisor with memory

---

## 📊 Monitoring & Analytics

* **Agent Performance Metrics**: Execution times, success rates
* **Workflow Analytics**: Decision paths and bottleneck detection
* **Audit Trail**: Track every recommendation and action
* **Error Tracking**: Automatic recovery and reporting

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

MIT License – See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

* **LangGraph** – Multi-agent orchestration
* **Ollama LLaMA 3** – Free, open-source LLM
* **scikit-learn** – ML models
* **Streamlit** – Interactive UI

---

## 💡 Why It’s Fabulous

* WhatsApp-style AI chat with **memory and context understanding**
* **Zero-cost inference** using a **state-of-the-art open-source LLM**
* Fully automated **financial advisory workflow**
* **Modular agents** make it **extensible and production-ready**

---


Do you want me to do that next?
