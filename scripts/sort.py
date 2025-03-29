import os
import json

# 定义统一的键顺序
key_order = [
    "##",
    "version",
    "description",
    "homepage",
    "license",
    "notes",
    "depends",
    "suggest",
    "architecture",
    "url",
    "hash",
    "extract_dir",
    "extract_to",
    "innosetup",
    "pre_install",
    "installer",
    "post_install",
    "pre_uninstall",
    "uninstaller",
    "post_uninstall",
    "env_set",
    "env_add_path",
    "bin",
    "psmodule",
    "shortcuts",
    "persist",
    "checkver",
    "autoupdate"
]

# 定义一个函数来对字典进行排序，仅处理第一层
def sort_dict(d):
    if isinstance(d, dict):
        sorted_dict = {}
        for key in key_order:
            if key in d:
                sorted_dict[key] = d[key]
        # 处理不在 key_order 中的键
        for key in sorted(set(d.keys()) - set(key_order)):
            sorted_dict[key] = d[key]
        return sorted_dict
    return d

# 定义一个函数来处理单个 JSON 文件
def process_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        sorted_data = sort_dict(data)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(sorted_data, f, indent=4, ensure_ascii=False)
            f.write('\n')  # 添加行末空行
        print(f"Processed {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# 获取脚本所在目录的上一级目录中的bucket目录
current_dir = os.path.dirname(os.path.abspath(__file__))
bucket_dir = os.path.join(os.path.dirname(current_dir), 'bucket')

# 检查bucket目录是否存在
if os.path.exists(bucket_dir) and os.path.isdir(bucket_dir):
    # 处理bucket目录中的所有JSON文件
    for file in os.listdir(bucket_dir):
        if file.endswith('.json'):
            file_path = os.path.join(bucket_dir, file)
            process_json_file(file_path)
else:
    print(f"Error: Bucket directory not found at {bucket_dir}")
