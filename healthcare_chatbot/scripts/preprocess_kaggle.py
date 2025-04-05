import pandas as pd
import spacy

df = pd.read_csv("data/kaggle_data.csv")
nlp = spacy.load("en_core_web_sm")
processed_data = []

for index, row in df.iterrows():
    question = str(row["short_question"])
    answer = str(row["short_answer"])

    doc = nlp(question)
    entities = [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]

    if "have" in question.lower() or "feel" in question.lower():
        intent = "ask_symptom"
        if not entities:
            symptom_text = question.lower().split("have " if "have" in question.lower() else "feel ")[-1].strip()
            start = question.lower().index(symptom_text)
            entities = [(start, start + len(symptom_text), "SYMPTOM")]
    elif "need" in question.lower() or "for" in question.lower():
        intent = "request_medicine"
        if not entities:
            medicine = answer.lower().split(" ")[-1].strip(".")
            start = len(question)  # Medicine isn’t in question, so append
            entities = [(start, start + len(medicine), "MEDICINE")]
    else:
        continue

    processed_data.append({
        "question": question,
        "intent": intent,
        "entity_start": entities[0][0] if entities else 0,
        "entity_end": entities[0][1] if entities else 0,
        "entity_label": entities[0][2] if entities else ""
    })

processed_df = pd.DataFrame(processed_data)
processed_df.to_csv("data/processed_healthcare_data.csv", index=False)
print("Saved to data/processed_healthcare_data.csv")
