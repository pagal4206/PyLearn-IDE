## 🚀 PyLearn IDE
[![Readme style](https://img.shields.io/badge/readme%20style-Quick-green)](#)
[![Python](https://img.shields.io/badge/Python-3.14-blue)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)](#)

**PyLearn IDE** is a beginner-friendly **Python desktop IDE** built with **Tkinter**, designed for students to learn Python through lessons, modules, and hands-on coding.

---

## 📑 Table of Contents
<details>
  <summary>Click to expand</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#build-exe">Build EXE</a></li>
    <li><a href="#contribution">Contribution</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#author-info">Author Info</a></li>
  </ol>
</details>

---

## 📘 About The Project

**PyLearn IDE** is created to make Python learning simple and practical.

### Why PyLearn IDE?
- 🧑‍🎓 Student-friendly interface  
- 📘 Built-in Python lessons  
- 💻 Simple coding environment  
- 🧩 Modular project structure  
- 🌙 Dark theme UI  
- 🪟 Windows desktop application  

This project is ideal for **beginners, students, and self-learners**.

<p align="right">[<a href="#pylearn-ide">back to top</a>]</p>

---

## 🛠️ Built With

<div align="center">
  <img src="https://img.shields.io/badge/Python-20232A?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Tkinter-FFCA28?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Pillow-3DDC84?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/PyInstaller-4B8BBE?style=for-the-badge"/>
</div>

<p align="right">[<a href="#pylearn-ide">back to top</a>]</p>

---

## 🚀 Getting Started

### Build Windows EXE (PyLearn IDE)

Follow these commands to build a standalone **Windows executable (.exe)** using **PyInstaller**.

#### Prerequisites
Make sure you have:

- Python **3.14**
- pip
- Windows OS

Check required tools:
1. Download / Clone Repository
   ```sh
   git clone https://github.com/pagal4206/PyLearn-IDE
   ```
2. Go to Project Folder
   ```sh
   cd PyLearn-IDE
   ```
3. Install Required Packages
   ```sh
   pip install pillow && pip install pyinstaller
   ```
4. Build Windows EXE
   ```sh
   pyinstaller --onefile --windowed --name PyLearnIDE --icon=assets/icon.ico --add-data "assets;assets" main.py
   ```

