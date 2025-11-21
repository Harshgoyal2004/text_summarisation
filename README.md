# Text Summarization with PEGASUS

An end-to-end text summarization system using the PEGASUS model from Hugging Face Transformers. This project implements a complete pipeline from data ingestion to model deployment with FastAPI.

## 🚀 Features

- **End-to-End Pipeline**: Data ingestion, validation, transformation, model training, and evaluation
- **Pre-trained Model**: Utilizes Google's PEGASUS model fine-tuned on the SAMSum dataset
- **REST API**: FastAPI-based web service for model inference
- **Containerized**: Docker support for easy deployment
- **CI/CD**: GitHub Actions workflow for automated testing and deployment
- **Model Persistence**: Saves and loads models locally to avoid retraining

## 📦 Prerequisites

- Python 3.9+
- pip
- Git
- Docker (optional, for containerization)
- AWS Account (for ECR deployment, optional)

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Harshgoyal2004/text_summarisation.git
   cd text_summarisation
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

## 🏃‍♂️ Quick Start

1. **Run the training pipeline**
   ```bash
   python main.py
   ```
   This will execute the complete pipeline:
   - Data Ingestion
   - Data Validation
   - Data Transformation
   - Model Training
   - Model Evaluation

2. **Start the FastAPI server**
   ```bash
   uvicorn app:app --reload
   ```

3. **Make predictions**
   ```bash
   curl -X 'POST' \
     'http://localhost:8000/predict' \
     -H 'Content-Type: text/plain' \
     -d 'Your long text to be summarized goes here...'
   ```

## 🐳 Docker Support

Build the Docker image:
```bash
docker build -t text-summarization .
```

Run the container:
```bash
docker run -p 8000:8000 text-summarization
```

## 📂 Project Structure

```
text_summarisation/
├── artifacts/                     # Stores processed data, models, and outputs
│   ├── data_ingestion/           # Raw and processed data
│   ├── data_transformation/      # Transformed datasets
│   ├── model_evaluation/         # Evaluation metrics
│   └── model_trainer/            # Trained models
├── config/                       # Configuration files
│   ├── config.yaml              # Main configuration
│   └── params.yaml              # Hyperparameters
├── src/                          # Source code
│   └── textSummarizer/
│       ├── components/           # Pipeline components
│       ├── config/               # Configuration management
│       ├── entity/               # Data classes
│       ├── logging/              # Logging configuration
│       ├── pipeline/             # Pipeline stages
│       └── utils/                # Utility functions
├── .github/workflows/            # CI/CD workflows
├── app.py                       # FastAPI application
├── Dockerfile                   # Container configuration
├── main.py                      # Main pipeline
└── requirements.txt             # Dependencies
```

## 🤖 Model Details

- **Base Model**: PEGASUS (Pre-training with Extracted Gap-sentences for Abstractive Summarization)
- **Dataset**: SAMSum (conversation summarization)
- **Training**: Fine-tuned on a single GPU
- **Inference**: Supports both CPU and GPU

## 🌐 API Endpoints

- `POST /predict`: Generate summary from input text
  - Content-Type: `text/plain`
  - Returns: Plain text summary

- `GET /train`: Trigger model training
  - Returns: Training status

- `GET /`: Health check
  - Returns: API status

## 🔧 Configuration

Edit `config/config.yaml` to modify:
- Dataset paths
- Model parameters
- Training settings
- Evaluation metrics

## 🚀 Deployment

The project includes a GitHub Actions workflow (`.github/workflows/main.yaml`) for CI/CD that:
1. Runs tests
2. Builds and pushes Docker image to AWS ECR
3. Deploys to a self-hosted runner

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Resources

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PEGASUS Paper](https://arxiv.org/abs/1912.08777)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
8. Update the app.py