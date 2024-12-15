# RAG Chatbot with PDF Conversion and Streamlit Interface

This project implements a Retrieval-Augmented Generation (RAG) chatbot with a Streamlit interface and includes a PDF to Markdown converter.

The RAG chatbot leverages the LangChain library to create a conversational AI that can retrieve relevant information from a knowledge base to assist in answering user questions. The chatbot uses the BedrockChat language model and an Amazon Knowledge Bases Retriever for enhanced response generation.

Additionally, the project includes a utility script for converting PDF files to Markdown format, which can be useful for preparing documentation or knowledge base content.

## Repository Structure

- `day_4_rlhf/`
  - `convert_pdf_to_md.py`: Script for converting PDF files to Markdown format
  - `mdfiles/`: Directory containing Markdown files (likely output from PDF conversion)
- `Project/`
  - `vanilla_project/`
    - `app/`
      - `rag_chatbot_app.py`: Streamlit application for the RAG chatbot interface
      - `rag_chatbot_lib.py`: Library containing core functionality for the RAG chatbot
    - `starting_guide.md`: Guide for getting started with the project
  - `week_project.md`: Project overview or weekly progress document

## Usage Instructions

### Installation

1. Ensure you have Python 3.7+ installed.
2. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_name>
   ```
3. Install the required dependencies:
   ```
   pip install streamlit langchain pdfminer.six markdown boto3
   ```

### PDF to Markdown Conversion

To convert a PDF file to Markdown:

1. Navigate to the `day_4_rlhf` directory:
   ```
   cd day_4_rlhf
   ```
2. Run the conversion script:
   ```
   python convert_pdf_to_md.py
   ```
3. The script will convert `bedrock-ug.pdf` to `bedrock-ug.md` in the same directory.

### Running the RAG Chatbot

To start the RAG chatbot Streamlit application:

1. Navigate to the `Project/vanilla_project/app` directory:
   ```
   cd Project/vanilla_project/app
   ```
2. Run the Streamlit app:
   ```
   streamlit run rag_chatbot_app.py
   ```
3. Open your web browser and go to the URL provided by Streamlit (usually `http://localhost:8501`).

### Configuration

Before running the chatbot, ensure you have:

1. Set up your AWS credentials with the profile name "myprofile".
2. Created an Amazon Knowledge Base with ID "J9ILKVUWWO".
3. Configured the BedrockChat model in `rag_chatbot_lib.py` if necessary.

### Chatbot Usage

1. Type your message in the chat input box.
2. The chatbot will respond using information from the knowledge base and the conversation history.
3. The chat history is maintained throughout the session.

### Troubleshooting

- If you encounter AWS credential errors, ensure your "myprofile" is correctly set up in your AWS configuration.
- For issues with the Knowledge Base retriever, verify that the Knowledge Base ID is correct and accessible.
- If the chatbot responses are unexpected, check the `max_tokens`, `temperature`, and other model parameters in `get_llm()` function of `rag_chatbot_lib.py`.

## Data Flow

The RAG chatbot application follows this data flow:

1. User input is received through the Streamlit interface.
2. The input is passed to the `get_rag_chat_response` function in `rag_chatbot_lib.py`.
3. The function initializes the BedrockChat LLM and AmazonKnowledgeBasesRetriever.
4. A retrieval chain is created, combining the user input with relevant information from the knowledge base.
5. The LLM processes the combined information to generate a response.
6. The response is returned to the Streamlit app and displayed to the user.
7. The conversation history is updated in the Streamlit session state.

```
[User Input] -> [Streamlit Interface] -> [RAG Chatbot Library]
                                         |
                                         v
[BedrockChat LLM] <-> [Retrieval Chain] <-> [Amazon Knowledge Bases Retriever]
                                         |
                                         v
[Generated Response] -> [Streamlit Interface] -> [User Display]
```

Note: The PDF conversion process is separate and does not interact with the chatbot data flow.