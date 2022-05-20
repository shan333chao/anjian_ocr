

###1.拉取代码
        git clone https://gitee.com/baramongan/TrWebOCR_anjian.git

###1.修改wsl版本
        sed -i 's#/usr/lib/wsl/lib#/usr/lib/wsl/lib2#g' /etc/ld.so.conf.d/ld.wsl.conf
        cp wsl.conf /etc/wsl.conf

###3.修改wsl ubuntu 源
        sudo cp -a /etc/apt/sources.list /etc/apt/sources.list.bak
        sudo sed -i "s@http://.*archive.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
        sudo sed -i "s@http://.*security.ubuntu.com@http://repo.huaweicloud.com@g" /etc/apt/sources.list
        apt update



###4.修改Python源

        apt install python3-pip
        pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple


###4.安装docker 

4.1卸载旧版软件

        sudo apt-get remove docker docker-engine docker.io containerd runc

4.2更新源

            apt-get update

4.5安装依赖

            sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release

4.6 Docker’s official GPG key:

        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

4.7 设置docker 源

            echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

4.8 Install Docker Engine

        sudo apt-get update
        sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

4.9 查看docker engine 版本列表 选择一个

        apt-cache madison docker-ce


4.10 安装一个版本

        sudo apt-get install docker-ce=5:20.10.16~3-0~ubuntu-focal docker-ce-cli=5:20.10.16~3-0~ubuntu-focal containerd.io docker-compose-plugin

4.10.1 修改docker 源
    mkdir -p /etc/docker/
    touch /etc/docker/daemon.json
    cp -f docker_deamon.json /etc/docker/daemon.json

4.10.2 启动docker服务

    service docker start


4.11 启动一个 hello-world 镜像  测试安装效果

    docker run hello-world


###5 构建docker 环境

    docker build -t anjian_ocr:latest .

    docker run -itd --rm -p 8989:8989 --name anjian_ocr anjian_ocr:latest 


###6 运行端口同步

        ps wsl2-network.ps1

