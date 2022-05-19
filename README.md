# TrWebOCR-开源的离线OCR  

## 介绍

anjian_ocr，基于开源项目 [TrWebOCR](https://gitee.com/alisen39/TrWebOCR) 构建。  

在其基础上修改了dockerfile，便于你在docker中自己构建。 

修改了接口返回的小数精度 

添加了更适合手机端脚本调用的接口 /api/tr-run2/

修改了默认启动端口为8989

过滤了可信度为0的识别结果

![web页面](https://images.alisen39.com/20200517184619.png)  

## 特性
* 中文识别  
快速高识别率
 
* 文字检测  
支持一定角度的旋转  

* 并发请求  
由于模型本身不支持并发，但通过tornado多进程的方式，能支持一定数量的并发请求。具体并发数取决于机器的配置。


## 安装需求  
 
### 运行平台  
* ✔ Python 3.6+  
* ✔ Ubuntu 16.04
* ✔ ️Ubuntu 18.04
* ✔ CentOS 7   
* ✔ Docker   

Windows和MacOS系统下可通过构建Docker镜像来使用，暂不支持直接部署使用  
其他Linux平台暂未测试，可自行安装测试  

### 最低配置要求  
* CPU:    1核  
* 内存:    2G  
* SWAP:   2G  

## 安装说明  
### 服务器部署
1. 安装python3.7  
    推荐使用miniconda
    
2. 安装依赖包  
``` shell script
pip install -r requirements.txt
```  

3. 运行  
项目默认运行在8989端口，默认不开启gpu：  
``` shell script
python backend/main.py [--port=8989][--open_gpu=0]
# --port 指定运行时端口号 默认是8989  
# --open_gpu 是否开启gpu 默认是0(不开启），可设置为1（开启）
```

看到以下输出则代表安装成功： 
```shell script
tr 2.3.0 https://github.com/myhub/tr
Server is running: http://192.168.31.95:8989
Now version is: cpu
```   

### Docker部署  
使用 Dockerfile 构建 或者直接 Pull镜像  
```shell script
# dockerfile 构建
docker build -t anjian_ocr:latest .
    
# 运行镜像
docker run -itd --rm -p 8989:8989 --name anjian_ocr anjian_ocr:latest
```  

```shell script
# 从 dockerhub pull
docker pull mmmz/trwebocr:latest

# 运行镜像
docker run -itd --rm -p 8989:8989 --name trwebocr mmmz/trwebocr:latest 
```  
这里把容器的8989端口映射到了物理机的8989上，但如果你不喜欢映射，去掉run后面的`-p 8989:8989` 也可以使用docker的IP加`8989`来访问  

## 接口文档  
接口文档的内容放在了本项目的wiki里：  
[接口文档](https://github.com/alisen39/TrWebOCR/wiki/%E6%8E%A5%E5%8F%A3%E6%96%87%E6%A1%A3)    

## 接口调用示例  
* Python 使用File上传文件  
``` python
import requests
url = 'http://192.168.31.108:8989/api/tr-run2/'
img1_file = {
    'file': open('img1.png', 'rb')
}
res = requests.post(url=url, data={'compress': 0}, files=img1_file)
```  

* Python 使用Base64  
``` python
import requests
import base64
def img_to_base64(img_path):
    with open(img_path, 'rb')as read:
        b64 = base64.b64encode(read.read())
    return b64
    
url = 'http://192.168.31.108:8989/api/tr-run2/'
img_b64 = img_to_base64('./img1.png')
res = requests.post(url=url, data={'img': img_b64})
```



## 效果展示  

![文档识别](https://images.alisen39.com/20200501171943.png)  

![验证码识别](https://images.alisen39.com/20200501173211.png)

## 更新记录  
* 2022年01月23日  
    更新tr2.3.1版模型  
    > 模型本身支持多线程了~~现在直接可以打满CPU了！所有核！
* 2022年01月16日  
    更新接口，增加不返回图片参数

* 2020年08月17日  
    更新Dockerfile，docker镜像支持tr2.3  
    
* 2020年07月30日  
    支持启动命令选择GPU/CPU  

[更多记录 >>>](https://github.com/alisen39/TrWebOCR/blob/master/updateHistory.md)  


## License  
Apache 2.0

## 鸣谢
* 感谢 [myhub](https://github.com/myhub) 和它的开源项目[Tr](https://github.com/myhub/tr)  
* 感谢 [alisen39](https://github.com/alisen39) 和它的开源项目 [TrWebOCR](https://gitee.com/alisen39/TrWebOCR) 

## 最后  
项目在上https://gitee.com/baramongan/TrWebOCR_anjian 同步更新， 可以通过码云clone项目~   
如果你也喜欢这个项目，不妨给个star (^.^)✨