# !/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print(f"Python 数据：{data}")
print(f"JSON 串：{json_str}")

json_str = json.dumps(data, indent=2, sort_keys=True)
print(f"key排序后的JSON pretty串：{json_str}")

# 将 JSON 对象转换为 Python 字典
json_obj = json.loads(json_str)
print(f"json_obj['name']: {json_obj['name']}")
print(f"json_obj['url']: {json_obj['url']}")

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)
    print('json文件写入完成')

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)
    print(f'json文件内容：{data}')
