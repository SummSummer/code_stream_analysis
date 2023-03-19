from struct_to_dict import struct_to_dict
from code_stream_to_bytes import code_stream_to_bytes


# 总体流程处理类
class CodeStreamAnalysis:
    def __init__(self, struct_msg: str, stream_msg: str):
        self.struct_dict = struct_to_dict.transform(struct_msg)
        self.stream_bytes = code_stream_to_bytes.transform(stream_msg)

    def total_step(self):
        pass


if __name__ == '__main__':
    # 1. 展示界面、获取用户输入
    CodeStreamAnalysis('', '').total_step()
    # 2. 调用动态库解析码流，获取转换后的结果
    # 3. 展示结果
