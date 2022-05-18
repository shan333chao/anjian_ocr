FROM python:3.7-slim
COPY . ./TrWebOCR_anjian
RUN sed -i 's#http://deb.debian.org#https://mirrors.tuna.tsinghua.edu.cn#g' /etc/apt/sources.list \
    && sed -i 's#http://security.debian.org#https://mirrors.tuna.tsinghua.edu.cn#g' /etc/apt/sources.list \
    && apt update && apt install -y libglib2.0-dev libsm6 libxrender1 libxext-dev supervisor build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && /usr/local/bin/python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple \
    && pip3 install -r ./TrWebOCR_anjian/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \
    && python3 ./TrWebOCR_anjian/install.py
EXPOSE 8089
CMD ["supervisord","-c","/TrWebOCR_anjian/supervisord.conf"]
