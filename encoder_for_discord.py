import subprocess
import argparse
import math
import pathlib

ffmpeg_dir = "ffmpeg"
size_limit = 8  # MB


def encode(input_file, output_file="output.mp4", vcodec="libx264", audio_bitrate=64):
    v_len = (get_video_length(input_file))
    total_bitrate = size_limit * 8172 / v_len
    while (math.floor(total_bitrate - audio_bitrate)) < 1:
        print(
            f"合計ビットレート({total_bitrate}) - 音声ビットレート({audio_bitrate}) = {total_bitrate-audio_bitrate}")
        audio_bitrate = float(input("ビデオビットレートが低すぎます。音声ビットレートを下げてください: "))
    video_bitrate = math.floor(total_bitrate - audio_bitrate)
    command = f"{ffmpeg_dir} -i {input_file} -pass 1 -c:v {vcodec} -b:v {video_bitrate}k -b:a {audio_bitrate}k {output_file} && {ffmpeg_dir} -i {input_file} -pass 2 -c:v {vcodec} -b:v {video_bitrate}k -b:a {audio_bitrate}k {output_file}"

    subprocess.call(command, shell=True)


def get_video_length(file):
    result = subprocess.run(
        ["ffprobe", file, "-hide_banner", "-show_entries", "format=duration"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    lines = result.stdout.split("\n")
    for line in lines:
        if "duration=" in line:
            return float(line[9:])


def check_gpu_nvidia(device: int) -> bool:
    """
    NVIDIAのGPUデバイスが使用可能か確認する
    Args:
        device: デバイス番号
    """
    output = subprocess.check_output(["nvidia-smi", "-L"])
    lines = output.decode().split('\n')
    for line in lines:
        if line == "":
            continue
        gpu_device_id = line.split(":")[0]
        if gpu_device_id == f"GPU {device}":
            return True
    return False


if __name__ == "__main__":

    default_vcode = "libx264"
    if check_gpu_nvidia(0):
        default_vcodec = "h264_nvenc"

    parser = argparse.ArgumentParser(description="Discord用に動画をエンコードする。")
    parser.add_argument("-i", "--input_file", help="変換するファイル")
    parser.add_argument("-o", "--output_file",
                        help="出力ファイル名", default="output.mp4")
    parser.add_argument(
        "-c:v", "--vcodec", help="映像エンコーダ", default=default_vcodec
    )
    parser.add_argument("-b:a", "--audio_bitrate",
                        help="音声ビットレート(kbps)", default=64, type=float)
    parser.add_argument("-sl", "--size_limit",
                        help="容量制限(MB)", default=8, type=float)
    args = parser.parse_args()
    input_file = ""
    try:
        input_file = args.input_file.replace("\\", "/")
    except:
        i = input("動画ファイルのパスを入力: ")
        input_file = i.replace("\\", "/")
    finally:
        encode(pathlib.Path(input_file), pathlib.Path(
            args.output_file), args.vcodec, args.audio_bitrate)

# usage: encoder_for_discord.py [-h] [-o OUTPUT_FILE] [-c:v VCODEC] [-b:a AUDIO_BITRATE] [-sl SIZE_LIMIT] input_file

# Discord用に動画をエンコードする。

# positional arguments:
#   input_file            変換するファイル

# optional arguments:
#   -h, --help            show this help message and exit
#   -o OUTPUT_FILE, --output_file OUTPUT_FILE
#                         出力ファイル名
#   -c:v VCODEC, --vcodec VCODEC
#                         映像エンコーダ
#   -b:a AUDIO_BITRATE, --audio_bitrate AUDIO_BITRATE
#                         音声ビットレート(kbps)
#   -sl SIZE_LIMIT, --size_limit SIZE_LIMIT
#                         容量制限(MB)
