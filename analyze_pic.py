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
    access_token = ret['access_token']
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token="

    ans = requests.post(url + access_token, data=data, headers=headers).text
    return ans


def get_para(ans):
    xx = ans.split(',')
    # print('打印逗号拆解后的参数')
    print(xx)
    d = {
        '电压': '未识别',
        '电流': '未识别',
        '有功常数': '未识别',
        '无功常数': '未识别',
        '精度': '未识别',
        '类型': '未识别',
        '条形码': '未识别',
        '生产厂家': '未识别',
        '年份': '未识别'}

    def analyze_dydl(dy):
        a = dy.find('A')
        v = dy.find('V')
        # 字符A V都找到，先是电压后是电流（三相表）
        if a > v > 0:
            d['电压'] = dy[:v] + 'V'
            d['电流'] = dy[v + 1:a] + 'A'
        # 字符A V都找到，先是电流后电压（单相表）
        if v > a > 0:
            d['电流'] = dy[:a] + 'A'
            d['电压'] = dy[a + 1:v] + 'V'

            # if dy.find('15(6)') > 0:
            #     d['电流'] = '3×1.5(6)'
            # if dy.find('1.5(6)') > 0:
            #     d['电流'] = '3×1.5(6)'
            # if dy.find('10(100)') > 0:
            #     d['电流'] = '10(100)'
            # if dy.find('60') > 0:
            #     d['电流'] = '5(60)'

    def analyze_cs(cs):
        # 有功常数和无功常数
        # c = cs[cs.find('Hz') + 2:]

        c = cs.upper()
        # c is   " ×20/380V3×15(6)A6400IMP/K图H "
        a = c.find('A')
        z = c.find('Z')
        i = c.find('I')
        if i == -1:
            i = c.find('M')
        if i == -1:
            i = c.find('P')
        if i == -1:
            i = c.find('/')
        if i == -1:
            return
        if 0 < a < i:
            d['有功常数'] = c[a + 1:i]
        if 0 < z < i:
            d['有功常数'] = c[z + 1:i]
        # for x in c[i:]:
        #     print('x is ', x)
        #     if x in '0123456789':
        #         wgcs = wgcs + x
        # if len(wgcs) > 1:
        #     d['无功常数'] = wgcs

    def analyze(item):

        if item.find('②') > 0 and (d['精度'] is None or d['精度'] == '未识别'):
            d['精度'] = '2.0'
        if item.find('①') > 0 and (d['精度'] is None or d['精度'] == '未识别'):
            d['精度'] = '1.0'

        if item.find('型') > 0 and item.find('相') > 0:
            d['类型'] = item
        if item.find('回') > 0 or item.find(
                'A') > 0 or item.find('(') > 0 or item.find(')') > 0:
            analyze_dydl(item)
            analyze_cs(item)

        if item.find('333') == 0:
            d['条形码'] = item[:22]

        if item.find('年') > 0:
            d['年份'] = item[item.find('年') - 4:item.find('年')]

        if item.find('公司') > 0:
            d['生产厂家'] = item[:item.find('公司') + 2]
    for x in xx:
        for y in x.split('"'):
            analyze(y)
    return d


def get_MDS(rstr):
    #     解析MDS图片
    xx = rstr.split(',')
    print(xx)
    d = {
        '电压': '未识别',
        '电流': '未识别',
        '有功常数': '未识别',
        '无功常数': '未识别',
        '精度': '未识别',
        '类型': '未识别',
        '条形码': '未识别',
        '生产厂家': '未识别',
        '年份': '未识别'}
    def analyze(item):
        if item.find('条形码:') >= 0:
            d['条形码'] = item.split(':')[1]

        if item.find('厂家:') >= 0:
            d['生产厂家'] = item.split(':')[1]

        if item.find('类型:') >= 0:
            d['类型'] = item.split(':')[1]

        if item.find('电流:') >= 0:
            d['电流'] = item.split(':')[1]

        if item.find('电压:') >= 0:
            d['电压'] = item.split(':')[1]

        if item.find('常数:') >= 0:
            d['有功常数'] = item.split(':')[1]

        if item.find('有功精度:') >= 0:
            d['精度'] = item.split(':')[1]

        if item.find('出厂年份:') >= 0:
            d['年份'] = item.split(':')[1]
    for x in xx:

        for y in x.split('"'):
            if len(y) > 3:
                print(y)
                analyze(y)
    return d


if __name__ == '__main__':

    path = r"C:\Users\Administrator\PycharmProjects\Meter_Parameters\190429-104759.jpg"
    rst = analyze_pic(path)
    if rst.find('条形码:') > 0:
        rst = rst.replace('"words": ', '')
        print(rst)
        dict = get_MDS(rst)
        print(dict)
    else:
        dict = get_para(rst)
    for x in dict:
        print(x, '\t', dict[x])
