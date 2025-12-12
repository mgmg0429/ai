import os
import joblib
import pandas as pd
from django.conf import settings
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from typing import Dict, Any, Optional

from .data_processing import preprocess_for_ml, load_simulated_data, clean_data, feature_engineering

class StockPredictor:
    def __init__(self):
        self.model = LinearRegression()
        # Ensure models directory exists
        self.model_dir = settings.BASE_DIR / 'models' 
        self.model_path = self.model_dir / 'stock_price_predictor.pkl'
        
        if not self.model_dir.exists():
            self.model_dir.mkdir(parents=True, exist_ok=True)

    def train(self, data: Optional[pd.DataFrame] = None) -> Dict[str, float]:
        """
        Trains the model using provided data or simulated data.
        Returns evaluation metrics.
        """
        if data is None:
            # Load simulated data if none provided
            raw_data = load_simulated_data()
            cleaned = clean_data(raw_data)
            data = feature_engineering(cleaned)
            
        X, y = preprocess_for_ml(data)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False, random_state=42
        )
        
        # Train
        self.model.fit(X_train, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        # Save model
        joblib.dump(self.model, self.model_path)
        
        return {
            "mse": mse,
            "r2": r2,
            "samples": len(X)
        }

    def load_model(self) -> bool:
        """Loads the model from disk if available."""
        if self.model_path.exists():
            self.model = joblib.load(self.model_path)
            return True
        return False

    def predict(self, input_data: pd.DataFrame) -> float:
        """
        Predicts the next day's price given the latest data features.
        Expects input_data to be preprocessed features (1 row).
        """
        if not hasattr(self.model, 'coef_'):
            if not self.load_model():
                raise ValueError("Model not trained or loaded.")
        
        return self.model.predict(input_data)[0]
