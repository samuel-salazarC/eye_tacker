# Eye Tracker Heatmap

A Python-based eye tracking tool that captures gaze data via webcam using [MediaPipe Face Mesh](https://google.github.io/mediapipe/solutions/face_mesh) and generates heatmaps to visualize eye movement across the screen.

![Heatmap Example](docs/example_heatmap.png)

## 🔍 Features

- Real-time webcam eye tracking
- Eye coordinates logged to CSV
- Heatmap generation over a Cartesian plane
- Clean separation of modules: data capture vs. data visualization
- Uses `MediaPipe`, `OpenCV`, `Matplotlib`, `Seaborn` and `Pandas`

## 🧠 Use Cases

- UX & UI research
- Human-computer interaction studies
- Assistive technology exploration
- Psychology & behavior analysis

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone git@github.com:samuel-salazarC/eye_tacker.git
cd eye_tacker

# Create and activate virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the eye tracker
python eye_tracker.py

# Generate a heatmap from the eye tracking data
python heatmap_cartesiano.py
