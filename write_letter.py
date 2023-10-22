
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Optional, Type
import openai

class WriteLetterDefineInput(BaseModel):
    NAME: str = Field(
        ...,
        description="The people name you want to write to, such as professor, teacher, and so on.")

    REASON: str = Field(
        ...,
        description="The reason why you want to write letter for the recipient, such as asking for a leave or some tasks.")

class WriteLetterTool(BaseTool):
    name = "generate_the_e-mail"
    description = "Automatic generate a letter for a person you want to write to."

    def generate_letter(self,recipient_name, reason_for_writing):
        print("generating...")
        prompt = f"Dear {recipient_name},\nI am writing to you because {reason_for_writing}. Please find below the content of the letter:\n"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100
        )
        return response['choices'][0]['text']
    def _run(self, NAME, REASON):
        # You need to implement your logic to extract recipient name and reason for writing from user_input
        recipient_name = NAME
        reason_for_writing = REASON
        letter_content = self.generate_letter(recipient_name, reason_for_writing)
        return letter_content
    args_schema: Optional[Type[BaseModel]] = WriteLetterDefineInput
