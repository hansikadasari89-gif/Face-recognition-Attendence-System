import os
import pandas as pd
import pickle

def check_dirs():
    os.makedirs('core', exist_ok=True)
    os.makedirs('gui', exist_ok=True)
    os.makedirs('dataset', exist_ok=True)
    
    # Initialize basic files if they don't exist
    if not os.path.exists('students.csv'):
        df = pd.DataFrame(columns=['Roll_No', 'Name', 'Image_Path', 'Last_Attendance'])
        df.to_csv('students.csv', index=False)
        
    if not os.path.exists('attendance_log.csv'):
        df = pd.DataFrame(columns=['Date', 'Time', 'Roll_No', 'Name', 'Status'])
        df.to_csv('attendance_log.csv', index=False)
        
    if not os.path.exists('encodings.pickle'):
        with open('encodings.pickle', 'wb') as f:
            pickle.dump([], f)

if __name__ == "__main__":
    check_dirs()
    # Ensure the directories actually exist when running
    from gui.app import App
    app = App()
    app.mainloop()
