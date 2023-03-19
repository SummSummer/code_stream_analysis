class CodeStreamToBytes:
    def __init__(self, string: str):
        self.code_stream = string.strip()

    def str_to_bytes(self) -> bytes:
        return bytes([int(x, base=16) for x in self.code_stream.split(' ')])


def transform(code_stream: str) -> bytes:
    return CodeStreamToBytes(code_stream).str_to_bytes()
