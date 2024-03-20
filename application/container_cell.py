from flask import Blueprint, request, make_response, jsonify
from pymongo import MongoClient
import json
import datetime
from application.util.util_container import search_cell
bp = Blueprint('container_bp', __name__, url_prefix='')

# 查询cell
@bp.route('/container_cell/', methods=['POST'])
def get_container_data():
    """
        获取数据库样本
    """
    try:
        client = MongoClient(host='localhost', port=27017)
        mongodb = client['bioSample']['container'].find()
        result =[      
                    {
                        "treePos":"1",
                        "label": "冰箱存储房间_1",
                        "icon": "TakeawayBox",
                        "level": 1,
                        "children": [
                            {
                                "treePos":"11",
                                "label": "立式冰箱_R01",
                                "icon": "Refrigerator",
                                "level": 2,
                                "children": [
                                    {
                                        "treePos":"111",
                                        "label": "层_1",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1111",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11111",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11112",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11113",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"11114",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1112",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11121",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11122",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11123",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"11124",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1113",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11131",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11132",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11133",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11134",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1114",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11141",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11142",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11143",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11144",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"111441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"111444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"112",
                                        "label": "层_2",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1121",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11211",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11212",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11213",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"11214",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1122",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11221",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11222",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11223",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"11224",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1123",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11231",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11232",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11233",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11234",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1124",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11241",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11242",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11243",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11244",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"112441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"112444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"113",
                                        "label": "层_3",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1131",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11311",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11312",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11313",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"11314",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1132",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11321",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11322",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11323",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"11324",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1133",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11331",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11332",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11333",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11334",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1134",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11341",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11342",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11343",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11344",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"113441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"113444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"114",
                                        "label": "层_4",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1141",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11411",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11412",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11413",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"11414",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1142",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11421",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11422",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11423",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"11424",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1143",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11431",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11432",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11433",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11434",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1144",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"11441",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11442",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11443",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"11444",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"114441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"114444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "treePos":"12",
                                "label": "立式冰箱_R02",
                                "icon": "Refrigerator",
                                "level": 2,
                                "children": [
                                    {
                                        "treePos":"121",
                                        "label": "层_1",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1211",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12111",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12112",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12113",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"12114",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1212",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12121",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12122",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12123",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"12124",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1213",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12131",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12132",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12133",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12134",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1214",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12141",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12142",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12143",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12144",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"121441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"121444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"122",
                                        "label": "层_2",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1221",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12211",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12212",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12213",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"12214",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1222",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12221",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12222",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12223",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"12224",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1223",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12231",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12232",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12233",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12234",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1224",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12241",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12242",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12243",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12244",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"122441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"122444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"123",
                                        "label": "层_3",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1231",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12311",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12312",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12313",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"12314",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1232",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12321",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12322",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12323",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"12324",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1233",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12331",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12332",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12333",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12334",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1234",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12341",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12342",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12343",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12344",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"123441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"123444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"124",
                                        "label": "层_4",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1241",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12411",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12412",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12413",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"12414",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1242",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12421",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12422",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12423",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"12424",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1243",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12431",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12432",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12433",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12434",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1244",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"12441",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12442",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12443",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"12444",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"124441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"124444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                            {
                                "treePos":"13",
                                "label": "立式冰箱_R03",
                                "icon": "Refrigerator",
                                "level": 2,
                                "children": [
                                    {
                                        "treePos":"131",
                                        "label": "层_1",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1311",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13111",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13112",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13113",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"13114",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1312",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13121",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13122",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13123",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"13124",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1313",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13131",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13132",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13133",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13134",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1314",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13141",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13142",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13143",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13144",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"131441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"131444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"132",
                                        "label": "层_2",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1321",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13211",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13212",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13213",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"13214",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1322",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13221",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13222",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13223",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"13224",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1323",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13231",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13232",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13233",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13234",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1324",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13241",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13242",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13243",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13244",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"132441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"132444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"133",
                                        "label": "层_3",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1331",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13311",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13312",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13313",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"13314",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1332",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13321",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13322",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13323",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"13324",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1333",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13331",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13332",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13333",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13334",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1334",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13341",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13342",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13343",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13344",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"133441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"133444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"134",
                                        "label": "层_4",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"1341",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13411",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13412",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13413",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"13414",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1342",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13421",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13422",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13423",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"13424",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1343",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13431",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13432",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13433",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13434",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"1344",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"13441",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13442",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13443",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"13444",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"134441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"134444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                        ]
                    },
                    {
                                "treePos":"21",
                                "label": "液氮罐_Y01",
                                "icon": "Refrigerator",
                                "level": 2,
                                "children": [
                                    {
                                        "treePos":"211",
                                        "label": "层_1",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"2111",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21111",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21112",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21113",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"21114",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2112",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21121",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21122",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21123",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"21124",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2113",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21131",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21132",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21133",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21134",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2114",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21141",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21142",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21143",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21144",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"211441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"211444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"212",
                                        "label": "层_2",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"2121",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21211",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21212",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21213",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"21214",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2122",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21221",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21222",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21223",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"21224",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2123",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21231",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21232",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21233",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21234",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2124",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21241",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21242",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21243",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21244",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"212441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"212444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"213",
                                        "label": "层_3",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"2131",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21311",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21312",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21313",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"21314",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2132",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21321",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21322",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21323",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"21324",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2133",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21331",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21332",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21333",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21334",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2134",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21341",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21342",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21343",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21344",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"213441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"213444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                    {
                                        "treePos":"214",
                                        "label": "层_4",
                                        "icon": "Files",
                                        "level": 3,
                                        "children": [
                                            {
                                                "treePos":"2141",
                                                "label": "架_1",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21411",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214111",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214112",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214113",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214114",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21412",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214121",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214122",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214123",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214124",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21413",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214131",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214132",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214133",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214134",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"21414",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214141",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214142",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214143",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214144",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2142",
                                                "label": "架_2",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21421",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214211",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214212",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214213",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214214",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21422",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214221",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214222",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214223",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214224",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21423",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214231",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214232",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214233",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214234",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                         "treePos":"21424",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214241",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214242",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214243",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214244",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2143",
                                                "label": "架_3",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21431",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214311",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214312",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214313",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214314",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21432",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214321",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214322",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214323",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214324",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21433",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214331",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214332",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214333",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214334",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21434",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214341",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214342",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214343",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214344",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "treePos":"2144",
                                                "label": "架_4",
                                                "icon": "Coin",
                                                "level": 4,
                                                "children": [
                                                    {
                                                        "treePos":"21441",
                                                        "label": "行_1",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214411",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214412",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214413",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214414",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21442",
                                                        "label": "行_2",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214421",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214422",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214423",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214424",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21443",
                                                        "label": "行_3",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214431",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214432",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214433",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214434",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "treePos":"21444",
                                                        "label": "行_4",
                                                        "icon": "Coin",
                                                        "level": 5,
                                                        "children": [
                                                            {
                                                                "treePos":"214441",
                                                                "label": "盒_1",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214442",
                                                                "label": "盒_2",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214443",
                                                                "label": "盒_3",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            },
                                                            {
                                                                "treePos":"214444",
                                                                "label": "盒_4",
                                                                "icon": "Box",
                                                                "level": 6,
                                                                "cells": []
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                        ]
                                    },
                                ]
                            },
                ]
        for i in mongodb:
            del i['_id']
            pos = i['位置'].split('/')[1:]
            i['POS'] = int(pos[6])
            result = search_cell(result,pos,i)
        if result:
            res = {'data':result}
            status = '200 OK'
        else:
            res = {"error": "没有找到对应的数据"}
            status = '403 Forbidden'
       
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(res)
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp

@bp.route('/container_cel/del/', methods=['POST'])
def del_container_data():
    """
        删除指定数据库样本
        {
            位置: 1,
            样本源编号: 'xxxxxx',
            样本源姓名: '王*',
            样本类型: 'xxxx',
            所属样本组: 'xxxxxxxxxx',
            样本量: 'xxxxx',
            入库时间: 'xxxxxxxx',
        }
        用户信息
        {
            name
        }
        1. 先加入到审批的库中，待管理员审批（样本状态:'待审批');
        2. 审批后（样本状态:'正常');
    """
    data = {}
    data['样本源编号'] = request.form['样本源编号']
    data['用户信息'] = request.form['name']
    client = MongoClient(host='localhost', port=27017)
    try:
        result = client['bioSample']['container'].find({
            '样本源编号':data['样本源编号'],
        })
        choose_data = result[0]
        del choose_data['_id']
        choose_data['用户信息'] = data['用户信息']
        choose_data['样本状态'] = '废弃审核中'
        choose_data['操作'] = '样本废弃'

        client['bioSample']['examine'].insert_one(choose_data)
        res = {"result": "上传数据成功"}
        status = "200 OK"
       
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(res)
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp

# 待入库样本查询
@bp.route('/container_cell/add/', methods=['POST'])
def add_container_cell():
    client = MongoClient(host='localhost', port=27017)
    try:
        result = client['bioSample']['collections'].find({
            '接收状态':'已完成'
        })
        data = []
        for i in result:
            del i['_id']
            data.append(i)
        res = {"result": data}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp

#样本入库审核
@bp.route('/container_cell/storage/', methods=['POST'])
def storage_container_cell():
    """
        加入数据库样本
        用户信息
        {
            name
        }
        1. 先加入到审批的库中，待管理员审批（样本状态:'待审批');
        2. 审批后（样本状态:'正常');
    """
    data = {}
    data['位置'] = request.form['位置']
    data['样本源编号'] = request.form['样本源编号']
    data['用户信息'] = request.form['name']
    client = MongoClient(host='localhost', port=27017)
    try:
        newData = {"$set":{
            '入库状态':'审核中'
        }}
        client['bioSample']['collections'].update_many({
            '样本源编号':data['样本源编号'],
        },newData)
        result = client['bioSample']['collections'].find({
            '样本源编号':data['样本源编号'],
        })
        change_data = result[0]
        del change_data['_id']
        change_data['位置'] = data['位置']
        change_data['用户信息'] = data['用户信息']
        change_data['操作'] = '样本入库'
        client['bioSample']['examine'].insert_one(change_data)
        res = {"result": 'success'}
        status = "200 OK"
    except Exception as err:
        res = {"error": "服务器错误" + str(err)}
        status = '500 ServerError'

    resp = make_response(jsonify(res))
    resp.status = status
    resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
    return resp


@bp.route('/container_cell/trans/', methods=['POST'])
def trans_contaniner_cell():
    oldData = json.loads(request.json.get('oldData'))
    newData = json.loads(request.json.get('newData'))
    if oldData['样本类型'] != '暂无' & newData['样本类型'] == '暂无':
        
        newData = {"$set":{'位置':newData['位置'][1:]}}
        # result = client['bioSample']['container'].insert_one(oldData)
        client = MongoClient(host='localhost', port=27017)
        print({'位置':oldData['位置']}, newData)
        client['bioSample']['container'].update_one({'位置':oldData['位置']}, newData)

        res = {"result": "上传数据成功"}
        status = "200 OK"
        resp = make_response(jsonify(res))
        resp.status = status
        resp.headers['ACCESS-CONTROL-ALLOW-ORIGIN'] = '*'
        return resp