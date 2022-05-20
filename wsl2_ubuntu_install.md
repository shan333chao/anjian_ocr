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

###3.1 安装ssh

        apt-get remove -y openssh-server
        apt-get install -y openssh-server
        sudo sed -i "s@#Port 22@Port 22@g" /etc/ssh/sshd_config
        sudo sed -i "s@PasswordAuthentication no@PasswordAuthentication yes@g" /etc/ssh/sshd_config
        sudo sed -i "s@#ListenAddress 0.0.0.0@ListenAddress 0.0.0.0@g" /etc/ssh/sshd_config
        sudo sed -i "s@#PermitRootLogin prohibit-password@PermitRootLogin yes@g" /etc/ssh/sshd_config
        service ssh restart

####3.1.1 映射wsl 端口到物理机

        apt install -y net-tools

        在pose人shell 中运行
        . wsl2-network.ps1

        ssh-server安装完成

        
###4.修改Python源

        apt install -y python3-pip
        pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
        


###4.安装docker 

4.1若您安装过docker，需要先删掉，之后再安装依赖:

        sudo apt-get  remove -y docker docker-engine docker.io
        sudo apt-get  install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common

4.2 信任Docker的GPG公钥::

       curl -fsSL https://repo.huaweicloud.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -

4.3 设置docker 源

        sudo add-apt-repository "deb [arch=amd64] https://repo.huaweicloud.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"

4.4 Install Docker Engine

        sudo apt-get update
        sudo apt-get install docker-ce

4.5 修改docker 源

        mkdir -p /etc/docker/
        touch /etc/docker/daemon.json
        cp -f docker_deamon.json /etc/docker/daemon.json

4.6 启动docker服务

        service docker start

###5 构建docker 环境

        docker build -t anjian_ocr:latest .

        docker run -itd --rm -p 8989:8989 --name anjian_ocr anjian_ocr:latest 


###6 运行端口同步

        . wsl2-network.ps1

