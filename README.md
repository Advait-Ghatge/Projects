> 📁 **Python Automation & Data Security Suite**

A collection of high-performance Python utilities designed to automate system administration, data integrity, and storage optimization tasks. These tools leverage core system libraries to provide lightweight, dependency-free solutions for modern environments.


🛡️ **1. Marvellous Automated Data Shield**
Concept: Intelligent Backup Automation

This system ensures data redundancy without wasting storage. By comparing file states, it only processes changes, making it ideal for large-scale directory mirroring.

Logic: Uses MD5 checksums to verify if a file has actually changed before copying.

Archiving: Automatically generates .zip archives with ISO-standard timestamps.

Scheduling: Includes a built-in scheduler to run at user-defined intervals (e.g., every 60 minutes).

Usage: ```bash
python DataShield.py [Interval_in_Minutes] [Source_Directory]


📊 **2. Automated Platform Surveillance System**
Concept: Periodic System Health Logging

A monitoring tool that provides a "black box" recorder for your PC or server. It captures hardware metrics and process snapshots to help diagnose performance bottlenecks or unauthorized resource usage.

System Metrics: Logs CPU Load %, RAM Availability, Disk I/O, and Network Throughput.

Process Tracking: Captures a snapshot of all running processes, including their PID, status, and memory footprint.

Automation: Runs silently in the background, creating new log folders and files dynamically.

Usage: ```bash
python Surveillance.py [Interval_in_Minutes]


🧹 **3. Automated Disk Sanitiser**
Concept: Content-Aware Storage Optimization

Traditional cleanup tools only look at filenames. This tool looks at the "DNA" of the file (MD5 Hash) to find duplicates even if they have been renamed or moved.

Deep Scan: Recursively traverses directories to find identical bit-streams.

Safe Deletion: Deletes the redundant copies while strictly preserving one original master copy.

Data Integrity: Uses hashlib to ensure 0% false positives during the deletion process.

Usage: ```bash
python DiskSanitiser.py [Target_Directory]
