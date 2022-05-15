import re
import numpy as np 

res = [
    [
        [
            83,
            21,
            84,
            24.9,
            0
        ],
        "物理防御",
        0.95301
    ],
    [
        [
            325.5,
            21.5,
            33,
            20.6,
            0
        ],
        "+16.6",
        0.9998
    ],
    [
        [
            83,
            62.5,
            84,
            23.4,
            0
        ],
        "物理攻击",
        0.9999
    ],
    [
        [
            324,
            63.5,
            38,
            20.6,
            0
        ],
        "+34.4",
        1
    ],
    [
        [
            73,
            106.5,
            66,
            23.4,
            0
        ],
        "MaxHp",
        0.99995
    ],
    [
        [
            318.5,
            106,
            49,
            19.1,
            0
        ],
        "+292.5",
        0.90885
    ]
]
def pick_number(numstr):
    regex_val = re.findall(r"\d+\.?\d*", numstr)
    if len(regex_val) == 0:
        return 0
    else:
        np_arr=np.array(regex_val)
        return np_arr.astype(float)[0]
def convert_fumo(raw_data):
    # 下一行的高度
    nextLineHeight = 0 
    arrdic=dict()
    ocrText = ""
    for i in range(0,len(raw_data)):
        # 合并同一行的数据
        if i < len(raw_data) - 1:
            nextLineHeight = raw_data[i + 1][0][1]
            # 判断判断同一行的依据是 两段的行高差 小于 行高的一半
            if abs(raw_data[i][0][1] - nextLineHeight) < raw_data[i][0][3] / 2:
                ocrText += raw_data[i][1]
            else:
                arrdic[ocrText]=pick_number(raw_data[i][1]) 
                ocrText=""
        else:
            arrdic[ocrText]=pick_number(raw_data[i][1]) 
    return arrdic
        
        
fumo_res=convert_fumo(res)


print(f"{fumo_res}")
