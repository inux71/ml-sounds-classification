import numpy as np

class FeatureExtractor:
    @staticmethod
    def amplitude_envelope(signal: np.ndarray, frame_size: int, hop_length: int) -> np.array:
        ae = []
        for i in range(0, len(signal), hop_length):
            ae.append(max(signal[i:i + frame_size]))
        return np.array(ae)