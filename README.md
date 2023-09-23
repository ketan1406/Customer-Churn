Customer Churn Prediction

This project aims to predict customer churn using machine learning techniques. Customer churn refers to the phenomenon where customers stop doing business with a company, such as canceling a subscription or discontinuing a service.

Project Structure
The project follows the following directory structure:

Customer-Churn-Prediction/
├── data/ # Data directory
│ ├── raw/ # Raw data file
├── notebooks/ # Jupyter notebook
│ ├── notebook.ipynb # Notebook with assignment work
├── app/ # FastAPI application for model deployment
│ ├── main.py # FastAPI application code
│ ├── logistic_regression_model.pkl # Trained model file
├── requirements.txt # List of project dependencies
├── README.md # Project README with an overview and instructions

API Documentation
You can access the model by using the following curl command. An example is given below:
curl -X POST "http://localhost:8000/predict/" -H "Content-Type: application/json" -d "{\"age\": 35, \"subscription_length_months\": 12,\"monthly_bill\": 66.4, \"total_usage_gb\": 50.0, \"gender_encoded\": 0, \"location_encoded\": 2}"
