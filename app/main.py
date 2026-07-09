from fastapi import FastAPI, UploadFile, File, Form
from pydantic import BaseModel
from app.detector import ScamScriptDetector
from app.audio_check import AudioVoiceAnalyzer
import os

app = FastAPI(title="Digital Public Safety Shield API")
detector = ScamScriptDetector()

class TextPayload(BaseModel):
    transcript: str

@app.post("/api/analyze-text")
async def analyze_text(payload: TextPayload):
    result = detector.analyze_transcript(payload.transcript)
    return result

@app.post("/api/analyze-call")
async def analyze_call(transcript: str = Form(...), file: UploadFile = File(...)):
    # Save file temporarily for verification
    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
        
    text_analysis = detector.analyze_transcript(transcript)
    audio_analysis = AudioVoiceAnalyzer.analyze_spoof(temp_path)
    
    # Cleanup
    if os.path.exists(temp_path):
        os.remove(temp_path)
        
    return {
        "text_intelligence": text_analysis,
        "audio_intelligence": audio_analysis,
        "unified_risk_score": max(text_analysis["risk_score"], 85 if audio_analysis.get("voice_signature") != "Natural Signature" else 0)
    }