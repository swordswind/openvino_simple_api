# openvino_simple_api

## Introduction

`openvino_simple_api` is an API server project built based on Intel's OpenVINO framework and the MiniCPM-2B OV edition large language model. The project aims to provide a fast and accurate intelligent Q&A service that can automatically adapt to hardware and run on Intel NPU, Intel GPU, and general-purpose CPUs.

## Project Address

- Main project address: [openvino_simple_api](https://github.com/swordswind/openvino_simple_api) 
- OpenVINO source address: [openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) 
- MiniCPM-2B OV edition source address: [modelscope.cn/models/snake7gun/minicpm-2b-dpo-int4-ov](https://modelscope.cn/models/snake7gun/minicpm-2b-dpo-int4-ov) 

## Running Method

Run the command `python api.py` to start the server.

## Server Address

The API server address for the OpenVINO large language model framework is: `http://your_computer_IP:8087/`

## API Interface

### Interface Address

`/openvino/`

### Request Method

GET

### Request Parameters

- `p`: Required, robot role setting.
- `q`: Required, user's question content.

## Usage Example

Enter the following address in the browser's address bar:

```
http://127.0.0.1:8087/openvino/?p=You%20are%20a%20useful%20assistant&q=Who%20are%20you%3F
```

Press Enter, and the server will return the following JSON-formatted response:

```json
{"answer": "I am an artificial intelligence assistant."}
```

## Precautions

1. The API server only supports the GET request method.
2. The content of the server's response is for reference only. Please refer to the actual Q&A if there are any inaccuracies.

## Install Dependencies

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, copy, modify, and distribute this project.

---

### Contribution

We welcome any form of contribution, including but not limited to submitting issues, providing code improvements, and updating documentation. If you have any questions or suggestions about the project, please feel free to submit an issue or pull request.