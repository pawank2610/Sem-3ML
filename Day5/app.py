
import streamlit as st
import joblib
import pandas as pd
from pathlib import Path
import numpy as np

st.set_page_config(
    page_title="Iris Species Prediction",
    page_icon="🌸",
    layout="centered"
)

# File location
BASE_DIR = Path(r"C:\Sem-3 ML\Day5")

# Load saved files
@st.cache_resource
def load():
    model = joblib.load(BASE_DIR / "model.pkl")
    features = joblib.load(BASE_DIR / "features.pkl")
    targets = joblib.load(BASE_DIR / "target.pkl")
    return model, features, targets

try:
    model, feature_names, targets = load()
except FileNotFoundError as error:
    st.error(f"Required file not found: {error.filename}")
    st.info(
        "Run the training code in 1.ipynb first "
        "to create model.pkl, features.pkl and target.pkl."
    )
    st.stop()

# Page heading
st.title("🌸 Iris Flower Species Predictor")
st.write("Enter the flower measurements to predict its species.")

st.sidebar.header("🌿 Flower Measurements")

# Measurement ranges
ranges = {
    "sepal length (cm)": (4.0, 8.0, 5.1, 0.1),
    "sepal width (cm)": (2.0, 4.5, 3.5, 0.1),
    "petal length (cm)": (1.0, 7.0, 1.4, 0.1),
    "petal width (cm)": (0.1, 2.5, 0.2, 0.1),
}

inputs = {}

# Create sliders
for feature in feature_names:
    low, high, default, step = ranges.get(
        feature, (0.0, 10.0, 1.0, 0.1)
    )

    inputs[feature] = st.sidebar.slider(
        feature,
        min_value=float(low),
        max_value=float(high),
        value=float(default),
        step=float(step)
    )

# Prediction button
if st.button("Predict Species", type="primary"):

    X_input = pd.DataFrame(
        [[inputs[f] for f in feature_names]],
        columns=feature_names
    )

    prediction = model.predict(X_input)[0]

    # Convert prediction to species name
    def get_species_name(value):
        if isinstance(value, (int, np.integer)):
            if 0 <= value < len(targets):
                return str(targets[value])
        return str(value)

    species = get_species_name(prediction)

    st.success(f"🌼 Predicted Iris Species: {species}")

    # Display probabilities
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X_input)[0]

        classes = getattr(
            model, "classes_", range(len(probabilities))
        )

        probability_df = pd.DataFrame({
            "Species": [
                get_species_name(c) for c in classes
            ],
            "Probability (%)": np.round(
                probabilities * 100, 2
            )
        })

        st.subheader("📊 Prediction Probabilities")

        st.bar_chart(
            probability_df.set_index("Species")
        )

        st.dataframe(
            probability_df,
            hide_index=True,
            use_container_width=True
        )

        st.caption(
            "Probabilities are model estimates, not guarantees."
        )
