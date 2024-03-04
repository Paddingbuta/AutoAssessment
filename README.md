# AutoAssessment
- 妈妈再也不用担心我抢不到四史啦

## 自动评教
- 首先修改学号和密码
```
# 在代码中写入你的账户&密码
your_id = 'xxxx'
your_password = 'xxxx'
```
- 运行
```
pip install selenium
python main.py
```
- 打开界面后有5秒钟的时间手动输入验证码，输入完成后不要点击登录

## 自动选课
- 在浏览器控制台抓取信息后运行
```
Request_URL = ""
lessonId = ""
Cookie = ""  # your cookie
```
