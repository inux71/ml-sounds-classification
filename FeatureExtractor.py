import librosa
import numpy as np


class FeatureExtractor:
    @staticmethod
    def root_mean_square(signal: np.array, frame_size: int, hop_size: int) -> np.array:
        return librosa.feature.rms(y=signal, frame_length=frame_size, hop_length=hop_size)
