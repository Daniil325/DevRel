from ..models.sender import Sender
import smtplib as smtp
import config as auth
from email.mime.text import MIMEText

class MailSender(Sender):
    def login(self):
        self.server = smtp.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(auth.mail, auth.password)

    def send(self):
        self.server.sendmail(auth.mail, self.users, self.message.as_string())

    def create_template(self, template_name: str = 'template'):
        with open(f'MailTemplates/{template_name}.html') as file:
            self.template = file.read()

    def prepare_template(self, header: str = '', company: str = '', button: str = '', description: str = '', btn_link: str = '', link: str = ''):
        self.template = self.template.replace('#HEADER#', header)
        self.template = self.template.replace('#DESCRIPTION#', description)
        self.template = self.template.replace('#COMPANY#', company)
        self.template = self.template.replace('#BUTTON#', button)
        self.template = self.template.replace('#BUTTON_LINK#', btn_link)
        self.template = self.template.replace('#LINK#', link)

    def create_message(self,  header: str = '', company: str = '', button: str = '', description: str = '', btn_link: str = '', link: str = '', users: list = []):

        self.create_template()
        self.prepare_template(header, company, button, description, btn_link, link)
        self.users = users

        self.message = MIMEText(self.template, "html")
        self.message["From"] = auth.mail
        self.message["To"] = ', '.join(users)
        self.message["Subject"] = "Новое сообщение"


