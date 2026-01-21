import requests
import os
import sys
import time
import json
from Chat2Audio import format_size


def generate_tts_audio(text: str, output_file="output.wav"):
    """生成TTS音频文件"""
    print(f"开始生成语音: {text[:50]}...")

    # 发送请求
    json_data = {
        "refer_wav_path": "F:/developToolkit/GSV/符玄/激动说话-如此境地，还要处理将军交来的星核猎手，可不是大祸临头？.wav",
        "prompt_text": "如此境地，还要处理将军交来的星核猎手，可不是大祸临头？",
        "prompt_language": "zh",
        "text": text,
        "text_language": "zh"
    }

    try:
        url = "http://127.0.0.1:9880"
        response = requests.post(url, json=json_data)

        if response.status_code == 200:
            # 保存文件
            with open(output_file, 'wb') as f:
                f.write(response.content)

            file_size = os.path.getsize(output_file)
            format_file_size = format_size(file_size)
            print(f"✅ 成功生成语音！文件大小: {format_file_size} ")
            return True
        else:
            print(f"❌ 生成失败，状态码: {response.status_code}")
            print(f"错误信息: {response.text}")
            return False

    except Exception as e:
        print(f"❌ 发生错误: {e}")
        return False

