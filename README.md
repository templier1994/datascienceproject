# End to End Data Science Project
This project is an end to end data science project used to train MLOps.



### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation -- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation -- MLFLOW,Dagshub

## Workflows

1. Update config.yaml-- config.yaml = folder with input/output for all task in the pipeline
2. Update schema.yaml  -- schema of the data (columns with type and target)
3. Update params.yaml
4. Update the entity -- Dataclass that contain config.
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py


### Run
to run the projet don't forget to add DagsHub credential into src/datascience/components/model_evaluation.py