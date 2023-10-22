
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
import openai

class NameDefineInput(BaseModel):
    NAME: str = Field(
        ...,
        description="The user name")
    USER_ID: str = Field(
        ...,
        description="The user id is usually a long data of many characters"
    )


class MailDefineInput(BaseModel):
    EMAIL_ADDRESS: str = Field(
    ...,
    description="The user's Email address end with @gmail.com"
    )
    USER_ID: str = Field(
    ...,
    description="The user id is usually a long data of many characters"
    )
        
class MailPasswordDefineInput(BaseModel):
    EMAIL_PASSWORD: str = Field(
    ...,
    description="The user's Email password, it is usually 16 characters "
    )
    USER_ID: str = Field(
    ...,
    description="The user id is usually a long data of at least 30 characters"
    )
    

class NameInputTool(BaseTool):
    name = "Get_the_user_name"
    description = "Getting the user name"

    def getuserinfo(self,user_name):
        text = "已輸入資訊\n姓名: " + user_name
        return text
    def _run(self, NAME,USER_ID):
        # You need to implement your logic to extract recipient name and reason for writing from user_input
        print("input name tool")
        username = NAME
        user_id = USER_ID
        print(user_id)
        info = self.getuserinfo(username)
        file_path = "data/" + user_id + ".txt"
        with open(file_path,'a') as f:
            f.write("username," + username + "\n")
        return info
    args_schema: Optional[Type[BaseModel]] = NameDefineInput
    
class MailInputTool(BaseTool):
    name = "Get_the_user_gmail"
    description = "Getting the Gmail"

    def getuserinfo(self,mail):
        text = "已輸入資訊" + "\nGmail: "+ mail 
        return text
    def _run(self, EMAIL_ADDRESS,USER_ID):
        # You need to implement your logic to extract recipient name and reason for writing from user_input
        print("input email tool")
        mail = EMAIL_ADDRESS
        info = self.getuserinfo(mail)
        file_path = "data/" + user_id + ".txt"
        with open(file_path,'a') as f:
            f.write("gmail," + mail + "\n")
        return info
    args_schema: Optional[Type[BaseModel]] = MailDefineInput

class MailPasswordInputTool(BaseTool):
    name = "Get_the_user_gmail_password"
    description = "Getting the Gmail Password"

    def getuserinfo(self,password,user_id):
        text = "已輸入資訊" + "\nPassword: "+ password
        
        return text
    def _run(self, EMAIL_PASSWORD,USER_ID):
        # You need to implement your logic to extract recipient name and reason for writing from user_input
        print("input email tool")
        password = EMAIL_ADDRESS
        user_id = USER_ID
        info = self.getuserinfo(mail,user_id)
        file_path = "data/" + user_id + ".txt"
        with open(file_path,'a') as f:
            f.write("password" + "," + password + "\n")
        return info
    args_schema: Optional[Type[BaseModel]] = MailPasswordDefineInput
