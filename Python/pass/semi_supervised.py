import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier


# -----------------------------
# Load datasets
# -----------------------------
def load_data(labeled_path, unlabeled_path):

    labeled = pd.read_csv(labeled_path)
    unlabeled = pd.read_csv(unlabeled_path)

    X_labeled = labeled.drop("label", axis=1)
    y_labeled = labeled["label"]

    X_unlabeled = unlabeled.copy()

    return X_labeled, y_labeled, X_unlabeled


# -----------------------------
# Train initial model
# -----------------------------
def train_initial_model(X, y):

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    return model


# -----------------------------
# Generate pseudo labels
# -----------------------------
def generate_pseudo_labels(model, X_unlabeled, threshold=0.8):

    probs = model.predict_proba(X_unlabeled)
    preds = np.argmax(probs, axis=1)

    confidence = np.max(probs, axis=1)

    mask = confidence >= threshold

    pseudo_X = X_unlabeled[mask]
    pseudo_y = preds[mask]

    pseudo_df = pseudo_X.copy()
    pseudo_df["label"] = pseudo_y

    pseudo_df.to_csv("pseudo_labels.csv", index=False)

    return pseudo_X, pseudo_y


# -----------------------------
# Train final model
# -----------------------------
def train_final_model(X_labeled, y_labeled, pseudo_X, pseudo_y):

    X_combined = pd.concat([X_labeled, pseudo_X])
    y_combined = pd.concat([y_labeled, pd.Series(pseudo_y)])

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_combined, y_combined)

    return model


# -----------------------------
# Evaluation
# -----------------------------
def evaluate_model(model, X_test, y_test):

    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    return acc


# -----------------------------
# Main pipeline
# -----------------------------
def main():

    labeled_path = "labeled_data.csv"
    unlabeled_path = "unlabeled_data.csv"

    X_labeled, y_labeled, X_unlabeled = load_data(labeled_path, unlabeled_path)

    X_train, X_test, y_train, y_test = train_test_split(
        X_labeled, y_labeled, test_size=0.2, random_state=42
    )

    # Initial model
    initial_model = train_initial_model(X_train, y_train)
    initial_acc = evaluate_model(initial_model, X_test, y_test)

    # Generate pseudo labels
    pseudo_X, pseudo_y = generate_pseudo_labels(initial_model, X_unlabeled)

    # Train final model
    final_model = train_final_model(X_train, y_train, pseudo_X, pseudo_y)
    final_acc = evaluate_model(final_model, X_test, y_test)

    print("Initial Model Accuracy:", initial_acc)
    print("Final Model Accuracy:", final_acc)


if __name__ == "__main__":
    main()