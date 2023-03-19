from data_transform import data_transform as transform

if __name__ == '__main__':
    # 1. 展示界面、获取用户输入
    # 2. 调用动态库解析码流，获取转换后的结果
    print(transform.run_cpp('1.so', '123', 'abc'))
    # 3. 展示结果
