# Day 1: Retrieval Augmented Generation (RAG)

## Overview

This module introduces Retrieval Augmented Generation (RAG), a powerful technique that combines information retrieval with large language models to create more accurate, knowledge-grounded AI systems.

## Learning Objectives

By the end of this module, you will:
- Understand the fundamentals of RAG architecture
- Master different retrieval approaches (bi-encoder, cross-encoder, reranking)
- Build a complete RAG pipeline with AWS Bedrock
- Evaluate RAG system performance using key metrics
- Apply best practices for production RAG systems

## Exercises

### 1. Bi-Encoder vs Cross-Encoder (`1_bi_cross_encoder.ipynb`)

**What you'll learn:**
- Difference between bi-encoder and cross-encoder architectures
- Implement cosine similarity for semantic search
- Compare performance trade-offs between approaches
- Understand when to use each method in production

**Key concepts:** Embeddings, semantic similarity, retrieval speed vs accuracy

**Duration:** 30-45 minutes

---

### 2. Advanced RAG Pipeline (`2_advanced_rag.ipynb`)

**What you'll learn:**
- Build a complete RAG system using LangChain and AWS Bedrock
- Implement intelligent document chunking strategies
- Create and query vector databases with FAISS
- Visualize embeddings in 2D space
- Combine retrieval and generation workflows

**Key concepts:** Document processing, vector databases, embedding visualization, prompt engineering

**Duration:** 60-90 minutes

---

### 3. Reranking for Improved Retrieval (`3_reranking.ipynb`)

**What you'll learn:**
- Implement two-stage retrieval (retrieve + rerank)
- Use ColBERT for reranking retrieved documents
- Measure the impact of reranking on result quality
- Optimize K values for different stages
- Integrate reranking into existing RAG pipelines

**Key concepts:** Two-stage retrieval, ColBERT, ranking optimization, hybrid approaches

**Duration:** 45-60 minutes

---

### 4. RAG Evaluation (`4_rag_evaluation.ipynb`)

**What you'll learn:**
- Evaluate retrieval quality with Precision, Recall, MRR, and NDCG
- Measure generation quality with faithfulness and relevance metrics
- Build comprehensive evaluation pipelines
- Visualize system performance with dashboards
- Apply best practices for continuous evaluation

**Key concepts:** Retrieval metrics, generation metrics, ground truth datasets, A/B testing

**Duration:** 60-75 minutes

## Prerequisites

### Required Accounts
- **AWS Account** with Bedrock access (for exercises 2-3)
- **Hugging Face Account** (optional, for additional resources)

### Software Requirements
- Python 3.8+
- Jupyter Notebook or JupyterLab
- AWS CLI (configured with credentials)

### Knowledge Prerequisites
- Basic Python programming
- Understanding of machine learning concepts
- Familiarity with transformers (helpful but not required)

## Setup Instructions

### 1. Create Virtual Environment

**macOS/Linux:**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows:**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure AWS Bedrock

1. Configure your AWS CLI profile:
   ```bash
   aws configure --profile myprofile
   ```

   Enter:
   - **Access Key ID**: Your AWS access key
   - **Secret Access Key**: Your AWS secret key
   - **Default region**: `us-east-1` (for Bedrock)

2. Verify configuration:
   ```bash
   aws configure list-profiles
   ```

3. Export profile for use:
   ```bash
   export AWS_PROFILE=myprofile  # macOS/Linux
   set AWS_PROFILE=myprofile     # Windows
   ```

### 4. Launch Jupyter

```bash
jupyter notebook
# or
jupyter lab
```

## Exercise Flow

We recommend completing the exercises in order:

```
1. Bi-Encoder vs Cross-Encoder
   ↓
   Learn retrieval fundamentals

2. Advanced RAG Pipeline
   ↓
   Build complete system

3. Reranking
   ↓
   Improve retrieval quality

4. RAG Evaluation
   ↓
   Measure and optimize performance
```

## Key Technologies

| Technology | Purpose | Exercise |
|------------|---------|----------|
| **Sentence Transformers** | Embedding generation | 1, 3, 4 |
| **AWS Bedrock** | LLM and embeddings | 2, 3 |
| **LangChain** | RAG orchestration | 2 |
| **FAISS** | Vector database | 2 |
| **RAGatouille** | ColBERT reranking | 3 |
| **NumPy/Pandas** | Data processing | All |
| **Matplotlib/Seaborn** | Visualization | All |

## Common Issues and Solutions

### Issue: AWS Bedrock Access Denied
**Solution:** Ensure your AWS account has Bedrock enabled in `us-east-1` region. Request model access in the Bedrock console.

### Issue: Out of Memory
**Solution:** Reduce batch sizes or use smaller models. For exercise 2, reduce the dataset size (change `train[:100]` to `train[:50]`).

### Issue: Slow Embedding Generation
**Solution:** Use GPU if available. For CPU-only, reduce document count or use smaller embedding models.

### Issue: Module Not Found
**Solution:** Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

## Additional Resources

### Documentation
- [LangChain Documentation](https://python.langchain.com/)
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Sentence Transformers Documentation](https://www.sbert.net/)
- [FAISS Documentation](https://faiss.ai/)

### Tutorials
- [HuggingFace RAG Tutorial](https://huggingface.co/learn/cookbook/rag_with_hf_and_milvus)
- [Multimodal RAG with CLIP](https://huggingface.co/learn/cookbook/faiss_with_hf_datasets_and_clip)

### Research Papers
- [RAG: Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [ColBERT: Efficient and Effective Passage Search](https://arxiv.org/abs/2004.12832)

## Next Steps

After completing Day 1, you'll be ready to:
- Explore fine-tuning techniques (Day 2)
- Learn about RLHF and advanced evaluation (Day 3)
- Build agentic RAG systems (Day 4)
- Complete the capstone RAG project

## Support

If you encounter issues:
1. Check the **Common Issues** section above
2. Review notebook markdown explanations
3. Consult the **Additional Resources**
4. Ask your instructor during lab sessions

---

**Happy Learning!** 🚀
