import os
import re

# 获取当前工作目录
root_dir = os.getcwd()

# 遍历根目录及所有子目录
for subdir, dirs, files in os.walk(root_dir):
    for filename in files:
        # 使用正则表达式匹配文件名中的数字
        match = re.search(r'net_params_(\d+).pkl', filename)
        if match:
            # 提取文件名中的数字并转换为整数
            number = int(match.group(1))
            # 检查数字是否不是50的倍数
            if number % 10 != 0:
                # 构建完整的文件路径
                file_path = os.path.join(subdir, filename)
                # 删除文件
                os.remove(file_path)
                print(f"Deleted: {file_path}")

