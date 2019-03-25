from wxpy import *

bot = Bot(cache_path=True)
# 获取好友
my_friend = bot.friends().search('凯哥')[0]

# 搜索信息
messages = bot.messages.search(keywords='凯哥', sender=bot.self)

for message in messages:
    print(message)

# 发送文本
my_friend.send('Hello, WeChat!')
# 发送图片



# 消息接收监听器
@bot.register()
def print_others(msg):
    # 输出监听到的消息
    print(msg)
    # 回复消息
    msg.reply("hello world")
bot.logout()

embed()
