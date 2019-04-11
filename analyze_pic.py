import requests
import base64

def analyze_pic(img_path):
    ak = 'RKY2ezIX4gyEyg8wOKkrUoiY'
    sk = 'SCifoqP4OQ2dz8NWp0YMaCuxHiPWmikO'
    # 根据ak和sk 获取 access_token
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}'

    ret = requests.get(host).json()

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    # 将图片转为base64 编码
    with open(img_path, mode='rb') as f:
        img_base64 = bytes.decode(base64.b64encode(f.read()))

    # 数据可以使用base64格式或者网页url
    data = {'image': img_base64}
    access_token=ret['access_token']
    url="https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token="

    ans = requests.post(url+access_token, data=data, headers=headers).text
    return ans

def get_para(ans):
    xx = ans.split(',')
    d = {'电压':'未识别','电流':'未识别','有功常数':'未识别','无功常数':'未识别','精度':'未识别','类型':'未识别','条形码':'未识别','生产厂家':'未识别','年份':'未识别'}
    def analyze_dydl(dy):
    #    解析电压
        if dy.find('×100') > 0:
            d['电压'] = '3×100'
        if dy.find('×220') > 0:
            d['电压'] = '3×220'
        if dy.find('3×15(6)') > 0:
            d['电流'] = '3×1.5(6)'
        if dy.find('3×1.5(6)') > 0:
            d['电流'] = '3×1.5(6)'

    def analyze_cs(cs):
        # 有功常数和无功常数
        c = cs[cs.find('A')+1:]
        c = c.upper()
        i = 0
        for x in c:
            i += 1
            if  'KVARHWIMP'.find(x) > 0:
                d['有功常数'] = c[0:i-1]
                break
        wgcs = ''
        for x in c[i:]:
            if x in '0123456789':
                wgcs = wgcs + x
        if len(wgcs) > 1:
            d['无功常数'] = wgcs

    def analyze(item):
        if item.find('②') >= 0 and d['精度'] is None:
            d['精度'] = '②'
        if item.find('①') >= 0:
            d['精度'] = '①'
        if item.find('型') > 0 and item.find('相') > 0 :
            d['类型'] = item
        if item.find('×') > 0 or item.find('(') > 0 or item.find(')') > 0:
            analyze_dydl(item)
            analyze_cs(item)
        if item.find('33') == 0 and len(item) == 22:
            d['条形码'] = item
        if item.find('20') > 0 and item.find('年') > 0:
            d['生产厂家'] = item[0:item.find('20')]
            d['年份'] = item[item.find('20'): item.find('年')]
    for x in xx:
        for y in x.split('"'):
            analyze(y)
    return d


if __name__ == '__main__':

    path = r"C:\Users\Administrator\Desktop\捕获3.JPG"
    rst = analyze_pic(path)
    print(rst)
    dict = get_para(rst)
    for x in dict:
        print(x, '\t', dict[x])