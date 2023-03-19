import ctypes
from ctypes import *


# 用于调用cpp动态库，并将执行结果返回
class DataTransmission:
    def __init__(self, cpp_so_path: str, code_stream: str, struct_str: str):
        self.cpp_so_path = cpp_so_path
        self.code_stream = code_stream
        self.struct_str = struct_str

    def run_cpp(self) -> bytes:
        load = ctypes.cdll.LoadLibrary
        lib = load('./' + self.cpp_so_path)
        lib.get_python_input.restype = c_char_p
        lib.get_python_input.argtypes = [c_char_p]

        # 传给cpp的c类型是const char*
        code_stream = create_string_buffer(self.code_stream.encode('utf-8'))
        struct_str = create_string_buffer(self.struct_str.encode('utf-8'))

        # cpp中的调用函数为 const char* get_python_input(const char*, const char*)
        return lib.get_python_input(code_stream, struct_str)


# 调用方法 run_cpp('1.so', '123', 'abc')
def run_cpp(cpp_so_path: str, code_stream: str, struct_str: str) -> bytes:
    return DataTransmission(cpp_so_path, code_stream, struct_str).run_cpp()
