from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import Quest, RequestData
import requests
import re

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# uvicorn main:app

API_KEY = ""

def generate_gpt_prompt(quest: Quest, prompt_template: str, bio_info: str):

    template = clean_up_null_values(quest, prompt_template, bio_info)

    p_title = quest.problem_title
    p_subtitle = quest.problem_subtitle
    q_title = quest.question_title
    q_subtitle = quest.question_subtitle
    stu_ans = quest.student_answer
    cor_ans = quest.correct_answer

    template = template.format(
        problem_title = p_title, 
        problem_subtitle = p_subtitle,
        question_title = q_title,
        question_subtitle = q_subtitle,
        student_answer = stu_ans,
        correct_answer = cor_ans,
        bio_info = bio_info
    )

    return template

def clean_up_null_values(quest: Quest, template: str, bio_info: str):

    p_title_is_null = quest.problem_title is None or len(quest.problem_title) == 0
    template = remove_wrappers(template, "problem_title", p_title_is_null)

    p_subtitle_is_null = quest.problem_subtitle is None or len(quest.problem_subtitle) == 0
    template = remove_wrappers(template, "problem_subtitle", p_subtitle_is_null)

    q_title_is_null = quest.question_title is None or len(quest.question_title) == 0
    template = remove_wrappers(template, "question_title", q_title_is_null)

    q_subtitle_is_null = quest.question_subtitle is None or len(quest.question_subtitle) == 0
    template = remove_wrappers(template, "question_subtitle", q_subtitle_is_null)

    stud_ans_is_null = quest.student_answer is None or len(quest.student_answer) == 0
    template = remove_wrappers(template, "student_answer", stud_ans_is_null)

    cor_ans_is_null = quest.correct_answer is None or len(quest.correct_answer) == 0
    template = remove_wrappers(template, "correct_answer", cor_ans_is_null)

    bio_is_null = bio_info is None or len(bio_info) == 0
    template = remove_wrappers(template, "bio_info", bio_is_null)

    return template

def remove_wrappers(template, parameter, parameter_is_null):

    start_index = template.rfind("<", 0, template.find(parameter))
    end_index = template.find(">", template.find(parameter)) + 1

    if start_index != -1 and end_index != 0:
        if parameter_is_null:
            if template[end_index:end_index+1] == " ":
                end_index += 1
            return template[:start_index] + template[end_index:]
        else:
            return template[:start_index] + template[start_index+1:end_index-1] + template[end_index:]
    else:
        return template

def reformat_hint(hint: str):
    hint = hint.lstrip('\n')
    prefix = "hint:"
    if hint.lower().startswith(prefix):
        hint = hint[len(prefix):].lstrip()
    pattern = r'[^\$]\$([^\$]+)\$[^\$]'
    replacement = r' $$\1$$ '
    hint = re.sub(pattern, replacement, hint)
    return hint

@app.get("/")
async def root():
    return {"message": "hello"}

@app.post("/get_hint")
def test_question(request_data: RequestData):
    quest = request_data.quest
    prompt_template = request_data.prompt_template
    bio_info = request_data.bio_info
    gpt_prompt = generate_gpt_prompt(quest, prompt_template, bio_info)
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant providing hints to a student."},
            {"role": "user", "content": gpt_prompt}
        ]
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    response = response.json()
    hint = ""
    if 'choices' in response and len(response['choices']) > 0:
        hint = reformat_hint(response['choices'][0]['message']['content'])
    return {"hint": hint}
