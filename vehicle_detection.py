import cv2
import numpy as np


# Load YOLO model once
net = cv2.dnn.readNet(
    "models/yolov3.weights",
    "models/yolov3.cfg"
)

# Load COCO classes
with open("models/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Vehicle classes only
vehicle_classes = ["car", "bus", "truck", "motorbike"]

# Get output layers
layer_names = net.getLayerNames()
output_layers = [
    layer_names[i - 1]
    for i in net.getUnconnectedOutLayers()
]


def run_detection(video_source):
    cap = cv2.VideoCapture(video_source)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        height, width, _ = frame.shape

        blob = cv2.dnn.blobFromImage(
            frame,
            0.00392,
            (416, 416),
            (0, 0, 0),
            True,
            crop=False
        )

        net.setInput(blob)
        outs = net.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:
                    label = classes[class_id]

                    if label in vehicle_classes:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)

                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(
            boxes,
            confidences,
            0.5,
            0.4
        )

        vehicle_count = len(indexes)

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = classes[class_ids[i]]
                confidence = confidences[i]

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    f"{label} {round(confidence, 2)}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

        # Traffic analytics
        cv2.putText(
            frame,
            f"Vehicles Detected: {vehicle_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        # Return frame to Streamlit
        yield frame

    cap.release()


# Local testing mode (optional)
if __name__ == "__main__":
    for frame in run_detection("demo/traffic.mp4"):
        cv2.imshow(
            "Intelligent Vehicle Vision System",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()