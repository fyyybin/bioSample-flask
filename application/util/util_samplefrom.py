from pypinyin import lazy_pinyin
# 修改样本源列表的格式
def transform_from(documents):
    dic = []
    for doc in documents:
        if(doc.get("样本源类型")=='其他'):
            type = doc.get('其他','')
        else:
            type = doc.get('样本源类型','')
        dic.append({
            "样本源编号": doc.get("样本源编号",'-'),
            "采集医院": doc.get("采集医院",'-'),
            "样本源姓名": doc.get("样本源姓名",'-'),
            "性别": doc.get("性别",'-'),
            "年龄": doc.get("年龄",'-'),
            "样本创建时间": doc.get("样本创建时间",'-'),
            "样本源类型": type,
            "知情同意": doc.get("知情同意",'-')
        })
    return dic

# 生成样本源编号（未知情同意）
def sampleID(source,hospital,document):
    count = 1
    for doc in document:
        count+=1
    s = ''
    if(hospital=='浙江大学医学院附属第一医院'):
        a = 'ZJU1H'
    elif(hospital=='浙江大学医学院附属第四医院'):
        a = 'ZJU4H'
    elif(hospital=='浙江大学医学院附属儿童医院'):
        a = 'ZJEB'
    else:
        a = 'TZYY'
    text = lazy_pinyin(source)
    for item in text:
        s+=item[0].upper()
    a = a + '-' + s + str(count)
    return a