# Yearly Amount Predictor

A Streamlit web app that predicts the yearly amount spent by a user based on four input features using a trained Linear Regression model.

## Features

- Input fields for:
  - Average Session Length (in mins)
  - Time on App (in hrs)
  - Time on Website (in hrs)
  - Length of Membership (in years)
- Predicts yearly amount spent using a pre-trained model (`model.pkl`)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/yearly-amount-predictor.git
cd yearly-amount-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your trained model

Place your `model.pkl` file in the root directory of the project.

### 4. Run the app locally

```bash
streamlit run app.py
```

### 5. Deploy to Streamlit Cloud

1. Push your code (including `app.py`, `model.pkl`, and `requirements.txt`) to your GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your GitHub repo.
3. Follow the instructions to deploy.

## Files

- `app.py` - Streamlit frontend and prediction logic
- `model.pkl` - Pre-trained Linear Regression model
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## Troubleshooting

- If you see `ModuleNotFoundError`, make sure you installed all dependencies.
- If you see `FileNotFoundError: model.pkl`, ensure `model.pkl` is in the same folder as `app.py`.
- For deployment, make sure all files are committed to your GitHub repo.

## License

MIT License
