# niai-emr

> 脑血管病人工智能系统数据获取后台

## 系统配置

在config.py中可以更改系统配置

在__init__.py的create_app()中通过下面的语句改变系统配置：
```python
    app.config.from_object(config['dev'])
```