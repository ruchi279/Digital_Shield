import librosa
import numpy as np

class AudioVoiceAnalyzer:
    @staticmethod
    def analyze_spoof(file_path: str) -> dict:
        try:
            # Load audio file 
            y, sr = librosa.load(file_path, duration=5)
            
            spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
            zcr = librosa.feature.zero_crossing_rate(y)[0]
            
            centroid_variance = float(np.var(spectral_centroids))
            zcr_mean = float(np.mean(zcr))
            
            is_synthetic = "Suspicious (High/Uniform Variance)" if centroid_variance < 50000 else "Natural Signature"
            
            return {
                "status": "Success",
                "spectral_variance": round(centroid_variance, 2),
                "zero_crossing_mean": round(zcr_mean, 4),
                "voice_signature": is_synthetic
            }
        except Exception as e:
            return {"status": "Error", "message": str(e)}