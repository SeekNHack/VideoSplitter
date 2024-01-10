import sys
import os
import subprocess

def dividi_video(input_file, num_parti, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    video_info = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_file])
    durata_totale = float(video_info)

    durata_parte = durata_totale / num_parti

    for i in range(num_parti):
        inizio = i * durata_parte
        fine = (i + 1) * durata_parte

        output_file = os.path.join(output_folder, f'parte_{i + 1}.mp4')
        subprocess.run(['ffmpeg', '-i', input_file, '-ss', str(inizio), '-to', str(fine), '-c', 'copy', output_file])

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <video_file_path> <num_parti> <output_folder>")
        sys.exit(1)

    input_file = sys.argv[1]
    num_parti = int(sys.argv[2])
    output_folder = sys.argv[3]

    dividi_video(input_file, num_parti, output_folder)
