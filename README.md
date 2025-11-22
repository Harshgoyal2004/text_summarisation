# 📝 Text Summarization with PEGASUS

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An end-to-end text summarization system using the state-of-the-art PEGASUS model from Google Research, fine-tuned on the SAMSum dataset. This project implements a complete MLOps pipeline from data ingestion to model deployment with FastAPI, featuring containerization and CI/CD integration.

## 🌟 Key Features

### 🏗️ End-to-End Pipeline
- **Data Processing**: Automated data ingestion, validation, and transformation
- **Model Training**: Fine-tuning of pre-trained PEGASUS model
- **Evaluation**: Comprehensive metrics including ROUGE scores
- **API**: Production-ready FastAPI service with Swagger documentation

### 🚀 Deployment Ready
- **Docker** containerization for consistent environments
- **REST API** with request/response validation
- **Model Versioning**: Save and load different model versions
- **Logging**: Comprehensive logging for debugging and monitoring

### 🔄 MLOps Integration
- **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions
- **Configuration Management**: YAML-based configuration for all components
- **Experiment Tracking**: Log training metrics and parameters

## � Prerequisites

- Python 3.9+
- pip (latest version)
- Git
- Docker 20.10+ (for containerization)
- AWS Account (optional, for cloud deployment)
- CUDA-compatible GPU (recommended for training)

## 🛠 Installation

### Option 1: Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Harshgoyal2004/text_summarisation.git
   cd text_summarisation
   ```

2. **Set up a virtual environment**
   ```bash
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Install core requirements
   pip install -r requirements.txt
   
   # Install package in development mode
   pip install -e .
   
   # Install development dependencies (optional)
   pip install -r requirements-dev.txt
   ```

### Option 2: Using Docker

```bash
# Build the Docker image
docker build -t text-summarization .

# Run the container
docker run -p 8000:8000 text-summarization
```

## 🚀 Quick Start

### 1. Configuration
Update the configuration files in `config/` as per your requirements:
- `config.yaml`: Main configuration
- `params.yaml`: Model hyperparameters

### 2. Run the Pipeline

#### Training Mode
```bash
# Run the complete pipeline
python main.py

# Or run individual components
python -m src.textSummarizer.pipeline.data_ingestion
python -m src.textSummarizer.pipeline.data_transformation
python -m src.textSummarizer.pipeline.model_trainer
python -m src.textSummarizer.pipeline.model_evaluation
```

#### Inference Mode
Start the FastAPI server:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Using the API

#### Interactive Documentation
Access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

#### Example API Requests

**Summarize Text**
```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: text/plain' \
  -d 'The quick brown fox jumps over the lazy dog. This is a test sentence to demonstrate the summarization API.'
```

**Batch Processing**
```bash
curl -X 'POST' \
  'http://localhost:8000/batch_predict' \
  -H 'Content-Type: application/json' \
  -d '{
    "texts": [
      "First document to summarize...",
      "Second document to summarize..."
    ]
  }'
```

## 🧪 Testing

Run the test suite:
```bash
pytest tests/
```

Run with coverage:
```bash
pytest --cov=src tests/
```

## 🐳 Docker Deployment

### Build the Image
```bash
docker build -t text-summarization .
```

### Run the Container
```bash
docker run -d \
  --name text-summarization \
  -p 8000:8000 \
  --gpus all \  # If using GPU
  -v $(pwd)/artifacts:/app/artifacts \
  text-summarization
```

### Using Docker Compose
```bash
docker-compose up -d
```

## 🏗️ Project Structure

```
text_summarisation/
├── artifacts/                     # Stores all pipeline artifacts
│   ├── data_ingestion/           # Raw and processed datasets
│   ├── data_transformation/      # Transformed and tokenized data
│   ├── model_trainer/            # Saved model checkpoints
│   └── model_evaluation/         # Evaluation metrics and results
│
├── config/                       # Configuration files
│   ├── config.yaml              # Main configuration
│   ├── params.yaml              # Hyperparameters
│   └── logging.yaml             # Logging configuration
│
├── src/                          # Source code
│   └── textSummarizer/
│       ├── components/           # Pipeline components
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │   └── model_evaluation.py
│       │
│       ├── config/               # Configuration management
│       │   ├── configuration.py
│       │   └── logging_config.py
│       │
│       ├── entity/               # Data classes
│       ├── logging/              # Logging setup
│       ├── pipeline/             # Pipeline orchestration
│       └── utils/                # Helper functions
│
├── tests/                        # Test suite
│   ├── unit/
│   └── integration/
│
├── .github/workflows/            # CI/CD workflows
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## 📚 Model Details

### PEGASUS Architecture
- **Model**: PEGASUS (Pre-training with Extracted Gap-sentences for Abstractive Summarization)
- **Base Model**: [google/pegasus-large](https://huggingface.co/google/pegasus-large)
- **Fine-tuned On**: SAMSum dataset (conversation summarization)
- **Max Input Length**: 1024 tokens
- **Max Output Length**: 128 tokens

### Performance Metrics
| Metric | Score |
|--------|-------|
| ROUGE-1 | 0.45  |
| ROUGE-2 | 0.22  |
| ROUGE-L | 0.35  |
| BLEU    | 0.28  |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use type hints for better code clarity
- Document all public functions and classes
- Write unit tests for new features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Google Research](https://github.com/google-research/pegasus)
- [SAMSum Dataset](https://arxiv.org/abs/1911.12237)
- [FastAPI](https://fastapi.tiangolo.com/)

## 📧 Contact

For questions or feedback, please open an issue or contact Harsh Goyal at harshgoyal2004@gmail.com
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
