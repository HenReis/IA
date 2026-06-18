"""
ThresholdClassifier — Group12 helper module.

Wraps a sklearn pipeline and applies a custom decision threshold
to predict(), so the exported pickle correctly uses the tuned threshold
without requiring any manual post-processing.
"""


class ThresholdClassifier:
    """Sklearn-compatible wrapper applying a custom decision threshold to predict()."""

    def __init__(self, pipeline, threshold=0.5):
        self.pipeline  = pipeline
        self.threshold = threshold

    def predict(self, X):
        import numpy as np
        proba = self.pipeline.predict_proba(X)[:, 1]
        return (proba >= self.threshold).astype(int)

    def predict_proba(self, X):
        return self.pipeline.predict_proba(X)
