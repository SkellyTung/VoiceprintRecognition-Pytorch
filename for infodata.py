import os
import json

# 设置语音文件目录路径
audio_dir = 'dataset/zhvoice/audio'

# 创建用于存储语音样本信息的列表
data = []

# 遍历语音文件目录
for filename in os.listdir(audio_dir):
    if filename.endswith('.wav'):
        file_path = os.path.join(audio_dir, filename)
        label = filename.split('.')[0]  # 假设文件名即为标签
        sample_info = {
            'id': filename,
            'file_path': file_path,
            'label': label
        }
        data.append(sample_info)

# 构建包含数据列表的字典
info_data = {'data': data}

# 将数据保存为 JSON 文件
json_path = 'dataset/zhvoice/text/infodata.json'
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(info_data, f, ensure_ascii=False, indent=4)

print('infodata.json 文件生成完毕。')
