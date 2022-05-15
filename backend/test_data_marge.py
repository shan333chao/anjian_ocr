import re
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
        "+16",
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
        "+34",
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
        "+292",
        0.90885
    ]
]

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
                arrdic[ocrText]=  re.findall(r"\d+\.?\d*", raw_data[i][1])[0]
                ocrText=""
        else:
            arrdic[ocrText]=re.findall(r"\d+\.?\d*", raw_data[i][1])[0]
    return arrdic
        
        
fumo_res=convert_fumo(res)


print(f"{fumo_res}")
