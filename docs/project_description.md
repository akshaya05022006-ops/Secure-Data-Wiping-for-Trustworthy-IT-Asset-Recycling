# Project Description

## Title
Secure Data Wiping for Trustworthy IT Asset Recycling

## Introduction
With the rapid growth of technology, electronic waste (e-waste) has become a major environmental issue. Millions of electronic devices such as laptops, smartphones, and storage drives are discarded every year. One of the main reasons people hesitate to recycle their devices is the fear that sensitive data stored on them may be recovered.

Traditional file deletion methods do not completely remove data from storage devices. Even after deletion, files can often be recovered using data recovery tools. This creates a serious risk of data breaches.

The Secure Data Wiping for Trustworthy IT Asset Recycling project aims to solve this problem by providing a system that permanently deletes sensitive data from storage devices before they are recycled.

## Problem Statement
Many individuals and organizations avoid recycling their old devices because they fear that personal or confidential data may be recovered. Standard deletion techniques are not secure enough to prevent data recovery.

A secure and verifiable method is needed to ensure that data stored on devices is completely erased before recycling.

## Proposed Solution
This project implements a secure data wiping system using a multi-pass overwrite method. The system overwrites files multiple times with specific patterns such as zeros and random data before deleting them permanently.

The application also calculates a SHA-256 checksum of the file before wiping to provide verification and maintain logs of the wiping process.

A graphical user interface allows users to select files or folders and perform secure wiping operations easily.

## Key Features
- Secure multi-pass file overwriting
- SHA-256 checksum generation
- File and folder wiping support
- Real-time progress monitoring
- Wiping logs and verification records
- Simple graphical user interface

## System Workflow
1. The user selects a file or folder.
2. The system calculates the SHA-256 checksum of the file.
3. The secure wipe algorithm overwrites the file multiple times.
4. The file is permanently deleted from the system.
5. The system records logs of the wiping process.

## Technologies Used
- Python
- Tkinter (GUI)
- hashlib (checksum generation)
- threading (background processing)
- os module (file handling)

## Applications
- Secure disposal of old laptops and storage devices
- Data protection before device recycling
- Secure data deletion in organizations
- Cybersecurity awareness and research

## Limitations
This system performs file-level secure wiping. For solid-state drives (SSDs), full sanitization may require hardware-level commands such as ATA Secure Erase.

## Future Enhancements
- Integration with hardware-based secure erase tools
- Automated detection of sensitive files
- Cloud-based verification reports
- Enterprise-level bulk device wiping

## Conclusion
Secure data wiping is an important step in building trust in IT asset recycling. By ensuring that sensitive data is permanently erased, users can safely recycle their devices without the risk of data breaches.
