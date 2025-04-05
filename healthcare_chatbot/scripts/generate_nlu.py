import pandas as pd

# Function to remove special characters
def sanitize_text(text):
    return ''.join(c for c in str(text) if ord(c) < 128)  # Keep only ASCII

df = pd.read_csv("data/processed_healthcare_data.csv")
print("version: \"3.1\"\nnlu:")
for intent in df["intent"].unique():
    print(f"- intent: {intent}\n  examples: |")
    for _, row in df[df["intent"] == intent].iterrows():
        question = sanitize_text(row['question'])
        entity_text = sanitize_text(question[row['entity_start']:row['entity_end']])
        print(f"    - {question} [{entity_text}]({row['entity_label']})")
