# -*- coding: utf-8 -*-
from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()

    # 邮件相关信息
    message['From'] = Header('发件人', 'utf-8')
    message['To'] = Header('收件人', 'utf-8')
    message['Subject'] = Header('开题报告电子版', 'utf-8')

    # 读取文件并将文件作为附件添加到邮件消息对象中
    fileName = 'paper.pdf'
    filePath = './' + fileName
    # 创建文本内容
    text_content = MIMEText('paper：' + fileName, 'plain', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)
    with open(filePath, 'rb') as f:
        part = MIMEApplication(f.read())
        part.add_header('Content-Disposition', 'attachment', filename=fileName)
        message.attach(part)

    # 创建SMTP对象
    smtper = SMTP('smtp.qq.com')
    # 开启安全连接
    # smtper.starttls()
    sender = ''
    receivers = ['']
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    smtper.login(sender, '')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成!')


if __name__ == '__main__':
    main()