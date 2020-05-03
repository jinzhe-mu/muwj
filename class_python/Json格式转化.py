import json
info = [{
        "name": "Tom",
        "gender": "male",
        'other': None
        },
        {
        "name": "Jack",
        "gender": "male",
        'other': None
        }]  # 列表里面放了两个字典，字典里面分别放了三个键值对
# dumps： 将
data = json.dumps(info, sort_keys=True, indent=4)  # 以key值进行排序 indent=4为每一个字符串以换行缩进的方式缩进
print(data)
print(type(data))



info2 = [{
        "name": "Tom",
        "gender": "male",
        'other': None
        },
        {
        "name": "Jack",
        "gender": "male",
        'other': None
        }]  # 列表里面放了两个字典，字典里面分别放了三个键值对

print("读取json文件")
# dump方法将info2内容写入wwi.py文件
json.dump(info2, open("wwi.py", "w"))  # 以key值进行排序 indent=4为每一个字符串以换行缩进的方式缩进

print("loads方法：")
str1 = '''
[{
        "name": "Tom",
        "gender": "male"
},
{
        "name": "Jack",
        "gender": "male"
}]
'''

print(type(str1))
# loads： 将字符串转换为json
data3 = json.loads(str1)  # 转换为列表形
print(type(data3))
print(data3)

print("load方法：")
# load：把文件打开从字符串转换成json
jsobj = json.load(open('wwi.py', 'r'))
print(jsobj)
print(type(jsobj))
print(jsobj[0]['name'])  # 打印第0个key为name的值
print(jsobj[1]['gender'])  # 打印第2个key为gender的值

