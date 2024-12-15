# Retrieval Augmented Generation (RAG) Course

## Course Goals
The primary objectives of this course are to:
- Understand the fundamentals of Retrieval Augmented Generation (RAG)
- Learn how to implement RAG techniques using state-of-the-art tools and frameworks
- Explore multimodal RAG applications

## Course Agenda

1. Retrieval Augmented Generation Fundamentals Presentation
2. Amazon Bedrock Presentation (Live Demo)
3. Local Code: [Local Re-ranker Notebook](./reranking.ipynb)
4. [Naive RAG (Hugging Face)](https://huggingface.co/learn/cookbook/rag_with_hf_and_milvus)
5. [Multimodal RAG (Hugging Face)](https://huggingface.co/learn/cookbook/faiss_with_hf_datasets_and_clip)
6. This week deliverable [Project](../Project)

## Prerequisites
1. Create a Hugging Face Account
   - Visit [Hugging Face](https://huggingface.co/)
   - Generate an access token
   - Keep the token secure for use during the course

## Setting Up Your Development Environment

### Creating a Virtual Environment

#### Windows Users
1. Open PowerShell or Command Prompt as Administrator
2. Ensure Python is installed and accessible from the command line
3. Navigate to your project directory:
   ```powershell
   cd Code\
   ```
4. Create the virtual environment:
   ```powershell
   python -m venv .venv
   ```

#### Activating the Virtual Environment

##### Windows
```powershell
.venv\Scripts\activate
```

##### macOS/Linux
```bash
source .venv/bin/activate
```

### Managing Dependencies
1. Install project dependencies:
   ```powershell
   pip install -r ./day_X_X/requirements.txt
   ```

2. To deactivate the virtual environment:
   ```powershell
   deactivate
   ```

