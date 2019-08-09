import os
import win32com.client as win32
import datetime
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase, MIMEMultipart
from email.utils import parseaddr, formataddr
from email.header import Header
from email import encoders

# from testFile import getPathInfo, readConfig
sys.path.append("./")
from testFile import readConfig
from testFile import getPathInfo

read_conf = readConfig.readConfig()
subject = read_conf.get_email("subject")
app = str(read_conf.get_email("app"))
address = read_conf.get_email("address")
toAddress = read_conf.get_email("toAddress")
password = read_conf.get_email("password")
smtpServer = read_conf.get_email("smtpServer")
smtpServer_host = read_conf.get_email("smtpServer_host")
mail_path = os.path.join(
    getPathInfo.get_Path().replace("\\testFile", ""), "result", "report.html"
)


class send_email:
    def outlook(self):
        olook = win32.Dispatch("%s.Application" % app)
        mail = olook.CreateItem(0)
        mail.To = address
        mail.Subject = str(datetime.datetime.now())[0:19] + "%s" % subject
        mail.Attachments.Add(mail_path, 1, 1, "myFile")
        content = """
                执行测试中....
                测试已完成！！！
                生成报告中....
                报告已生成....
                报告已邮件发送！！！
                """
        mail.Body = content
        mail.Send()

    def __format__addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, "utf-8").encode(), addr))

    def smtp(self):
        server = smtplib.SMTP_SSL(smtpServer, smtpServer_host)
        server.set_debuglevel(1)
        server.login(address, password)
        content = """
                执行测试中....
                测试已完成！！！
                生成报告中....
                报告已生成....
                报告已邮件发送！！！
                """
        msg = MIMEMultipart()
        msg["From"] = self.__format__addr("%s" % address)
        msg["To"] = self.__format__addr("%s" % toAddress)
        msg["Subject"] = Header("测试报告", "utf-8").encode()

        msg.attach(MIMEText(content, "plain", "utf-8"))

        with open(mail_path, "rb") as f:
            mime = MIMEBase("file", "html", filename="test.html")
            mime.add_header("Content-Disposition", "attachment", filename="test.html")
            mime.add_header("Content-ID", "<0>")
            mime.add_header("X-Attachment-Id", "0")
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)
        server.sendmail(address, [toAddress], msg.as_string())
        server.quit()


if __name__ == "__main__":
    print(subject)
    # send_email().outlook()
    send_email().smtp()
    print("send email ok!!!!!")
