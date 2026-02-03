## Set up

1. Create a new folder  
2. Open it in vs code  
3. Create a new venv
    ```bash  
    python -m venv venv  
    ```
4. Activate venv  
    ```bash  
    venv\Scripts\Activate   
    ```
5. Create the `requirements.txt`  
6. install packages from `requirements.txt` 
    ```bash  
    pip install -r requirements.txt  
    ```   
7. Verify LangChain installation
    * Create test.py
    * Add below code
    ```python
    import langchain
    print(langchain.__version__)
    ```
    * run
    ```bash
    python test.py
    ```


## Required Modules
```bash
# LangChain Core
langchain
langchain-core

# OpenAI Integration
langchain-openai
openai

# Anthropic Integration
langchain-anthropic

# Google Gemini (PaLM) Integration
langchain-google-genai
google-generativeai

# Hugging Face Integration
langchain-huggingface
transformers
huggingface-hub

# Environment Variable Management
python-dotenv

# Machine Learning Utilities
numpy
scikit-learn
```