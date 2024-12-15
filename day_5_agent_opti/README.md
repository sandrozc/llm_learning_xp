# Agentic Workflow & MLOPs System Design

## Course Goals
The primary objectives of this course are to:
- Understand the fundamentals of Agentic Workflow & Some MLOPs System Desing
- Learn how to implement inline Amazon Bedrock Agent
- Understand LLM Inference tradeoffs

## Course Agenda

1.  Agentic Workflow & MLOPs System Desing & LLM Inference Presentation
2. Amazon Bedrock Agent Presentation (Live Demo)
3. Local Code: [Inline Agent Notebook](./inline_agent.ipynb)
4. Project presentation [Project](../Project)

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

### Configure AWS Profile 
1. On the CLI, configure your AWS profile:
   ```bash
   aws configure --profile myprofile
   ```
   Enter:
   - Access Key ID
   - Secret Access Key
   - Default region name: eu-west-3

2. Verify your profile:
   ```bash
   aws configure list-profiles
   ```

3. Export your profile:
   ```bash
   export AWS_PROFILE=myprofile
   ```

