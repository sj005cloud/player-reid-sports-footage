# Player Re-Identification in Sports Footage

This project performs player detection, tracking, and re-identification in a single broadcast video using **YOLOv11** and **Deep SORT**.  
It includes enhancements like **goalkeeper highlighting**, **player count overlay**, and a **mini-map** showing player positions.

---

##  Project Structure

```
player_reid_project/
├── reid_tracker.py            # Main tracking script
├── yolo11s.pt                 # YOLOv11 model weights
├── videos/
│   └── 15sec_input_720p.mp4   # Input video
├── output/
│   └── output_with_ids.mp4    # Output video with tracked IDs
└── README.md
```

> `yolo11s.pt` is automatically downloaded if missing.  
> Input `.mp4` video must be placed inside the `videos/` folder.

---

##  Setup Instructions

### Step 1: Open the project folder

Make sure your folder structure matches the layout shown above.  
Open your command prompt or terminal and navigate to the project folder:

```bash
cd "C:\Users\saraj\OneDrive\Desktop\player_reid_project"
```

---

### Step 2: Create a virtual environment and install dependencies

```bash
# Create virtual environment (only once)
python -m venv venv

# Activate the environment
venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

If `requirements.txt` is not available, install packages manually:

```bash
pip install ultralytics==8.0.20
pip install deep_sort_realtime
pip install opencv-python
pip install numpy
```

---

### Step 3: Run the project

```bash
python reid_tracker.py
```

The output video will be saved at:

```
output/output_with_ids.mp4
```

▶️ **Watch the processed output video:**  
[Google Drive Link]( https://drive.google.com/file/d/1zzPVAhVy7-cfqiU__8NwRQRoW5U8HZTO/view?usp=sharing)

---

##  Dependencies and Environment

- **Python Version:** 3.8 or higher

| Package              | Purpose                         |
|----------------------|----------------------------------|
| ultralytics==8.0.20  | YOLOv11 object detection         |
| deep_sort_realtime   | Tracking & re-identification     |
| opencv-python        | Video and image processing       |
| numpy                | Matrix & numerical computations  |

---

##  Notes

- **Goalkeeper Highlighting**  
  Controlled using the constant `GOALKEEPER_ID = 79` in the script.

- **Mini-map Overlay**  
  Shows real-time player positions on a football pitch (bottom-right corner).

- **Offline Functionality**  
  The script works fully offline once the model and video are downloaded.
