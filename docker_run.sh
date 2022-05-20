sed -i "s@http://\(deb\|security\).debian.org@https://mirrors.huaweicloud.com@g" /etc/apt/sources.list
apt update 
apt install -y libglib2.0-dev libsm6 libxrender1 libxext-dev supervisor build-essential libgomp1  apt-file  libxext6 libxrender-dev
rm -rf /var/lib/apt/lists/*
/usr/local/bin/python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install -r ./TrWebOCR_anjian/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
pip3 intall supervisor
python3 ./TrWebOCR_anjian/install.py