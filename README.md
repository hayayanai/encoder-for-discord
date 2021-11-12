# encoder-for-discord

- ffmpegの環境変数を通すか、ffmpegと同じディレクトリで実行してください。

```
usage: Encode_for_Discord.py [-h] [-o OUTPUT_FILE] [-c:v VCODEC]
                             [-b:a AUDIO_BITRATE]
                             input_file

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
```
