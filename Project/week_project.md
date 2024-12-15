### Project: Building Your Own Chatbot Application  
#### Objective  
The goal of this project is to give you hands-on experience in designing and building a chatbot application. By the end of the week, you will have developed a working chatbot using Retrieval-Augmented Generation (RAG) techniques, incorporating a on-demand model from Amazon Bedrock

#### Key Technologies  
1. **Large Language Models (LLMs):** Understanding the core model functionalities.  
2. **RAG (Retrieval-Augmented Generation):** Combining LLMs with external knowledge retrieval for more accurate and domain-specific responses.  
3. **AWS Services:** S3 & Amazon Bedrock

---

### **Steps to Build Your Chatbot**  

#### **Day 1: Concept and Design**  
1. **Understand the Problem Domain:**  
   - Choose a domain for your chatbot (e.g., customer support, education, or healthcare).  
   - Define key functionalities.  

2. **Sketch the System Design:**  
   - Identify components: Local model, retrieval engine, database for external knowledge, and the user interface (UI).  
   - Visualize data flow from user input to final response.  

3. **Set Up AWS:**  
   - Set you credentials  
   - Familiarize yourself with S3 and Amazon Bedrock.  

#### **Day 2: Knowledge Base and Data Preparation**  
1. **Create a Knowledge Base:**  
   - Gather relevant documents for your chatbot’s domain.  
   - Preprocess and format data (e.g., clean up text, convert to JSON).  
   - Upload to S3 Bucket

2. **Build an Index:**  
   - Using Amazon Bedrock Knowledge Base, build a VectorDB

#### **Day 3: Model Setup**  
1. **Select a Pre-trained Model:**  
   - Use LLM available on Amazon Bedrock like **Claude 3 Haiku/ Mistral ...**

2. **Implement the RAG Pipeline:**  
   - Combine retrieval (from the index) with generation (model inference).  
   - Test the pipeline locally using sample questions.  
 
#### **Day 4: Frontend and Final Testing**  
**Create a Simple User Interface (UI):**  
   - Build a web-based or terminal-based chatbot interface using Streamlit.  
   - Make sure you can create multiple conversation
   - Integrate the UI with your backend API.  

**BONUS**: 
    - Use an agent to redirect the user request to ether the Knowledge Base or simply the LLM 

#### **Final Presentation**  
- Present your chatbot to the class, demonstrating its functionalities.  

---

### **Deliverables**  
1. Working chatbot application.  
2. System design diagram.  
3. Source code and documentation.  

This project provides you with practical experience in LLMs, RAG, and system design while building an end-to-end application.





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