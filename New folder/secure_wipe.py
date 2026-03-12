import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import hashlib
import time

# ---------- Core Functions ----------
def wipe_file(file_path, passes=3, progress_callback=None):
    """Overwrite file with secure multi-pass method (zeros + random) using chunked writes and fsync."""
    try:
        size = os.path.getsize(file_path)
        if size == 0:
            # Handle empty files: still remove them, but log as zero-length
            os.remove(file_path)
            if progress_callback:
                progress_callback(100.0)
            return True

        chunk = 1024 * 1024  # 1 MB
        zeros = b"\x00" * chunk

        with open(file_path, "r+b", buffering=0) as f:
            for p in range(passes):
                f.seek(0)
                written = 0
                while written < size:
                    to_write = min(chunk, size - written)
                    if p % 2 == 0:
                        buf = zeros if to_write == chunk else b"\x00" * to_write
                    else:
                        buf = os.urandom(to_write)
                    f.write(buf)
                    written += to_write
                f.flush()
                os.fsync(f.fileno())
                if progress_callback:
                    progress_callback((p + 1) / passes * 100.0)

        os.remove(file_path)
        return True
    except Exception as e:
        return str(e)

def file_checksum(file_path):
    """Calculate SHA256 checksum of file (before wipe)."""
    sha = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()

# ---------- GUI Callbacks (thread-safe helpers) ----------
def append_log(msg):
    root.after(0, lambda: log_text.insert(tk.END, msg))

def set_progress(value):
    root.after(0, lambda: progress_var.set(value))

def normalized_passes(val):
    try:
        n = int(val)
    except:
        return 3
    return n if n in (1, 3, 7) else 3

# ---------- Wipe Operations ----------
def wipe_single_file(file_path, passes):
    try:
        before = file_checksum(file_path)
    except Exception as e:
        append_log(f"[ERROR] Checksum failed for {file_path}: {e}\n")
        return

    t0 = time.time()
    result = wipe_file(file_path, passes, set_progress)
    dt = time.time() - t0

    if result is True:
        exists = os.path.exists(file_path)
        append_log(f"[SUCCESS] Wiped: {file_path}\n")
        append_log(f"Checksum (pre): {before}\n")
        append_log(f"Passes: {passes}, Time: {dt:.2f}s\n")
        append_log("File no longer exists.\n\n" if not exists else "Warning: file still exists!\n\n")
    else:
        append_log(f"[ERROR] {result}\n")

def wipe_folder(folder_path, passes):
    count = 0
    for root_dir, _, files in os.walk(folder_path):
        for name in files:
            path = os.path.join(root_dir, name)
            try:
                if not os.path.islink(path) and os.path.isfile(path):
                    wipe_single_file(path, passes)
                    count += 1
            except Exception as e:
                append_log(f"[ERROR] {path}: {e}\n")
    append_log(f"[DONE] Wiped {count} files under: {folder_path}\n\n")

# ---------- GUI Event Handlers ----------
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_var.set(file_path)

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        file_var.set(folder_path)

def start_wipe():
    target = file_var.get().strip()
    passes = normalized_passes(pass_var.get())

    if not target or not os.path.exists(target):
        messagebox.showerror("Error", "Select a valid file/folder!")
        return

    log_text.delete("1.0", tk.END)
    progress_var.set(0.0)

    def worker():
        if os.path.isfile(target):
            wipe_single_file(target, passes)
        elif os.path.isdir(target):
            wipe_folder(target, passes)
        else:
            append_log("Invalid path!\n")

    threading.Thread(target=worker, daemon=True).start()

def save_log():
    log_content = log_text.get("1.0", tk.END).strip()
    if not log_content:
        messagebox.showwarning("Warning", "No logs to save!")
        return
    save_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    if save_path:
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(log_content)
        messagebox.showinfo("Saved", f"Logs saved to {save_path}")

# ---------- GUI Setup ----------
root = tk.Tk()
root.title("SIH 2025 - Secure Wipe Prototype")
root.geometry("700x560")

file_var = tk.StringVar()
pass_var = tk.StringVar(value="3")
progress_var = tk.DoubleVar()

# File Selection
tk.Label(root, text="Select File/Folder to Wipe:").pack(pady=(10, 0))
tk.Entry(root, textvariable=file_var, width=70).pack(pady=5)
frame = tk.Frame(root)
frame.pack()
tk.Button(frame, text="Browse File", command=select_file).pack(side=tk.LEFT, padx=5)
tk.Button(frame, text="Browse Folder", command=select_folder).pack(side=tk.LEFT, padx=5)

# Passes
tk.Label(root, text="Number of Passes (1, 3, 7):").pack(pady=5)
tk.Entry(root, textvariable=pass_var, width=8, justify="center").pack()

# Start Button
tk.Button(root, text="Start Wipe", command=start_wipe, bg="red", fg="white").pack(pady=12)

# Progress Bar
ttk.Progressbar(root, variable=progress_var, maximum=100, length=500).pack(pady=10)

# Logs
log_text = tk.Text(root, height=18, width=85)
log_text.pack(pady=5)

# Save Logs
tk.Button(root, text="Save Logs", command=save_log).pack(pady=6)

# Note for SSDs
note = ("Note: On SSDs, complete sanitization typically requires controller commands "
        "like ATA Secure Erase. This prototype demonstrates file-level wiping and "
        "verification within a live OS.")
tk.Label(root, text=note, wraplength=660, fg="#555").pack(pady=(6, 10))

root.mainloop()
