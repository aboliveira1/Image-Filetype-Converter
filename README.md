# Simple Image File Converter

<div align="center">
  <img src="https://github.com/user-attachments/assets/e69f3a83-7a97-4f4d-9389-4c7bae582e50" alt="Image Converter GUI" width="300">
</div>

---

A lightweight app for converting image file types. This tool allows you to select an image from your computer, choose an output format, and easily save the newly converted file. Great for quick conversions without hassle!

---


## Features
- **Lightweight & Simple**: No need for heavy libraries or complicated setups.
- **Supports Multiple Formats**: JPG (JPEG), PNG, BMP, GIF, TIFF, WEBP.
- **Automatic RGBA Handling**: Converts RGBA images to RGB automatically for JPEG output.
- **Self-Contained EXE**: Download and run `simple_image_file_converter.exe` without installing any dependencies.

---

## Getting Started

### 1. Using the EXE (Recommended for Most Users)
1. Go to the newest release of the [Image Filetype Converter](https://github.com/aboliveira1/Image-Filetype-Converter/releases/tag/app).
2. Download `simple_image_file_converter.exe`.
3. Double-click the EXE to launch the GUI.
4. Select an image to convert, choose your target format, and click **Convert and Save**.

**That’s it!** No Python or additional libraries are required.

### 1. Using the Source Code

#### Instructions
1. **Install Python**: Ensure Python 3.x is installed on your computer.

2. **Install Required Library**:  
   Open your terminal or command prompt and run the following command:  
   `pip install pillow`

3. **Run the Script**:  
   - Save the code provided in a file named `image_converter.py`.  
   - Open your terminal or command prompt, navigate to the folder containing the script, and execute:  
     `python image_converter.py`

The GUI will launch, and you can use it to convert your images.



## Usage

1. **Select Image:** Click the Select Image button to open a file chooser.
2. **Choose Format:** Pick the desired output format from the dropdown.
3. **Convert and Save:** Click Convert and Save to pick the destination folder and filename.

You’ll get a success message once the image is saved.
