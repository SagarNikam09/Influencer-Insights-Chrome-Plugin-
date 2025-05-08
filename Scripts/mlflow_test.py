import mlflow
import random

# Set up MLflow tracking URI
mlflow.set_tracking_uri("http://ec2-3-83-39-47.compute-1.amazonaws.com:5000/")

with mlflow.start_run() as run:
    # Log a parameter (key-value pair)
    mlflow.log_param("param1", 5)

    # Log a metric; metrics can be updated throughout the run
    mlflow.log_metric("foo", random.random())
    mlflow.log_metric("foo", random.random() + 1, step=2)
    mlflow.log_metric("foo", random.random() + 2, step=3)   

    mlflow.log_metric("foo", random.random() + 3, step=4)