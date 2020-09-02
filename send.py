import os
import sys
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from email.mime.base import MIMEBase
import smtplib
import transliterate
from re import *

path = os.getcwd()

def zip(exp):
	zname = path + '/f.zip'
	newzip=zipfile.ZipFile(zname,'w') #создаем архив

	for file in os.listdir(path): 
		if file.endswith("." + exp):
			fname = file.split('.')[0]
			tr = transliterate.detect_language(fname)
			if(tr == 'ru'):		
				new = transliterate.translit(fname, reversed=True)
				os.rename(file, new + '.' + exp)


	for file in os.listdir(path): 
		if file.endswith("." + exp):
			print(file)
			newzip.write(file)

	if(os.stat("f.zip").st_size == 0):
		print("В данной папке не существует такого расширения!\nПопробуйте еще раз!")
		main()

	else:
		print("Архив успешно создан!")

	newzip.close() 

def send_message():


	msg = MIMEMultipart()

	password = "zhesterstud1337"
	msg['From'] = "zhester.stud@yandex.ru"
	msg['To'] = sys.argv[2]
	msg['Subject'] = "Архив"

	filename = "f.zip"

	# Открытие PDF файла в бинарном режиме
	with open(filename, "rb") as attachment:
	    # Заголовок письма application/octet-stream
	    # Почтовый клиент обычно может загрузить это автоматически в виде вложения
	    part = MIMEBase("application", "octet-stream")
	    part.set_payload(attachment.read())

	# Шифровка файла под ASCII символы для отправки по почте 
	encoders.encode_base64(part)

	# Внесение заголовка в виде пара/ключ к части вложения
	part.add_header(
	    "Content-Disposition",
	    f"attachment; filename= {filename}",
	)
	 
	# Внесение вложения в сообщение и конвертация сообщения в строку
	msg.attach(part)
	text = msg.as_string()

	server = smtplib.SMTP_SSL('smtp.yandex.ru:465')

	server.login(msg['From'], password)
	server.sendmail(msg['From'], msg['To'], msg.as_string())
	 
	server.quit()

	print ("Успешно отправлено %s:" % (msg['To']))

def main():
	zip(sys.argv[1])
	is_valid = False
	pattern = compile('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
	is_valid = pattern.match(sys.argv[2])
	if is_valid:
		send_message()
		os.remove('f.zip')
	else:
		print('Неверный email!\n')

if __name__== "__main__":
  main()