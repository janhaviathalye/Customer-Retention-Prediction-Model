
from flask import Flask, jsonify, request, render_template
import nbformat
import subprocess
import os
import uuid
import papermill as pm
import json

app = Flask(__name__)

# Define the notebook name
NOTEBOOK_FILE = 'Customer_Retention_Prediction_Model.ipynb'


@app.route('/')
def home():
    return '''
    <h1>Customer Retention Prediction API</h1>
    <p>Use the <code>/execute-notebook</code> endpoint to submit a test dataset.</p>
    <p>Example using <code>curl</code>:</p>
    <pre>
    curl -X POST -F "test_dataset=@Churn_Modelling_Test.csv" http://localhost:5000/execute-notebook
    </pre>
    '''

@app.route('/upload', methods=['GET'])
def upload_form():
    return render_template('upload.html')

@app.route('/execute-notebook', methods=['POST'])
def execute_notebook():
    if 'test_dataset' not in request.files:
        return jsonify({'error': 'No test dataset file provided'}), 400
    
    test_file = request.files['test_dataset']
    
    # Save the uploaded test dataset to a unique file
    test_file_filename = f'test_dataset_{uuid.uuid4().hex}.csv'
    test_file.save(test_file_filename)
    
    # Generate unique filenames for the output notebook and metrics output
    output_notebook = f'output1.ipynb'
    metrics_output_filename = f'metrics_output.json'
    exited_customers_filename = f'exited_customers.json'
    
    try:
        # Execute the notebook using papermill, passing in the test dataset filename and metrics output filename
        pm.execute_notebook(
            NOTEBOOK_FILE,
            output_notebook,
            parameters=dict(
                test_data_path=test_file_filename,
                metrics_output_path=metrics_output_filename
            )
        )
        
        # Read the metrics output file
        
        with open(metrics_output_filename, 'r') as f:
            
            metrics = json.load(f)
        
        # Read the exited customers file
        with open('exited_customers.json', 'r') as f:
            exited_customers = json.load(f)
        
        # Render the dashboard template with metrics and exited customers
        return render_template('dashboard.html', metrics=metrics, exited_customers=exited_customers)
    
    except Exception as e:
        # Return any errors encountered
        return jsonify({'error': str(e)}), 500
    
    # finally:
    #     # Clean up the output notebook file, test dataset file, and metrics output file
    #     if os.path.exists(output_notebook):
    #         os.remove(output_notebook)
    #     if os.path.exists(test_file_filename):
    #         os.remove(test_file_filename)
    #     if os.path.exists(metrics_output_filename):
    #         os.remove(metrics_output_filename)

if __name__ == '__main__':
    app.run(port=5000)
