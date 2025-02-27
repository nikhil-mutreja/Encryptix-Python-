import cv2
import numpy as np
import face_recognition
import sqlite3
import pickle
import pyttsx3
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
from PIL import Image, ImageTk
from datetime import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', 'english+f3')

# Database setup
def initialize_db():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT,
            emp_id TEXT UNIQUE,
            face_encoding BLOB
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_id TEXT,
            name TEXT,
            login_time TEXT
        )
    """)
    conn.commit()
    conn.close()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to register an employee
def register_employee():
    name = simpledialog.askstring("Input", "Enter Employee Name")
    emp_id = simpledialog.askstring("Input", "Enter Employee ID")
    image_path = filedialog.askopenfilename(title="Select Image")
    
    if not name or not emp_id or not image_path:
        messagebox.showerror("Error", "All fields are required!")
        return

    img = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(img)
    
    if not face_encodings:
        messagebox.showerror("Error", "No face detected. Try another image.")
        return
    
    face_encoding = face_encodings[0]
    encoding_blob = pickle.dumps(face_encoding)
    
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, emp_id, face_encoding) VALUES (?, ?, ?)", 
                   (name, emp_id, encoding_blob))
    conn.commit()
    conn.close()
    
    messagebox.showinfo("Success", f"Employee {name} registered successfully!")
    speak(f"Employee {name} has been registered successfully!")

# Function to recognize employees and log attendance
def recognize_employee():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cap = cv2.VideoCapture(0)
    messagebox.showinfo("Recognition", "Starting real-time recognition...")
    
    known_encodings, known_names, known_ids = [], [], []
    cursor.execute("SELECT name, emp_id, face_encoding FROM employees")
    for name, emp_id, encoding_blob in cursor.fetchall():
        known_encodings.append(pickle.loads(encoding_blob))
        known_names.append(name)
        known_ids.append(emp_id)

    while True:
        ret, frame = cap.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name, emp_id = "Unknown", None
            
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            
            if matches[best_match_index]:
                name, emp_id = known_names[best_match_index], known_ids[best_match_index]
                cursor.execute("INSERT INTO attendance (emp_id, name, login_time) VALUES (?, ?, ?)",
                               (emp_id, name, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                conn.commit()
                speak(f"{name}, your attendance has been marked!")
                
            top, right, bottom, left = [x * 4 for x in face_location]
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    conn.close()

# Admin login to view attendance records
def admin_login():
    password = simpledialog.askstring("Admin Login", "Enter Admin Password", show='*')
    if password == "admin123":
        view_attendance()
    else:
        messagebox.showerror("Error", "Incorrect Password!")

# View attendance records
def view_attendance():
    conn = sqlite3.connect("attendance.db")
    cursor = conn.cursor()
    cursor.execute("SELECT emp_id, name, login_time FROM attendance")
    records = cursor.fetchall()
    conn.close()
    
    record_text = "\n".join([f"{emp_id} - {name} - {time}" for emp_id, name, time in records])
    messagebox.showinfo("Attendance Records", record_text if record_text else "No attendance records found!")

# GUI Setup
def main_gui():
    root = tk.Tk()
    root.title("Employee Face Recognition System")
    root.geometry("500x400")
    root.configure(bg="black")

    tk.Label(root, text="Face Recognition System", font=("Arial", 14, "bold"), fg="white", bg="black").pack(pady=10)

    btn_style = {"font": ("Arial", 12), "fg": "white", "width": 20, "height": 2}
    
    tk.Button(root, text="Register Employee", command=register_employee, bg="blue", **btn_style).pack(pady=10)
    tk.Button(root, text="Start Recognition", command=recognize_employee, bg="green", **btn_style).pack(pady=10)
    tk.Button(root, text="Admin Login", command=admin_login, bg="purple", **btn_style).pack(pady=10)
    tk.Button(root, text="Exit", command=root.quit, bg="red", **btn_style).pack(pady=10)
    
    root.mainloop()

# Initialize database
initialize_db()

# Run GUI
if __name__ == "__main__":
    main_gui()
