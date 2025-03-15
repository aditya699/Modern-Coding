# Customer Support Agent Chatbot

A modern customer support chatbot built with OpenAI Agents, FastAPI, and Gradio. This project demonstrates the power of AI-driven customer service automation using the latest OpenAI Agents library.

## 🌟 Features

- **AI-Powered Support Agent**: Utilizes OpenAI Agents for intelligent conversation handling
- **Order Status Tracking**: Connects with a local SQLite database to check order statuses
- **Interactive Web Interface**: Built with Gradio for a user-friendly chat experience
- **RESTful API**: FastAPI backend for robust and scalable performance
- **Real-time Response Streaming**: Smooth, natural-feeling conversation flow

## 🛠️ Technologies Used

- [OpenAI Agents](https://github.com/openai/openai-agents) - For intelligent agent-based conversations
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Gradio](https://gradio.app/) - For creating the interactive web interface
- [SQLite](https://www.sqlite.org/) - For order database management
- [Python 3.8+](https://www.python.org/) - Core programming language

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Project-1
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key and other configurations
```

### Running the Application

1. Start the FastAPI backend:
```bash
python main.py
```

2. In a new terminal, launch the Gradio interface:
```bash
python gradio_interface.py
```

3. Open your browser and navigate to `http://localhost:7860` to interact with the chatbot.

## 💡 Usage

1. Access the chat interface through your web browser
2. Type your customer support query (e.g., "What is my order status?")
3. The AI agent will process your request and provide relevant information
4. For order status queries, the system will check the orders database and return the current status

## 🔒 Environment Variables

Create a `.env` file with the following variables:
```
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=sqlite:///orders.db
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📧 Contact

For any questions or feedback, please reach out to [Your Contact Information]
