import pandas as pd
from transformers import pipeline

from controllers import ui_controller


def generate_categories(file, csv = True, load_popup =False ):
    # Initialize zero-shot classification pipeline (using PyTorch)
    # Compared facebook/bart-large-mnli and cross-encoder/nli-distilroberta-base nlp model
    # FInal app is using  since it is faster cross-encoder/nli-distilroberta-base

    if load_popup:
        loading = ui_controller.show_loading_message()
    classifier = pipeline(
        "zero-shot-classification",
        model="cross-encoder/nli-distilroberta-base",
        framework="pt"
    )
    df = pd.DataFrame()
    if csv:
        # Load CSV
        df = pd.read_csv(file)  #
    else :
        df =file


    candidate_labels = ["Food", "Transport", "Shopping", "Entertainment", "Bills", "Salary", "Healthcare", "Education","Other"]


    results = []
    for desc in df['description']:
        output = classifier(desc, candidate_labels)
        top_label = output['labels'][0]
        results.append(top_label)

    # Add predictions to the DataFrame
    df['category'] = results

    loading.close()
    return df




