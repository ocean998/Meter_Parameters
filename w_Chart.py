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
    print('启动机器人')
    global my_friend
    my_friend = bot.friends().search('凯哥')[0]

    @bot.register()
    def print_messages( msg ):
        print(msg)
        print(msg.text)
        print(msg.type)
        print(msg.file_name)

        if msg.type == 'Picture':
            fn = os.path.abspath(os.path.dirname(__file__))
            fn = fn + '\\'+msg.file_name
            msg.get_file(save_path=fn)
            signal.run('Picture',fn)
    # 堵塞线程，并进入 Python 命令行

    # embed()
    print('堵塞线程，并进入 Python 命令行')


# 发送文本
def sent_msg(msg):
    global my_friend
    my_friend.send(msg)




def logout_wchat():
    global bot
    bot.logout()
    print('关闭机器人')