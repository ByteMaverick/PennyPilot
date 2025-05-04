import pandas as pd
from transformers import pipeline


def generate_categories(csvPath):
    # Initialize zero-shot classification pipeline (using PyTorch)
    classifier = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli",
        framework="pt"
    )

    # Load CSV
    df = pd.read_csv(csvPath)  #


    candidate_labels = ["Food", "Transport", "Shopping", "Entertainment", "Bills", "Salary", "Healthcare", "Education","Other"]


    results = []
    for desc in df['description']:
        output = classifier(desc, candidate_labels)
        top_label = output['labels'][0]
        results.append(top_label)

    # Add predictions to the DataFrame
    df['category'] = results

    return df




