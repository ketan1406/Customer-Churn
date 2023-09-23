from fastapi import FastAPI
from pydantic import BaseModel
import joblib  # You'll need this to load your trained model
import os

# Create an instance of FastAPI
app = FastAPI()

# Define a Pydantic model for input data


class CustomerData(BaseModel):
    age: float
    subscription_length_months: int
    total_usage_gb: float
    gender_encoded: int
    location_encoded: int
    monthly_bill: float


# Load your trained model (replace 'model.pkl' with
model_file_path = os.path.join(os.path.dirname(
    __file__), 'logistic_regression_model.pkl')

# Load the model
model = joblib.load(model_file_path)

# Define a prediction endpoint


@app.post("/predict/")
async def predict_churn(data: CustomerData):
    # Convert input data to a dictionary
    input_data = data.dict()

    # Make predictions using your loaded model
    input_values = list(input_data.values())
    prediction = model.predict([input_values])

    # Assuming your model predicts 0 for no churn and 1 for churn
    if prediction[0] == 0:
        result = "No Churn"
    else:
        result = "Churn"

    return {
        "input_data": input_data,
        "prediction": result
    }


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
