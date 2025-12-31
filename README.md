# YOLO Car Tracking

This project implements real-time vehicle tracking and counting using YOLOv8 (You Only Look Once) object detection model. It processes a video file to detect, track, and count vehicles (cars, trucks, buses, motorcycles, bicycles) crossing a defined line.

## Features

- **Object Detection**: Uses YOLOv8 nano model for efficient detection.
- **Tracking**: Employs ByteTrack for persistent object tracking across frames.
- **Counting**: Counts unique vehicles crossing a vertical line at the center of the frame.
- **Visualization**: Draws bounding boxes, IDs, counting line, and live counts on the video.
- **Output**: Saves the processed video to `output.mp4`.

## Requirements

- Python 3.7+
- ultralytics
- opencv-python
- numpy

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/BerkeTozkoparam/yolo-car-tracking.git
   cd yolo-car-tracking
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install ultralytics opencv-python numpy
   ```

4. Ensure `yolov8n.pt` is in the directory (included in repo).

## Usage

1. Place your input video as `IMG_5268.MOV` in the directory (or modify the code for a different file).
2. Run the script:
   ```
   python main_car.py
   ```
3. The processed video will be saved as `output.mp4`.
4. Press 'q' in the display window to stop early.

## How It Works

- Loads YOLO model and video.
- For each frame:
  - Runs YOLO tracking.
  - Calculates object centers and determines side relative to the counting line.
  - Counts crossings for tracked vehicles.
  - Draws annotations.
- Outputs the annotated video.

## Demo Video

Here's a demo of the vehicle tracking and counting in action:

<video width="640" height="360" controls>
  <source src="output.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## License

This project is open-source. Feel free to modify and use.

## Contributing

Pull requests are welcome!</content>
<parameter name="filePath">/Users/berkebarantozkoparan/Project13/README.md