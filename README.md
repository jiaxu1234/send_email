# send_email
基于python的stmp自动发送邮件工具

python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

### Python创建 SMTP 对象语法如下：

	import smtplib

	smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

参数说明：

    host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如: runoob.com，这个是可选参数。
    port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下 SMTP 端口号为25。
    local_hostname: 如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可。 

subject: 邮件主题

text：邮件正文部分

返回值flag:True代表邮件发送成功；False发送失败。
