#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import sendgrid
from sendgrid.helpers.mail import *

SENDGRID_API    = ""
FROM_EMAIL      = ""
TO_EMAIL        = ""


sg          = sendgrid.SendGridAPIClient(api_key=SENDGRID_API)
from_email  = Email(FROM_EMAIL)
to_email    = To(TO_EMAIL)


#件名と本文を指定
subject     = "メールの件名"
content     = Content("text/plain", "ここに本文")


mail        = Mail(from_email, to_email, subject, content)

#メール送信
response    = sg.client.mail.send.post(request_body=mail.get())







