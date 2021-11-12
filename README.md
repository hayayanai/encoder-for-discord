# encoder-for-discord

![build executables](https://github.com/hayayanai/encoder-for-discord/actions/workflows/actions.yml/badge.svg)

- ffmpegの環境変数を通すか、ffmpegと同じディレクトリで実行してください。

```
usage: encoder_for_discord.py [-h] [-o OUTPUT_FILE] [-c:v VCODEC] [-b:a AUDIO_BITRATE] [-sl SIZE_LIMIT] input_file

Discord用に動画をエンコードする。

positional arguments:
  input_file            変換するファイル

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        出力ファイル名
  -c:v VCODEC, --vcodec VCODEC
                        映像エンコーダ
  -b:a AUDIO_BITRATE, --audio_bitrate AUDIO_BITRATE
                        音声ビットレート(kbps)
  -sl SIZE_LIMIT, --size_limit SIZE_LIMIT
                        容量制限(MB)
```
