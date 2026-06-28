# AI Face Recognition Attendance System

An advanced face recognition attendance system with a modern light theme UI.

## Features
- Real-time face detection and recognition.
- Attendance logging in CSV and Database.
- Modern GUI using `customtkinter`.
- Anti-spoofing and secure face detection.
- Student management dashboard.

## Prerequisites
- **Python 3.10 or 3.11** (Highly Recommended).
- **C++ Build Tools**: Required for `dlib` and `face_recognition`. If installation fails, download "Build Tools for Visual Studio" and select "Desktop development with C++".
- Webcam for face detection.

## Quick Start (Automatic)
For Windows users, we've provided a script to handle everything automatically:

1.  Extract the ZIP folder.
2.  Double-click `setup_and_run.bat`.
3.  The script will:
    - Check your Python version.
    - Create a virtual environment.
    - Install all required libraries with specific versions.
    - Launch the application.

## Troubleshooting
- **Python Version Error**: If the script says your Python version is too old or too new, please install Python 3.10.11 from the official website.
- **dlib/face_recognition Installation Failure**: This usually means you are missing "Desktop development with C++" in Visual Studio Build Tools.
- **Camera Not Found**: Ensure no other app is using your webcam.

## Manual Setup
If you prefer to set it up manually:

1.  Open a terminal in the project folder.
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate it:
    - Windows: `venv\Scripts\activate`
    - Linux/Mac: `source venv/bin/activate`
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Run the project:
    ```bash
    python main.py
    ```

## Project Structure
- `main.py`: Entry point of the application.
- `gui/`: UI components and styles.
- `core/`: Core logic for face recognition.
- `dataset/`: Training data for faces.
- `students.csv`: List of registered students.
- `attendance_log.csv`: Daily attendance logs.
- `attendance.db`: SQLite database for persistent records.

## Sharing Instructions
To send this project to your team:
1.  **Delete** the `venv` folder and `__pycache__` folders if they exist (to keep the zip small).
2.  Zip the entire project folder.
3.  Send the ZIP to your team!
