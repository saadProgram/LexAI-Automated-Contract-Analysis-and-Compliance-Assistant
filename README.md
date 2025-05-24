
# LexAI - AI-Powered Legal Contract Analysis Assistant

## Overview

LexAI is an advanced AI-powered legal assistant designed to automate contract analysis and streamline compliance evaluation. By leveraging state-of-the-art NLP technologies, LexAI intelligently extracts, analyzes, and compares contract clauses to identify potential compliance risks with unprecedented efficiency.

## Key Features

- **Automated Contract Analysis**: Processes PDF/TXT documents to extract and classify legal clauses
- **Compliance Risk Scoring**: Assigns risk scores (1-10) with clear justifications for each clause
- **Retrieval-Augmented Generation (RAG)**: Combines Google's Gemini 2.0 Flash model with document retrieval for accurate analysis
- **Similarity Search**: Compares clauses against database of similar documents using ChromaDB
- **Natural Language Interface**: Allows intuitive queries about contract content and risks
- **Document Processing Pipeline**: Robust system for ingesting and processing legal documents
- **LangGraph Workflow**: Coordinates multi-step analysis for consistent results
- **Risk-Highlighted Comparisons**: Visualizes potential issues in contract comparisons
- **Audit Trails & Reports**: Generates detailed documentation of analysis process

## Technology Stack

- **AI Model**: Google Gemini 2.0 Flash
- **Vector Database**: ChromaDB
- **Metadata Storage**: SQLite
- **Workflow Orchestration**: LangGraph
- **Dataset**: Processed CUAD (Contract Understanding Atticus Dataset)

## Requirements

The project dependencies are listed in `requirements.txt`. To install all required packages, run:

```bash
pip install -r requirements.txt
```

## Dataset

This project utilizes a processed version of the CUAD dataset:
- **Original Contents**:
  - 28 labeled Excel files with clause-level annotations
  - 510 full contract PDFs/TXTs as source data
- **Processing**:
  - Clauses and labels merged into unified format
  - Filename as first column with categorized clause text and annotations

Reference:  
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., & Steinhardt, J. (2021). CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review. arXiv preprint arXiv:2103.06268. https://arxiv.org/abs/2103.06268

## Benefits

- **Reduced contract review time** through automated analysis
- **Standardized evaluations** across legal teams
- **Improved consistency** in risk assessment
- **Non-obvious risk detection** through AI analysis
- **Full document integrity** maintained via read-only processing
- **Jurisdictional adaptability** for various contract types and regions
.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.
