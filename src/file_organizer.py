import os
import shutil
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, ttk
from tkinter import messagebox

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("600x400")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Directory selection
        self.dir_label = ttk.Label(self.main_frame, text="Select Directory:")
        self.dir_label.grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.dir_entry = ttk.Entry(self.main_frame, width=50)
        self.dir_entry.grid(row=1, column=0, padx=5)
        
        self.browse_btn = ttk.Button(self.main_frame, text="Browse", command=self.browse_directory)
        self.browse_btn.grid(row=1, column=1, padx=5)
        
        # Organize button
        self.organize_btn = ttk.Button(self.main_frame, text="Organize Files", command=self.organize_files)
        self.organize_btn.grid(row=2, column=0, columnspan=2, pady=20)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.main_frame, length=400, mode='determinate')
        self.progress.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Status label
        self.status_label = ttk.Label(self.main_frame, text="")
        self.status_label.grid(row=4, column=0, columnspan=2)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        self.dir_entry.delete(0, tk.END)
        self.dir_entry.insert(0, directory)

    def organize_files(self):
        directory = self.dir_entry.get()
        if not directory:
            messagebox.showwarning("Warning", "Please select a directory first!")
            return

        extension_map = {
        # Videos
        '.mp4': 'Videos',
        '.mov': 'Videos',
        '.avi': 'Videos',
        '.mkv': 'Videos',
        '.wmv': 'Videos',
        '.flv': 'Videos',
        '.webm': 'Videos',
        '.mpeg': 'Videos',
        '.3gp': 'Videos',
        
        # Audio
        '.mp3': 'Music',
        '.wav': 'Music',
        '.flac': 'Music',
        '.aac': 'Music',
        '.ogg': 'Music',
        '.wma': 'Music',
        '.m4a': 'Music',
        
        # Images
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.bmp': 'Images',
        '.tiff': 'Images',
        '.svg': 'Images',
        '.webp': 'Images',
        '.ico': 'Images',
        '.heic': 'Images',
        
        # Documents
        '.pdf': 'Documents',
        '.doc': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        '.xlsx': 'Documents',
        '.xls': 'Documents',
        '.ppt': 'Documents',
        '.pptx': 'Documents',
        '.odt': 'Documents',
        '.rtf': 'Documents',
        '.csv': 'Documents',
        '.tex': 'Documents',
        
        # Code Files
        '.py': 'Code',
        '.java': 'Code',
        '.c': 'Code',
        '.cpp': 'Code',
        '.cs': 'Code',
        '.js': 'Code',
        '.html': 'Code',
        '.css': 'Code',
        '.php': 'Code',
        '.sql': 'Code',
        '.sh': 'Code',
        '.json': 'Code',
        '.xml': 'Code',
        '.yaml': 'Code',
        '.yml': 'Code',
        
        # Archives
        '.zip': 'Archives',
        '.rar': 'Archives',
        '.7z': 'Archives',
        '.tar': 'Archives',
        '.gz': 'Archives',
        '.bz2': 'Archives',
        '.xz': 'Archives',
        '.iso': 'Archives',
        
        # Executables
        '.exe': 'Executables',
        '.msi': 'Executables',
        '.dmg': 'Executables',
        '.app': 'Executables',
        '.bat': 'Executables',
        '.sh': 'Executables',
        
        # Design & 3D Models
        '.psd': 'Design',
        '.ai': 'Design',
        '.xd': 'Design',
        '.fig': 'Design',
        '.sketch': 'Design',
        '.dwg': 'Design',
        '.blend': '3D Models',
        '.stl': '3D Models',
        '.fbx': '3D Models',
        '.obj': '3D Models',
        
        # Miscellaneous
        '.torrent': 'Torrents',
        '.log': 'Logs',
        '.dat': 'Data Files',
        '.db': 'Database',
        }


        try:
            files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
            total_files = len(files)
            processed_files = 0

            self.progress['maximum'] = total_files
            
            for filename in files:
                file_path = os.path.join(directory, filename)
                file_extension = os.path.splitext(filename)[1].lower()
                
                if file_extension in extension_map:
                    folder_name = extension_map[file_extension]
                    folder_path = os.path.join(directory, folder_name)
                    
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    
                    shutil.move(file_path, os.path.join(folder_path, filename))
                
                processed_files += 1
                self.progress['value'] = processed_files
                self.status_label['text'] = f"Processing: {processed_files}/{total_files} files"
                self.root.update()

            messagebox.showinfo("Success", "Files organized successfully!")
            self.status_label['text'] = "Complete!"
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()