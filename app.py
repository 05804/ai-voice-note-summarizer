import streamlit as st
import tempfile
import assemblyai as aai
from openai import OpenAI

st.title("🎙️ AI Voice Note Summarizer")

import assemblyai as aai

aai.settings.api_key = "c72b7736e77e4a60b0d08f4f39b7725b"

from openai import OpenAI

client = OpenAI(api_key="c72b7736e77e4a60b0d08f4f39b7725b")


audio_file = st.file_uploader(
    "Upload a voice note",
    type=["wav", "mp3", "m4a"]
)

if audio_file:
    st.success("Audio uploaded successfully!")
    st.audio(audio_file)

    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        temp_audio.write(audio_file.read())
        audio_path = temp_audio.name

    if st.button("▶ Transcribe Audio"):
        st.info("Transcribing with AI... ⏳")

        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_path)

        st.subheader("📝 Transcript")
        st.write(transcript.text)

        if st.button("✨ Generate AI Summary"):
            st.info("Generating summary... 🤖")

            prompt = f"""
            From the following voice note transcript:

            1. List key points
            2. List action items

            Transcript:
            {transcript.text}
            """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3
            )

            st.subheader("📌 AI Summary")
            st.write(response.choices[0].message.content)









