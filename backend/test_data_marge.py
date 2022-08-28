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
def convert_fumo(raw_data): 
    arrdic=[]
    for i in range(0,len(raw_data)):
        item={
            "Point":raw_data[i][0][:-1],
            "Text":raw_data[i][1],
            "Score":raw_data[i][2]
        }
        arrdic.append(item) 
    return arrdic
fumo_res=convert_fumo(res)


print(f"{fumo_res}")
