from fastapi import FastAPI, Query
import uvicorn
import openvino_genai

app = FastAPI()
word_count = 0
response = ""
model_path = "model/minicpm-2b-dpo-int4-ov"
print("正在加载OpenVINO框架的大语言模型，请稍等...")
try:
    model = openvino_genai.LLMPipeline(model_path, "NPU")
    print("正在使用Intel NPU")
except:
    print("未检测到Intel NPU")
    try:
        model = openvino_genai.LLMPipeline(model_path, "GPU")
        print("正在使用Intel GPU")
    except:
        print("未检测到Intel GPU")
        model = openvino_genai.LLMPipeline(model_path, "CPU")
        print("正在使用通用CPU")


def streamer(subword):
    global word_count, response
    if word_count < 100:
        response += subword
        word_count += len(subword)
    else:
        return True


@app.get("/openvino/")  # 使用举例：http://127.0.0.1:8087/openvino/?p=你是一个有用的助手&q=你是谁？
async def run_openvino(p: str = Query(...), q: str = Query(...)):
    global word_count, response
    word_count = 0
    response = ""
    message = f"<|im_start|>system\n{p}<|im_end|>\n<|im_start|>user\n{q}<|im_end|>\n<|im_start|>assistant\n"
    model.generate(message, eos_token_id=151645, max_length=100, streamer=streamer)
    response = response.split("<")[0].strip()
    return {"answer": response}


print("本地OpenVINO大语言模型框架API服务器启动成功!")
uvicorn.run(app, host="0.0.0.0", port=8087)
