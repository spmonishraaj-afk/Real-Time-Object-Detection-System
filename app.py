import streamlit as st
import cv2
from ultralytics import YOLO

st.title("Live Object Detection")

model = YOLO("yolo11n.pt")

start = st.button("Start Camera")

if start:

    camera = cv2.VideoCapture(0)

    frame_placeholder = st.empty()

    while True:

        success, frame = camera.read()

        if not success:
            st.write("Camera not found")
            break

        results = model(frame)

        for result in results:

            for box in result.boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                confidence = float(box.conf[0])

                class_id = int(box.cls[0])

                object_name = model.names[class_id]

                if confidence > 0.5:

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

                    text = object_name + " " + str(round(confidence, 2))

                    cv2.putText(
                        frame,
                        text,
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2
                    )

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        frame_placeholder.image(frame)