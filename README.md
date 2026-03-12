Secure Data Wiping for Trustworthy IT Asset Recycling
Overview

Secure Data Wiping for Trustworthy IT Asset Recycling is a Python-based tool designed to permanently delete sensitive files before recycling or disposing of storage devices. Many users hesitate to recycle devices because deleted files can often be recovered using forensic tools.

This project demonstrates a secure multi-pass file overwriting technique along with checksum verification and a graphical interface to ensure safe and trustworthy data removal.

Objectives

Ensure permanent deletion of sensitive data

Prevent data recovery and breaches

Increase trust in IT asset recycling

Provide verification logs for wiped files

Features
Multi-Pass Secure Wiping

Files are overwritten multiple times before deletion using zero patterns and random data.

Supported passes:

1 Pass – Quick wipe

3 Passes – Standard secure wipe

7 Passes – High security wipe

File Integrity Verification

Before wiping, the system generates a SHA-256 checksum of the file to record its original state.

Folder Wiping

The tool can securely wipe:

Individual files

Entire folders recursively

Progress Monitoring

A progress bar displays the wiping progress in real time.

Log Generation

The system logs:

File name

Checksum

Number of wiping passes

Time taken

Wiping status

Logs can be saved for verification and auditing.

Project Structure
secure-data-wiping/
│
├── create_dummy_file.py
├── secure_wipe_gui.py
└── README.md
Test File Generator
create_dummy_file.py

This script creates a dummy text file with generated data for testing the wiping system.

Example:

python create_dummy_file.py

Output:

Dummy file 'TopSecret.txt' created (10 KB)
Secure Wiping Application
secure_wipe_gui.py

This is the main graphical application used to securely wipe files.

Process:

User selects a file or folder.

The system generates a SHA-256 checksum.

The file is overwritten multiple times.

The file is permanently deleted.

The system records wiping logs.

Technologies Used
Technology	Purpose
Python	Core programming
Tkinter	Graphical user interface
hashlib	SHA-256 checksum
threading	Background execution
os	File system operations
Workflow

User selects a file or folder.

System calculates the file checksum.

Secure overwrite algorithm runs for selected passes.

File is overwritten with secure patterns.

File is permanently deleted.

Wiping log is generated.

How to Run the Project
Step 1 – Install Python

Install Python 3.x on your system.

Step 2 – Generate a Test File
python create_dummy_file.py
Step 3 – Run Secure Wipe Tool
python secure_wipe_gui.py
Important Note

For Solid State Drives (SSDs), complete data sanitization typically requires hardware-level commands such as ATA Secure Erase. This project demonstrates file-level secure wiping within a live operating system environment.

License

This project is developed for educational and research purposes.
