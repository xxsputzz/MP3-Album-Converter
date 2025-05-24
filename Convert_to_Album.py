import os
import subprocess

# Folder containing your MP3 files
input_folder = r"C:\Users\miken\Desktop\Music\downloads"
output_folder = os.path.join(input_folder, "Album")
os.makedirs(output_folder, exist_ok=True)

# Path to FFmpeg
ffmpeg_path = r"C:\ffmpeg\ffmpeg-6.1-essentials_build\bin\ffmpeg.exe"

# Create a temporary file list for FFmpeg
file_list_path = os.path.join(input_folder, "files_to_merge.txt")

with open(file_list_path, "w", encoding="utf-8") as f:
    for filename in sorted(os.listdir(input_folder)):
        if filename.lower().endswith(".mp3"):
            full_path = os.path.join(input_folder, filename)
            f.write(f"file '{full_path.replace('\\', '/')}'\n")

# Output path
output_file = os.path.join(output_folder, "combined_album.mp3")

# Run FFmpeg to concatenate the files
subprocess.run([
    ffmpeg_path,
    "-f", "concat",
    "-safe", "0",
    "-i", file_list_path,
    "-c", "copy",
    output_file
])
 
# Optionally delete the file list
os.remove(file_list_path)

print(f"\n✅ Combined MP3 saved to: {output_file}")
