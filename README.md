# Code-Review-Analyst

# Codalyze

Codalyze is an AI-powered code review tool built with Streamlit and LangChain using the LLaMA-3 model via Groq or other LLM providers. It takes a `.py` file as input and returns a detailed code review including suggestions, improvements, and line-by-line analysis.

## Features

* Upload any `.py` file and receive a detailed review
* Uses powerful large language models for code analysis
* Outputs line-by-line suggestions and improvement tips
* Option to download the review as a `.txt` file
* Built with Streamlit for a clean, interactive UI

## Setup Instructions

1. Clone the repository

```bash
git clone https://github.com/thelakshyadubey/Code-Review-Analyst.git
cd Code-Review-Analyst
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Set up the environment variable

Create a `.env` file in the root directory and add your API key:

```
GROQ_API_KEY=your_api_key_here
```

If using other providers like DeepInfra or TogetherAI, update accordingly.

4. Run the app

```bash
streamlit run app.py
```

## File Structure

```
.
├── app.py              # Main Streamlit app
├── .env                # Environment file with API key
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

## Model Used

Currently configured to use:

* Model: LLaMA-3 70B via Groq (`langchain_groq`)

## Author
Lakshya Dubey

## Preview
![image](https://github.com/user-attachments/assets/c4559544-7bf7-4954-93dd-0013162fe371)
![image](https://github.com/user-attachments/assets/0000d5c1-c361-4d8f-98ee-bca7d526d89c)
![image](https://github.com/user-attachments/assets/620b3bdb-d19a-4241-8808-ff3f15e21d78)
