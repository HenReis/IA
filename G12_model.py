import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.metrics import f1_score


class ThresholdClassifier(BaseEstimator, ClassifierMixin):
    """
    Wrapper portável que aplica um threshold personalizado a predict_proba().
    Substitui TunedThresholdClassifierCV sem depender de scikit-learn >= 1.5.

    Para carregar o pkl:
        import pickle
        from G12_model import ThresholdClassifier   # G12_model.py no mesmo directório
        clf = pickle.load(open('G12_pipeline_classification.pkl', 'rb'))
        preds = clf.predict(X)
    """

    def __init__(self, estimator, threshold=0.5):
        self.estimator = estimator
        self.threshold = threshold
        self.best_threshold_ = threshold

    def fit(self, X, y):
        self.estimator.fit(X, y)
        return self

    def predict_proba(self, X):
        return self.estimator.predict_proba(X)

    def predict(self, X):
        proba = self.predict_proba(X)[:, 1]
        return (proba >= self.best_threshold_).astype(int)

    def score(self, X, y):
        return f1_score(y, self.predict(X))
