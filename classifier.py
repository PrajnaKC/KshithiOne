import importlib.util

from PIL import Image
import numpy as np


class SatelliteImageClassification:
    """Lightweight wrapper for loading and running the CNN model.

    This keeps imports optional so the app can still run in fallback mode
    when TensorFlow is not installed.
    """

    def __init__(self):
        self.model = None
        self._tf = None

    def _get_tf(self):
        if self._tf is not None:
            return self._tf
        tf_spec = importlib.util.find_spec("tensorflow")
        if tf_spec is None:
            return None
        import tensorflow as tf  # noqa: WPS433

        self._tf = tf
        return tf

    def load_model_SIC(self, model_path: str) -> None:
        tf = self._get_tf()
        if tf is None:
            raise RuntimeError("TensorFlow is not available")
        self.model = tf.keras.models.load_model(model_path)

    def load_image(self, image_path: str, target_size=(64, 64)):
        """Load an image and return a batch tensor suitable for prediction."""
        image = Image.open(image_path).convert("RGB")
        image = image.resize(target_size)
        image_array = np.array(image, dtype=np.float32) / 255.0
        return np.expand_dims(image_array, axis=0)
