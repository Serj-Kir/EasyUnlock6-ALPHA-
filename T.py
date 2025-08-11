import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import psutil

def run_sfc():
    """Run the command sfc /scannow."""
    try:
        subprocess.run(["sfc", "/scannow"], check=True)
        messagebox.showinfo("Success", "sfc /scannow command executed successfully.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Error executing the sfc command.")

def unlock_task_manager():
    """Unlock the Task Manager."""
    try:
        # Command to unlock Task Manager
        # Replace with appropriate commands for your specific scenario.
        os.system('REG DELETE "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" /v DisableTaskMgr /f')
        messagebox.showinfo("Success", "Task Manager unlocked.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def restore_mbr():
    """Restore the MBR."""
    try:
        subprocess.run(["bootrec", "/fixmbr"], check=True)
        messagebox.showinfo("Success", "MBR restored successfully.")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Error restoring the MBR.")

def open_task_manager():
    """Open a built-in task manager."""
    root_task_manager = tk.Tk()
    root_task_manager.title("Built-in Task Manager")

    def list_processes():
        """List all running processes."""
        for proc in psutil.process_iter(['pid', 'name']):
            process_list.insert(tk.END, f"{proc.info['pid']}: {proc.info['name']}")

    def kill_process():
        """Terminate the selected process."""
        selected_process = process_list.curselection()
        if selected_process:
            pid = int(process_list.get(selected_process).split(':')[0])
            try:
                psutil.Process(pid).terminate()
                messagebox.showinfo("Success", f"Process {pid} terminated.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    frame = tk.Frame(root_task_manager)
    frame.pack(pady=10)

    process_list = tk.Listbox(frame, width=50, height=15)
    process_list.pack(side=tk.LEFT)

    list_processes_button = tk.Button(frame, text="Load Processes", command=list_processes)
    list_processes_button.pack(side=tk.TOP)

    kill_button = tk.Button(frame, text="Terminate Process", command=kill_process)
    kill_button.pack(side=tk.BOTTOM)

    root_task_manager.mainloop()

# Main interface
root = tk.Tk()
root.title("EasyUnlock6")

sfc_button = tk.Button(root, text="Run sfc /scannow", command=run_sfc)
sfc_button.pack(pady=10)

unlock_button = tk.Button(root, text="Unlock Task Manager", command=unlock_task_manager)
unlock_button.pack(pady=10)

restore_button = tk.Button(root, text="Restore MBR", command=restore_mbr)
restore_button.pack(pady=10)

task_manager_button = tk.Button(root, text="Open Built-in Task Manager", command=open_task_manager)
task_manager_button.pack(pady=10)

root.mainloop()