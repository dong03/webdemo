from dingtalkchatbot.chatbot import DingtalkChatbot, FeedLink
import time
import hmac
import urllib
import hashlib
import base64


# 获取链接,填入urlToken 和 secret
def getSIGN():
    timestamp = str(round(time.time() * 1000))
    urlToken = "https://oapi.dingtalk.com/robot/send?access_token=f69d0648104449bfecd6ae879bf0d60aa2b2713060b4949f198d7a7087b21fef"
    secret = 'SECac4b254f64e789b66f1a2ed08f84d34443d3decc8c1f43ee07a611d52b94f349'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    SignMessage = urlToken + "&timestamp=" + timestamp + "&sign=" + sign
    return SignMessage


SignMessage = getSIGN()
xiaoDing = DingtalkChatbot(SignMessage)  # 初始化机器人


def send_txt():
    """第一: 发送文本-->
    send_text(self,msg,is_at_all=False,at_mobiles=[],at_dingtalk_ids=[],is_auto_at=True)
        msg: 发送的消息
        is_at_all:是@所有人吗? 默认False,如果是True.会覆盖其它的属性
        at_mobiles:要@的人的列表,填写的是手机号
        at_dingtalk_ids:未知;文档说的是"被@人的dingtalkId（可选）"
        is_auto_at:默认为True.经过测试,False是每个人一条只能@一次,重复的会过滤,否则不然,测试结果与文档不一致
    """
    text = "Epoch[%d]: \nimg-level  sen: %.4f  spe: %.4f  f1: %.4f  acc: %.4f\navg_pixel_f1: %.4f\ncombine_f1: %.4f" % \
           (5, 0.7534, 0.7956, 0.7739, 0.7676, 0.5862, 0.9368)
    xiaoDing.send_text(text)


def send_img():
    """第二:发送图片
    send_image(self, pic_url):
        pic_url: "图片地址"
    """
    xiaoDing.send_image("http://rrd.me/gE93L")


def send_link():
    """第三:发送link
    send_link(self, title, text, message_url, pic_url='')
        title:标题    text:内容,太长会自动截取
        message_url:跳转的url  pic_url:添加的图片的url(可选)
    """
    xiaoDing.send_link(title="今天是星期8", text="牵你的手，朝朝暮暮，牵你的手，等待明天，牵你的手，走过今生，牵你的手，生生世世",
                       message_url="https://baidu.com",
                       pic_url="http://rrd.me/gE93L")

if __name__ == '__main__':
    send_txt()
