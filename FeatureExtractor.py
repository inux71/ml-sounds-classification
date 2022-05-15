import librosa
import numpy as np


class FeatureExtractor:
    @staticmethod
    def amplitude_envelope(signal: np.ndarray, frame_size: int, hop_length: int) -> np.array:
        ae = []
        for i in range(0, len(signal), hop_length):
            ae.append(max(signal[i:i + frame_size]))
        return np.array(ae)

    @staticmethod
    def root_mean_square(signal: np.ndarray, frame_size: int, hop_size: int) -> np.array:
        return librosa.feature.rms(y=signal, frame_length=frame_size, hop_length=hop_size)

    @staticmethod
    def normalize_feature(feature: np.ndarray) -> float:
        return np.sqrt(np.sum(feature ** 2))
