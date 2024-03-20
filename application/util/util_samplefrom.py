from pypinyin import lazy_pinyin
# 修改样本源列表的格式
def transform_from(documents):
    dic = []
    for doc in documents:
        dic.append({
            "样本源编号": doc.get("样本源编号",'-'),
            "采集医院": doc.get("采集医院",'-'),
            "样本源姓名": doc.get("样本源姓名",'-'),
            "性别": doc.get("性别",'-'),
            "年龄": doc.get("年龄",'-'),
            "样本创建时间": doc.get("样本创建时间",'-'),
            "样本源类型": doc.get("样本源类型",'-'),
            "知情同意": doc.get("知情同意",'-')
        })
    return dic

# 生成样本源编号
def sampleID(name,type,hospital):
    s = ''
    text = lazy_pinyin(hospital+'-'+type+'-'+name)
    for item in text:
        s+=item[0].upper()
    return s