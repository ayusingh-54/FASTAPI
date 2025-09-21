# Insurance Premium Prediction API

A FastAPI-based machine learning API that predicts insurance premium categories based on user demographics, health metrics, and lifestyle factors.

## 🚀 Features

- **Real-time Predictions**: Get instant insurance premium category predictions
- **Data Validation**: Robust input validation using Pydantic models
- **Computed Fields**: Automatic calculation of BMI, age groups, and risk assessments
- **City Tier Classification**: Categorizes cities into Tier 1, 2, or 3 based on metropolitan status
- **Interactive Documentation**: Auto-generated API docs with Swagger UI
- **Health Checks**: Built-in endpoints to monitor API status

## 📋 API Endpoints

### Core Endpoints

- `POST /predict` - Predict insurance premium category
- `GET /` - API status and information
- `GET /health` - Health check endpoint
- `GET /docs` - Interactive API documentation

## 🏗️ Project Structure

```
d:\GEN AI\Fast api\
├── app.py                 # Main FastAPI application
├── model.pkl             # Trained ML model (pickled)
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
└── fastapi-post-api\    # Additional API modules
    ├── main.py          # Patient management system
    └── patients.json    # Patient data storage
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd "d:\GEN AI\Fast api"
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows PowerShell
# or
.venv\Scripts\activate.bat  # Windows CMD
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Server

```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```

## 📊 API Usage

### Prediction Request Example

```json
POST /predict
{
  "age": 35,
  "weight": 75.5,
  "height": 175,
  "income_lpa": 12.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

### Response Example

```json
{
  "predicted_category": "Standard",
  "input_summary": {
    "bmi": 24.65,
    "age_group": "adult",
    "lifestyle_risk": "low",
    "city_tier": 1
  }
}
```

## 🎯 Input Parameters

| Parameter    | Type    | Description            | Validation                 |
| ------------ | ------- | ---------------------- | -------------------------- |
| `age`        | integer | User's age in years    | 1-119                      |
| `weight`     | float   | Weight in kilograms    | > 0                        |
| `height`     | float   | Height in centimeters  | 1-249                      |
| `income_lpa` | float   | Annual income in lakhs | > 0                        |
| `smoker`     | boolean | Smoking status         | true/false                 |
| `city`       | string  | City of residence      | Any valid city             |
| `occupation` | string  | Job category           | See occupation types below |

### Occupation Types

- `private_job`
- `government_job`
- `business_owner`
- `freelancer`
- `student`
- `retired`
- `unemployed`

## 🏙️ City Tier Classification

### Tier 1 Cities (Metropolitan)

Mumbai, Delhi, Bangalore, Chennai, Kolkata, Hyderabad, Pune

### Tier 2 Cities (Major Urban)

50+ cities including Jaipur, Chandigarh, Indore, Lucknow, etc.

### Tier 3 Cities

All other cities not listed in Tier 1 or 2

## 📈 Computed Fields

The API automatically calculates several derived metrics:

### BMI (Body Mass Index)

```python
BMI = weight(kg) / (height(m))²
```

### Age Groups

- **Young**: < 25 years
- **Adult**: 25-44 years
- **Middle-aged**: 45-59 years
- **Senior**: ≥ 60 years

### Lifestyle Risk Assessment

- **High**: Smoker + BMI > 30
- **Medium**: Smoker OR BMI > 27
- **Low**: Non-smoker + BMI ≤ 27

## 🔧 Development

### Running in Development Mode

```bash
uvicorn app:app --reload --log-level debug
```

### Testing the API

1. **Using Browser**: Visit `http://127.0.0.1:8000/docs` for interactive testing
2. **Using curl**:

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "age": 30,
  "weight": 70,
  "height": 175,
  "income_lpa": 8.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}'
```

## 📦 Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Pandas**: Data manipulation and analysis
- **Scikit-learn**: Machine learning model support
- **Uvicorn**: ASGI server for running FastAPI

## 🚨 Error Handling

The API provides detailed error responses:

- **422 Unprocessable Entity**: Invalid input data
- **500 Internal Server Error**: Model prediction errors
- **404 Not Found**: Endpoint not found

## 🔍 Monitoring & Health Checks

### Health Check Endpoint

```bash
GET /health
```

Returns API status and model loading status.

## 📝 Model Information

The API uses a pre-trained machine learning model (`model.pkl`) that predicts insurance premium categories based on:

- Demographic factors (age, location)
- Health metrics (BMI, smoking status)
- Economic factors (income, occupation)
- Geographic factors (city tier)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🐛 Troubleshooting

### Common Issues

1. **Model file not found**

   - Ensure `model.pkl` is in the root directory
   - Check file permissions

2. **Port already in use**

   - Use a different port: `uvicorn app:app --port 8001`
   - Kill existing processes on port 8000

3. **Import errors**
   - Verify virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

## 📞 Support

For issues and questions:

- Create an issue in the repository
- Check the interactive documentation at `/docs`
- Review error logs for detailed debugging information

---

**Built with ❤️ using FastAPI and Machine Learning**
