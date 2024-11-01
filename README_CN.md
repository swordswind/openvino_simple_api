# openvino_simple_api

## 简介

`openvino_simple_api` 是一个基于 Intel 的 OpenVINO 框架和 MiniCPM-2B OV 版大语言模型构建的 API 服务器项目。该项目旨在提供一个快速、准确的智能问答服务，能够自动适配硬件并在 Intel NPU、Intel GPU 和通用 CPU 上运行。

## 项目地址

- 主项目地址：[openvino_simple_api](https://github.com/swordswind/openvino_simple_api)
- OpenVINO 源地址：[openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino)
- MiniCPM-2B OV 版源地址：[modelscope.cn/models/snake7gun/minicpm-2b-dpo-int4-ov](https://modelscope.cn/models/snake7gun/minicpm-2b-dpo-int4-ov)

## 运行方式

运行命令 `python api.py` 即可启动服务器。

## 服务器地址

OpenVINO 大语言模型框架 API 服务器地址为：`http://你的电脑IP:8087/`

## API 接口

### 接口地址

`/openvino/`

### 请求方式

GET

### 请求参数

- `p`：必填，机器人角色设定。
- `q`：必填，用户提问内容。

## 使用示例

在浏览器地址栏输入以下地址：

```
http://127.0.0.1:8087/openvino/?p=你是一个有用的助手&q=你是谁？
```

按下回车键，服务器将返回以下 JSON 格式的回答：

```json
{"answer": "我是一个人工智能助手。"}
```

## 注意事项

1. API 服务器仅支持 GET 请求方式。
2. 服务器返回的回答内容仅供参考，如有不准确之处，请以实际问答为准。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 许可证

该项目采用 [MIT 许可证](LICENSE)。你可以自由地使用、复制、修改和分发该项目。

---

### 贡献

欢迎任何形式的贡献，包括但不限于提交问题、提供代码改进、更新文档等。如果你对项目有任何疑问或建议，请随时提交 issue 或 pull request。
