# Healthcare Chatbot Prototype

## Overview
This project is an **educational healthcare chatbot** built using Rasa, designed to assist users by diagnosing symptoms and suggesting basic over-the-counter remedies. It leverages a dataset from Kaggle to inform its responses, providing a simple, interactive way to explore healthcare-related queries. The bot is intended for learning purposes and not as a substitute for professional medical advice.

## Features
- **Symptom Diagnosis**: Responds to inputs like "I have a fever" with a possible diagnosis (e.g., "You might have a cold. Rest and hydrate!").
- **Medicine Suggestions**: Answers requests like "I need medicine for fever" with general suggestions (e.g., ibuprofen or acetaminophen).
- **Entity Recognition**: Extracts symptoms (e.g., "fever," "rash") to tailor responses.
- **Custom Actions**: Uses a Python-based action server for dynamic diagnosis logic.

## Tools and Technologies
- **Python 3.10**: Core programming language.
- **Rasa**: Open-source framework for building conversational AI.
- **SpaCy**: Used implicitly by Rasa for NLP tasks.
- **Kaggle**: Source of healthcare dataset for training (e.g., `kaggle_data.csv`).

## Project Structure
- `config.yml`: Rasa configuration (pipeline and policies).
- `data/nlu.yml`: Natural language understanding training data.
- `data/stories.yml`: Dialogue flow definitions.
- `domain.yml`: Intents, entities, slots, actions, and responses.
- `endpoints.yml`: Action server endpoint configuration.
- `actions/actions.py`: Custom action logic (e.g., `action_diagnose`).
- `data/*.csv`: Kaggle dataset and processed versions (excluded from Git if large).
- `scripts/*.py`: Preprocessing and NLU generation scripts.

## How to Run
1. **Setup Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt  
