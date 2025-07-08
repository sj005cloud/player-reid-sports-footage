Final README.md (Polished for GitHub)
markdown
Copy
Edit
# Player Re-Identification in Sports Footage

This project performs player detection, tracking, and re-identification in a single broadcast video using **YOLOv11** and **Deep SORT**.  
It includes enhancements like **goalkeeper highlighting**, **player count overlay**, and a **mini-map** showing player positions.

---

## Project Structure

player_reid_project/
├── reid_tracker.py # Main tracking script
├── yolo11s.pt # YOLOv11 model weights
├── videos/
│ └── 15sec_input_720p.mp4 # Input video
├── output/
│ └── output_with_ids.mp4 # Output video with tracked IDs
└── README.md

yaml
Copy
Edit

>  `yolo11s.pt` is automatically downloaded if missing.  
>  Input `.mp4` video must be placed inside the `videos/` folder.

---

##  Setup Instructions

### Step 1: Open project folder

Ensure your folder is structured as shown above.  
Open your command prompt or terminal and navigate to the project folder:

```bash
cd "C:\Users\saraj\OneDrive\Desktop\player_reid_project"
Step 2: Create virtual environment and install dependencies (Recommended)
bash
Copy
Edit
# Create virtual environment (once)
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
If requirements.txt is not available, install manually:

bash
Copy
Edit
pip install ultralytics==8.0.20
pip install deep_sort_realtime
pip install opencv-python
pip install numpy
Step 3: Run the project
bash
Copy
Edit
python reid_tracker.py
The output will be saved at:

bash
Copy
Edit
output/output_with_ids.mp4
▶ Watch the output video here:
Google Drive Link

 Dependencies and Environment
Python Version: 3.8 or higher

Required Packages:

Package	Purpose
ultralytics==8.0.20	YOLOv11 object detection
deep_sort_realtime	Tracking & re-identification
opencv-python	Video and image processing
numpy	Matrix & numerical computations

 Notes
Goalkeeper Highlighting:
Manually controlled using the constant GOALKEEPER_ID = 79 in the script.

Mini-map Overlay:
Displays at the bottom-right corner and updates player positions in real time.

The script works fully offline after downloading the model and video once.
