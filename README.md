# 📁 Python Automation & Data Security Suite

A collection of high-performance Python utilities designed to automate system administration, data integrity, and storage optimization tasks. These tools leverage core system libraries to provide lightweight, dependency-free solutions for modern environments.

---

## 🛡️ 1. Marvellous Automated Data Shield
**Concept:** Intelligent Backup Automation

This system ensures data redundancy without wasting storage by intelligently copying only new or modified files. It creates timestamped compressed archives to ensure efficient and reliable data protection, making it ideal for large-scale directory mirroring.

* **Logic:** Utilizes MD5 checksums to verify if a file's content has actually changed before performing a copy operation.
* **Archiving:** Automatically generates `.zip` archives utilizing ISO-standard timestamps for version control.
* **Scheduling:** Features a built-in scheduler allowing the system to run at specific user-defined intervals (e.g., every 60 minutes).
* **Usage:**
    ```bash
    python DataShield.py [Interval_in_Minutes] [Source_Directory]
    ```

---

## 📊 2. Automated Platform Surveillance System
**Concept:** Periodic System Health Logging

A robust monitoring tool that functions as a "black box" recorder for a PC or server. It automates the capture of hardware metrics and process snapshots at fixed intervals to help diagnose performance bottlenecks or unauthorized resource usage.

* **System Metrics:** Logs critical performance data including CPU Load %, RAM Availability, Disk usage for all partitions, and Network sent/received statistics.
* **Process Tracking:** Captures detailed snapshots of all running processes, including PID, process name, username, status, start time, and individual CPU/Memory footprint.
* **Automation:** Operates silently in the background, dynamically creating new log folders and timestamped log files.
* **Execution:** Continues to repeat monitoring cycles until manually terminated (e.g., via `Ctrl + C`).
* **Usage:**
    ```bash
    python Surveillance.py [Interval_in_Minutes]
    ```

---

## 🧹 3. Automated Disk Sanitiser
**Concept:** Content-Aware Storage Optimization

Unlike traditional cleanup tools that rely on filenames, this utility analyzes the "DNA" of a file using MD5 hashing to find duplicates regardless of their name or location.

* **Deep Scan:** Recursively traverses complex directory structures to identify identical bit-streams.
* **Safe Deletion:** Automatically deletes redundant copies while strictly preserving one original master copy.
* **Data Integrity:** Employs the `hashlib` library and MD5 checksums to ensure 0% false positives during the sanitization process.
* **Usage:**
    ```bash
    python DiskSanitiser.py [Target_Directory]
    ```

---

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Core Libraries:** `os`, `shutil`, `hashlib`, `zipfile`, `time`
* **Monitoring Extensions:** `psutil` (for Platform Surveillance)

---

### 👨‍💻 Author
**Advait Rahul Ghatge**
*Python Developer | Automation Specialist*
