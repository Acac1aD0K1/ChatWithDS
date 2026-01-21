import asyncio

from ollama import AsyncClient

from play_audio import play_audio
from gsv_tts import generate_tts_audio


async def chat_with_ollama_with_tts():
    """带TTS的异步聊天函数"""
    client = AsyncClient()
    messages = [{"role": "user",
                 "content": "请扮演一位朋友，在日常闲聊的语境下，生成一段口语化的对话或独白，要求在40字以内"}]

    print("deepseek-r1 模型服务已启动！输入 '退出' 结束对话。")

    while True:
        # 获取用户输入
        user_input = input("用户: ")
        if user_input.lower() in ["退出", "quit", "stop", "bye", "拜拜"]:
            print("退出与 deepseek-r1 模型的对话。")
            break

        # 将用户输入添加到对话历史
        messages.append({"role": "user", "content": user_input})

        # 获取模型回复
        response_content = ""
        print("deepseek-r1: ", end='', flush=True)
        async for part in await client.chat(model='deepseek-r1:8b', messages=messages, stream=True, think=False):
            response_content += part['message']['content']
            print(f"{part['message']['content']}", end='', flush=True)
        print()

        # 将模型的响应添加到对话历史
        messages.append({"role": "assistant", "content": response_content})

        # 生成并播放TTS
        print("\n" + "=" * 50)
        print("正在生成语音...")

        if generate_tts_audio(response_content):
            play_audio("output.wav")
        else:
            print("语音生成失败，继续下一轮对话...")

        print("=" * 50 + "\n")


def format_size(size_in_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} PB"


# 运行异步聊天函数
if __name__ == '__main__':
    asyncio.run(chat_with_ollama_with_tts())
