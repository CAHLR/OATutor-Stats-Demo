from pydantic import BaseModel
from uuid import UUID

class Quest(BaseModel):
    problem_title: str
    problem_subtitle: str
    question_title: str
    question_subtitle: str
    student_answer: str
    correct_answer: str
    
class RequestData(BaseModel):
    context: Quest
    prompt_template: str
    bio_info: str
