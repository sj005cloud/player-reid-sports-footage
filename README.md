Player Re-Identification in Sports Footage: 
This project performs player detection, tracking, and re-identification in a single broadcast video using YOLOv11 and Deep SORT. It includes enhancements like goalkeeper highlighting, player count overlay, and a mini-map showing player positions.

Project Structure:
player_reid_project/
├── reid_tracker.py            # Main tracking script
├── yolo11s.pt                 #YOLOv11 model weights
├── videos/
│   └── 15sec_input_720p.mp4   #Input video
├── output/
│   └── output_with_ids.mp4    #Output video with tracked IDs
└── README.md 

yolo11s.pt is automatically downloaded if missing.
Input .mp4 video must be placed inside the videos/ folder.

1. Setup Instructions:

 Step 1: Open project folder
         Ensure your folder is set up as shown above. You can place the project inside OneDrive/Desktop or any local directory.

         Open your command prompt or terminal, navigate to the project folder:
         cd "C:\Users\saraj\OneDrive\Desktop\player_reid_project"

 Step 2: Use a virtual environment setup (highly recommended) and install dependencies
 
         # Create virtual environment (once)
         python -m venv venv
         # activate it
         venv\Scripts\activate
         # Then install dependencies
         pip install -r requirements.txt

         If requirements.txt is not available, install packages manually:

         Inside the virtual environment of the project folder in command prompt:
         Copy code
         pip install ultralytics==8.0.20
         pip install deep_sort_realtime
         pip install opencv-python
         pip install numpy

 Step 3: Run the project
         In the command prompt, run the main script to begin tracking:
         python reid_tracker.py

         The output will be saved at:
         output/output_with_ids.mp4

         The processed video ouput is available at the following link: https://drive.google.com/file/d/1zzPVAhVy7-cfqiU__8NwRQRoW5U8HZTO/view?usp=sharing

2. Dependencies and Environment Requirements:

 Python Version: Python 3.8 or higher
 Required Packages:
 Package              | Purpose                      |
                      |                              |
 ultralytics==8.0.20  | YOLOv11 object detection     |
 deep_sort_realtime   | Tracking & re-identification |
 opencv-python        | Video and image processing   |
 numpy                | Matrix & numerical ops       |


3. Notes:

 The goalkeeper is manually highlighted by setting their ID inside the script: GOALKEEPER_ID = 79

 The mini-map is displayed at the bottom-right and scales with player movement.
 The script works offline after downloading the model and video.