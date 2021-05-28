#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import re

TARGET_TEXT = "あああああああ〒123-4567あああああ090-0987-4567あああああああああああ09012345678ああああああtest@email.com"



#TIPS:正規表現のパターンには冒頭にrをつける。これでバックスラッシュの検索も容易にできるようになる。

#郵便番号
POST_PATTERN    = r"\d{3}-\d{4}"

#メールアドレス(最初必ず英小文字のタイプ)
MAIL_PATTERN    = r"([a-z]+)@([a-z]+)\.com"

#携帯電話番号
PHONE_PATTERN   = r"\d{3}-{0,1}\d{4}-{0,1}\d{4}"


post    = re.compile(POST_PATTERN)
mail    = re.compile(MAIL_PATTERN)
phone   = re.compile(PHONE_PATTERN)


#searchメソッドは対象から最初にマッチした文字列を抽出
result  = post.search(TARGET_TEXT)
print(result)
print(result.group())

result  = mail.search(TARGET_TEXT)
print(result)
print(result.group())


#全て抽出するにはfindallを。.group()メソッドは無い
result  = phone.findall(TARGET_TEXT)
print(result)


#参照: https://miyabikno-jobs.com/it/tool-python-rechecker/



