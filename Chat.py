import asyncio
from ollama import AsyncClient

# 初始化对话历史
messages = [{"role": "user", "content": "请扮演一位亲切的朋友，在日常闲聊的语境下，生成一段口语化的对话或独白。"}]


async def chat_with_ollama():
    client = AsyncClient()
    print("deepseek-r1 模型服务已启动！输入 '退出' 结束对话。")

    while True:
        # 获取用户输入
        user_input = input("用户: ")
        if user_input.lower() in ["退出", "quit", "stop", "bye", "拜拜"]:
            print("退出与 deepseek-r1 模型的对话。")
            break

        # 将用户输入添加到对话历史
        messages.append({"role": "user", "content": user_input})

        response_content = ""
        print("deepseek-r1: ", end='', flush=True)
        async for part in await client.chat(model='deepseek-r1:8b',
                                            messages=messages,
                                            stream=True,
                                            think=False):
            response_content += part['message']['content']
            print(f"{part['message']['content']}", end='', flush=True)
        print()
        # 将模型的响应添加到对话历史
        messages.append({"role": "assistant", "content": response_content})


# 运行异步聊天函数
if __name__ == '__main__':
    asyncio.run(chat_with_ollama())

