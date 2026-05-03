import streamlit as st
import tempfile
from vehicle_detection import run_detection

st.title("🚗 Intelligent Vehicle Vision System")

uploaded_file = st.file_uploader(
    "Upload a vehicle video",
    type=["mp4", "avi", "mov"]
)

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    st.success("Video uploaded!")

    if st.button("Run Detection"):
        stframe = st.empty()

        for frame in run_detection(tfile.name):
            stframe.image(frame, channels="BGR")