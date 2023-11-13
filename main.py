import streamlit as st
from streamlit_webrtc import VideoProcessorBase, webrtc_streamer, WebRtcMode, ClientSettings
from turn import get_ice_servers
import av

st.set_page_config(
    page_title="push up counter",
    page_icon=":shark:",
    initial_sidebar_state="collapsed",
    layout="wide",
    menu_items={
        'Get Help': 'https://wa.me/6285536956301',
        'Report a bug': "https://wa.me/6285536956301"
    }
)

class coba(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        image = frame.to_ndarray(format="bgr24")
        # image = cv.
        # cv2.putText(image, f"ANDA TIDAK TERDETEKSI!", (20, 260), cv2.FONT_HERSHEY_DUPLEX, 1.5, (0, 0, 255), 4, cv2.LINE_4)
        return av.VideoFrame.from_ndarray(image, format="bgr24")

def main():
    def processor_factory():
        return coba()

    webrtc_ctx = webrtc_streamer(
        key="tokyo2020-Pictogram",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration={"iceServers": get_ice_servers()},
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=processor_factory,
    )
if __name__ == "__main__":
    main()

