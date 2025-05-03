from ollama import chat
from ollama import ChatResponse
from flask import Response, stream_with_context


def get_model_response(user_question):
    try:
        stream = chat(
            model='EmsStudyHelper',
            messages=[{'role': 'user', 'content': user_question}],
            stream=True,
            options={'num_ctx': 2048, 'num_thread': 4}
        )
        start = False
        for chunk in stream:
            if start:
                yield chunk['message']['content']
            if chunk['message']['content']=="</think>":
                start = True
    except Exception as e:
        return f'获取模型响应失败：{str(e)}'
