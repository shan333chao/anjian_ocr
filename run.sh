ps -ef | grep backend/main.py | grep -v color | awk -F " " '{print $2}' |grep -v grep| xargs kill -9
echo "停止进程"
rm -rf ocr.log
echo "删除日志 等待3秒启动"
sleep 3
nohup python3 -u backend/main.py >> ./ocr.log &