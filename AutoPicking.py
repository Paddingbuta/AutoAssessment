import requests
import time
Request_URL ="http://classes.tju.edu.cn/eams/stdElectCourse!batchOperator.action?profileId=2808"
lessonId = "446824"
Cookie = ""  # your cookie

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'Referer': 'http://classes.tju.edu.cn/eams/stdElectCourse!defaultPage.action',
    'Cookie':  "'" + Cookie + "'"
}

data={
    'optype': 'true',
    'operator0': lessonId + ':true:0'
}

while True:
    time.sleep(0.5)
    print('lessonId: ' + str(lessonId))
    sto = requests.post(Request_URL, headers = headers, data = data)
    res=str(sto.content, 'utf-8')
    # print(res)
    if '成功' in res:
        print('success!')
        continue
    elif '已经' in res:
        print('already selected')
        break
    else:
        print('failed')
        continue