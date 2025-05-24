# MP3 Album Converter

A simple Python script for combining multiple MP3 files into a single album file using FFmpeg.

## Features

- **Simple Concatenation**: Combine multiple MP3 files into a single file
- **Automatic Sorting**: Files are processed in alphabetical order
- **No Quality Loss**: Uses FFmpeg's copy mode to avoid re-encoding
- **Easy to Use**: Minimal setup required

## Requirements

- Python 3.6+
- FFmpeg

## Installation

1. Install Python if not already installed:
   - Download from: https://www.python.org/downloads/

2. Download and install FFmpeg:
   - Download from: https://ffmpeg.org/download.html
   - Extract to `C:\ffmpeg\ffmpeg-6.1-essentials_build\bin` (or update the path in the script)

## Usage

1. Place your MP3 files in the input folder
2. Run the script:
```bash
python Convert_to_Album.py
```

## Configuration

Edit the script to customize:
- `input_folder`: Location of your MP3 files (default: `C:\Users\miken\Desktop\Music\downloads`)
- `output_folder`: Where the combined album will be saved (default: creates an "Album" subfolder)
- `ffmpeg_path`: Path to FFmpeg executable

## How It Works

1. The script creates a text file listing all MP3 files in the input folder
2. It uses FFmpeg's concat demuxer to combine the files without re-encoding
3. The combined file is saved to the output folder as "combined_album.mp3"
4. The temporary file list is deleted after processing

## Troubleshooting

1. **FFmpeg not found**: Ensure FFmpeg is installed and the path is correct
2. **File not found errors**: Check that your input folder contains MP3 files
3. **Permission errors**: Make sure the script has write permissions to the output folder

## License

This project is released under the MIT License. Feel free to use and modify as needed.
