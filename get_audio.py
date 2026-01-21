import pyaudio
import wave


# Python录音
def get_audio(sec):
    # 创建对象
    p = pyaudio.PyAudio()
    # 创建流：采样位，声道数，采样频率，缓冲区大小，input=True
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    # 创建式打开音频文件
    wf = wave.open('voice.wav', 'wb')
    # 设置音频文件的属性:声道数，采样位，采样频率
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)
    print('开始录音')
    for w in range(int(16000 * sec / 1024)):
        data = stream.read(1024)
        wf.writeframes(data)
    print('录音结束')
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()
    return 'voice.wav'
