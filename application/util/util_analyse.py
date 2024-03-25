# 修改测序数据格式
def transform_analyse(document):
    dic = []
    for doc in document:
        dic.append({
            "样本编号": doc.get("样本编号","-"),
            "采集医院": doc.get("采集医院","-"),
            "样本源类型": doc.get("样本源类型","-"),
            "样本源姓名": doc.get("样本源姓名","-"),
            "研究用途": doc.get("研究用途","-"),
            "入库时间": doc.get("入库时间","-"),
            "是否测序": doc.get("是否测序","-"),
            "测序公司": doc.get("测序公司","-"),
            "测序平台": doc.get("测序平台","-"),
            "测序数据": doc.get("测序数据","-"),
            "测序状态": doc.get("测序状态","-"),
        })
    return dic