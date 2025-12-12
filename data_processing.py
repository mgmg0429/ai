import pandas as pd
import numpy as np
from typing import Tuple, List

TARGET_COLUMN = 'Close'

def load_simulated_data(days: int = 365) -> pd.DataFrame:
    """
    Generates simulated stock price data for testing.
    """
    dates = pd.date_range(start='2023-01-01', periods=days, freq='B')
    
    # Random walk simulation
    np.random.seed(42)
    start_price = 10000
    returns = np.random.normal(0, 0.02, days)
    prices = start_price * (1 + returns).cumprod()
    
    # Create DataFrame (OHLCV simulation)
    data = pd.DataFrame(index=dates)
    data['Close'] = prices
    data['Open'] = prices * (1 + np.random.normal(0, 0.005, days))
    data['High'] = data[['Open', 'Close']].max(axis=1) * (1 + np.random.uniform(0, 0.01, days))
    data['Low'] = data[['Open', 'Close']].min(axis=1) * (1 - np.random.uniform(0, 0.01, days))
    data['Volume'] = np.random.randint(1000, 100000, days)
    
    return data

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the data (handling missing values, etc.).
    """
    return df.dropna().copy()

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds technical indicators as features.
    """
    df = df.copy()
    
    # Simple Moving Averages
    df['SMA_5'] = df['Close'].rolling(window=5).mean()
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    
    # Daily Returns
    df['Return'] = df['Close'].pct_change()
    
    # Volatility
    df['Volatility'] = df['Return'].rolling(window=5).std()
    
    return df.dropna()

def preprocess_for_ml(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Prepares features (X) and target (y) for machine learning.
    Target: Next day's Close price.
    """
    df = df.copy()
    
    # Shift Close to create target (Next day Close)
    df['Target'] = df['Close'].shift(-1)
    
    df = df.dropna()
    
    feature_cols = ['Open', 'High', 'Low', 'Close', 'Volume', 'SMA_5', 'SMA_20', 'Return', 'Volatility']
    X = df[feature_cols]
    y = df['Target']
    
    return X, y
