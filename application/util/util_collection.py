# 修改采集需求的格式
def transform_cols(documents):
    dic = []
    for doc in documents:
        dic.append({
            "样本源编号": doc.get("样本源编号",'-'),
            "样本编号": doc.get("样本编号",'-'),
            "样本源姓名": doc.get("样本源姓名",'-'),
            "样本源类型": doc.get("样本源类型",'-'),
            "年龄": doc.get("年龄",'-'),
            "性别": doc.get("性别",'-'),
            "样本创建时间": doc.get("样本创建时间",'-'),
            "知情同意": doc.get("知情同意",'-'),
            "采集时间": doc.get("采集时间",'-'),
            "采集医院": doc.get("采集医院",'-'),
            "研究用途": doc.get("研究用途",'-'),
            "样本量": doc.get("样本量"),
            "样本数量": doc.get("样本数量"),
            "预处理": doc.get("预处理",'-'),
            "采集状态": doc.get("采集状态",'-'),
            "运输方": doc.get("运输方",'-'),
            "运出时间": doc.get("运出时间",'-'),
            "运输状态": doc.get("运输状态",'-'),
            "负责人": doc.get("负责人",'-'),
            "负责人联系方式": doc.get("负责人联系方式",'-'),
            "接收状态": doc.get("接收状态",'-'),
            "接收人": doc.get("接收人",'-'),
            "接收时间": doc.get("接收时间",'-'),
            "接收人联系方式": doc.get("接收人联系方式",'-')
        })
    return dic

# 修改采集需求的格式
def transform_detail(doc):
    dic = {
            "样本源编号": doc.get("样本源编号",'-'),
            "样本编号": doc.get("样本编号",'-'),
            "样本源姓名": doc.get("样本源姓名",'-'),
            "样本源类型": doc.get("样本源类型",'-'),
            "年龄": doc.get("年龄",'-'),
            "性别": doc.get("性别",'-'),
            "样本创建时间": doc.get("样本创建时间",'-'),
            "知情同意": doc.get("知情同意",'-'),
            "采集时间": doc.get("采集时间",'-'),
            "采集医院": doc.get("采集医院",'-'),
            "研究用途": doc.get("研究用途",'-'),
            "样本量": doc.get("样本量"),
            "样本数量": doc.get("样本数量"),
            "预处理": doc.get("预处理",'-'),
            "采集状态": doc.get("采集状态",'-'),
            "运输方": doc.get("运输方",'-'),
            "运出时间": doc.get("运出时间",'-'),
            "运输状态": doc.get("运输状态",'-'),
            "负责人": doc.get("负责人",'-'),
            "负责人联系方式": doc.get("负责人联系方式",'-'),
            "接收状态": doc.get("接收状态",'-'),
            "接收人": doc.get("接收人",'-'),
            "接收时间": doc.get("接收时间",'-'),
            "接收人联系方式": doc.get("接收人联系方式",'-')
        }
    return dic

# 样本编号
def transform_id(id,number,date):
    return id+'-'+date+'-'+str(number+1)

# 样本统计
def transform_static(document,name):
    dic = {}
    src = {
        "浙江大学医学院附属第一医院": "/src/assets/hospitals/zj1h.jpg",
        "浙江大学医学院附属第四医院": "/src/assets/hospitals/zj4h.jpg",
        "台州医院": "/src/assets/hospitals/tzh.jpg",
        "浙江大学医学院附属儿童医院": "/src/assets/hospitals/zjeb.jpg",
    }
    total = 0
    input = 0
    inputed = 0
    if document.alive:
        for doc in document:
            total+=1
            if doc.get('入库状态'):
                if doc.get('入库状态')=='待入库':
                    input += 1
                else:
                    inputed += 1
    dic = {
        "name": name,
        "src": src[name],
        "total": total,
        "input": input,
        "inputed": inputed
    }
    return dic