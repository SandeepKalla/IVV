# Intelligent Vehicle Vision & Traffic Analytics System

An AI-powered real-time traffic intelligence platform built using **YOLO**, **OpenCV**, and **Streamlit** for vehicle detection, traffic analytics, and smart transportation monitoring.

This project evolved from a basic object detection prototype into a scalable computer vision system focused on intelligent traffic analysis and autonomous mobility applications.

---

#  Features

## Real-Time Vehicle Detection

* Detects:

  * Cars
  * Trucks
  * Buses
  * Motorbikes
* Uses YOLO-based deep learning inference.

## Upload Custom Traffic Videos

* Upload any road or traffic video directly through the Streamlit web interface.
* No webcam dependency required.

## Interactive Web Dashboard

* Built using Streamlit.
* Modern dark-themed UI.
* Simple and responsive workflow.

## Traffic Analytics

* Real-time vehicle counting.
* Bounding box visualization.
* Confidence score display.
* Frame-by-frame traffic analysis.

## Modular Architecture

Project structured for future upgrades including:

* Vehicle tracking
* Traffic density estimation
* License plate recognition
* Violation detection
* Smart city analytics

---

# Tech Stack

## AI / Computer Vision

* Python
* OpenCV
* YOLOv3
* NumPy

## Web Interface

* Streamlit

## Future Planned Stack

* YOLOv8
* DeepSORT
* EasyOCR
* FastAPI
* PostgreSQL
* Docker

---

# 📸 Demo Preview

![Screenshot](https://github.com/SandeepKalla/object-detection/blob/main/Sample.png?raw=true)

---

# 📂 Project Structure

```bash
object-detection/
│
├── app.py
├── vehicle_detection.py
├── traffic_analytics.py
├── number_plate_ocr.py
├── requirements.txt
├── README.md
│
├── demo/
│   └── traffic.mp4
│
├── models/
│   ├── yolov3.cfg
│   └── coco.names
│
└── Sample.png
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/SandeepKalla/object-detection.git
cd object-detection
```

---

## 2️⃣ Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ⬇️ Download YOLO Weights

Due to GitHub file size limitations, the YOLO weights file is not included in the repository.

Download:

* [YOLOv3 Weights](https://pjreddie.com/media/files/yolov3.weights)

Then place:

```bash
yolov3.weights
```

inside:

```bash
models/
```

---

# ▶️ Running the Application

Launch the Streamlit dashboard:

```bash
streamlit run app.py
```

Then open:

```bash
http://localhost:8501
```

---

# How It Works

## Step 1

Upload a traffic video.

## Step 2

Frames are processed using YOLO object detection.

## Step 3

Vehicles are identified and classified.

## Step 4

Bounding boxes and analytics are rendered live.

---

# 🔍 Current Capabilities

* Vehicle Detection
* Vehicle Counting
* Confidence Visualization
* Video Processing
* Upload-Based Workflow

---

# 🧩 Planned Upgrades

## 🚧 Next Development Phases

### Phase 1 — UI & Dashboard Enhancements

* Analytics cards
* Traffic charts
* Density indicators
* FPS monitoring

### Phase 2 — Multi-Object Tracking

* DeepSORT integration
* Unique vehicle IDs
* Vehicle trajectory tracking

### Phase 3 — License Plate Recognition

* OCR integration
* Vehicle registry logging
* Searchable plate database

### Phase 4 — Traffic Violation Detection

* Wrong-side driving
* Red-light violation
* Illegal parking detection
* Speed estimation

### Phase 5 — Smart City Analytics

* Congestion prediction
* Traffic flow analysis
* Peak-hour analytics

---

# 🎯 Project Goals

This project is being developed as a production-style intelligent transportation system capable of supporting:

* Autonomous mobility research
* Smart traffic systems
* AI-based surveillance
* Urban traffic analytics
* Edge AI transportation solutions

---

# 🧪 Example Applications

* Smart Cities
* Traffic Monitoring
* Autonomous Transportation
* Urban Planning
* AI Surveillance Systems
* Intelligent Mobility Research

---

# 📌 Author

## Sandeep Kalla

AI & Autonomous Systems Engineering
Computer Vision • Robotics • Intelligent Systems • Software Engineering

GitHub:

```bash
https://github.com/SandeepKalla
```

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

* YOLO — You Only Look Once
* OpenCV
* Streamlit
* COCO Dataset
* Ultralytics AI Community
