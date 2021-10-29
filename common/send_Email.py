import smtplib
import time
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from readConfig import read_config


def send_mail(attachment, content):
    print("\033[31m开始发送测试报告......")
    # 设置邮件主题
    subject = "[" + time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())) + "] " + "pcClient_UI自动化测试测试"
    # 构造一个MIMEMultipart对象代表邮件本身
    msg = MIMEMultipart()
    # HTML邮件正文
    msg.attach(MIMEText(content, 'html', 'utf-8'))
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = read_config().get_Email("sendmail")
    msg['To'] = read_config().get_Email("receivemail")

    # 添加附件
    with open(attachment, 'rb') as f:
        # MIMEBase表示附件的对象
        mime = MIMEBase('application', 'octet-stream')
        # filename是显示附件名字
        attachment_name = attachment.split("\\")[-1]
        mime.add_header('Content-Disposition', 'attachment', filename=attachment_name)
        # 获取附件内容
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        # 作为附件添加到邮件
        msg.attach(mime)
    try:
        stmp = smtplib.SMTP_SSL(host="smtp.exmail.qq.com", port=465)
        # 连接SMTP主机
        stmp.connect(host="smtp.exmail.qq.com")
        # 登录邮箱
        stmp.login(read_config().get_Email("sendmail"), read_config().get_Email("PassKey"))
        # 邮件发送
        stmp.sendmail(read_config().get_Email("sendmail"), read_config().get_Email("receivemail").split(","),
                      msg.as_string())
        # 断开SMTP连接
        stmp.quit()
        print("邮件发送——Success")
    except Exception as e:
        print("邮件发送——Fail" + str(e))
    print("----------------------------------------------------------\033[0m")