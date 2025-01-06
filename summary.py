import os
import re
import pandas as pd

def extract_final_score(file):
    project_dict = {}
    # 打开文件并读取全部内容
    with open(file, 'r') as fhand:
        content = fhand.read()
    # 项目名称
    pattern_name = r'Project Name: (.+)\n'
    project = re.search(pattern_name,content)
    project_dict['Project_name']=project.group(1).strip()

    # 项目x
    pattern_x = r'https://x.com/(.+)\n'
    try:
        twitter = re.search(pattern_x,content)
        project_dict['Twitter'] = "@"+twitter.group(1).strip()
    except:
        project_dict['Twitter'] = None

    # 项目分数
    pattern_score = r'### \d+\.\s([A-Za-z0-9\s]+)\n\*\*Score: (\d+)/(\d+)\*\*'
    matches = re.findall(pattern_score, content)
    for match in matches:
        title = match[0]  # 匹配标题部分
        score_numerator = match[1]  # 匹配分子
        score_denominator = match[2]  # 匹配分母
        project_dict[title]=score_numerator
    
    # 项目最终分数
    pattern_final_score = r"\*\*(Final\s)?Score: (\d+(\.\d+)?)/(\d+)\*\*"
    matches = re.findall(pattern_final_score, content)
    for match in matches:
        final_score = match[1]  # 总分部分（例如10）
        project_dict["Final_score"]=final_score

    return project_dict

        
folder_path = './'
# 遍历文件夹并返回文件列表
file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
projects = []
for file in file_list:
    if file.endswith("md"):
        try:
            projects.append(extract_final_score(file))
        except:
            print(file)

df = pd.DataFrame(projects)
print(df)
df.to_csv('output_summary.csv', sep=',', index=False, na_rep='N/A')