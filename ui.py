import streamlit as st
import requests

st.set_page_config(page_title="Digital Shield", page_icon="🛡️", layout="centered")

st.title("🛡️ Digital Public Safety Shield")
st.markdown("### Real-Time 'Digital Arrest' & Fraud Detection")
st.markdown("Protecting citizens from coercive psychological manipulation and AI voice spoofing.")
st.divider()

tab1, tab2 = st.tabs(["💬 Text Analysis", "🎙️ Audio/Call Analysis"])

with tab1:
    st.markdown("**Simulate a suspicious text message:**")
    transcript = st.text_area("Transcript Input", height=150, label_visibility="collapsed", placeholder="Paste the suspicious text here...")
    
    if st.button("🚨 Analyze Text Threat", type="primary", use_container_width=True):
        if transcript.strip():
            with st.spinner("Analyzing psychological phases..."):
                try:
                    response = requests.post("http://localhost:8000/api/analyze-text", json={"transcript": transcript})
                    if response.status_code == 200:
                        data = response.json()
                        score = data["risk_score"]
                        st.divider()
                        if score >= 75:
                            st.error(f"**VERDICT:** {data['verdict']} (Risk Score: {score}/100)", icon="🚨")
                        elif score >= 50:
                            st.warning(f"**VERDICT:** {data['verdict']} (Risk Score: {score}/100)", icon="⚠️")
                        else:
                            st.success(f"**VERDICT:** {data['verdict']} (Risk Score: {score}/100)", icon="✅")
                            
                        if data["triggered_phases"]:
                            st.markdown("#### 🔍 Coercive Tactics Detected:")
                            for phase in data["triggered_phases"]:
                                st.markdown(f"- **{phase.capitalize()} Manipulation**: Scammer used terms like {data['evidence'][phase]}")
                except Exception:
                    st.error("⚠️ Connection Error: Is your Docker API running on port 8000?")
        else:
            st.warning("Please paste a transcript first.")

with tab2:
    st.markdown("**Upload a suspicious call recording (tests for AI-generated/spoofed voices) and transcript:**")
    audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])
    audio_transcript = st.text_area("Call Transcript", height=100, placeholder="Paste the transcript of the call here...")
    
    if st.button("🚨 Analyze Call & Audio", type="primary", use_container_width=True):
        if audio_file and audio_transcript.strip():
            with st.spinner("Analyzing audio variance and script mechanics..."):
                try:
                    files = {"file": (audio_file.name, audio_file.getvalue(), audio_file.type)}
                    data = {"transcript": audio_transcript}
                    response = requests.post("http://localhost:8000/api/analyze-call", data=data, files=files)
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.divider()
                        unified_score = result["unified_risk_score"]
                        
                        if unified_score >= 75:
                            st.error(f"**UNIFIED VERDICT: CRITICAL THREAT** (Risk Score: {unified_score}/100)", icon="🚨")
                        else:
                            st.success(f"**UNIFIED VERDICT: LOW RISK** (Risk Score: {unified_score}/100)", icon="✅")
                        
                        st.markdown("#### 🎙️ Voice Intelligence:")
                        st.info(f"**Voice Signature:** {result['audio_intelligence'].get('voice_signature', 'N/A')}")
                        st.caption(f"Spectral Variance: {result['audio_intelligence'].get('spectral_variance', 'N/A')} | Zero Crossing Mean: {result['audio_intelligence'].get('zero_crossing_mean', 'N/A')}")
                        
                        st.markdown("#### 💬 Text Intelligence:")
                        st.write(f"Psychological Risk Score: {result['text_intelligence']['risk_score']}")
                except Exception as e:
                    st.error(f"⚠️ Connection Error: Ensure Docker API is running.")
        else:
            st.warning("Please upload an audio file and provide a transcript.")