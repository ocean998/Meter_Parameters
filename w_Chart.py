from wxpy import *
import  os

from PyQt5.QtCore import QObject, pyqtSignal

# 信号对象


class QTypeSignal(QObject):
    # 定义一个信号
    sendmsg = pyqtSignal(str, str)

    def __init__(self):
        super(QTypeSignal, self).__init__()

    def run(self,msg,msg2):
        # 发射信号
        self.sendmsg.emit(msg, msg2)
        print('sendmsg.emit',msg)
        print('sendmsg.emit',msg2)


# 好友
my_friend = None
bot = None
signal = QTypeSignal()
def login_wchat():
    global bot
    bot = Bot(cache_path=True)
    print('启动机器人', get_name())

    global my_friend
    my_friend = bot.file_helper

    @bot.register(bot.file_helper,except_self=False)
    def print_helper_msg( msg ):
        print('文件助手收到消息')
        print(msg.type)
        if msg.type == 'Text':
            signal.run('Text', msg.text)

        if msg.type == 'Picture':
            fn = os.path.abspath(os.path.dirname(__file__))
            fn = fn + '\\' + msg.file_name.split('.')[0] + '.jpg'
            print('\nfn:', fn)
            msg.get_file(save_path=fn)
            signal.run('Picture', fn)


def get_name():
    return   bot.self.name
# 发送文本
def sent_msg(msg):
    global my_friend
    my_friend.send(msg)




def logout_wchat():
    global bot
    bot.logout()
    print('关闭机器人')