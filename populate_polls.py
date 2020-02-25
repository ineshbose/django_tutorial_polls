import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from polls.models import Question, Choice
from datetime import datetime
from pytz import utc

def populate():
    question1_choices = [
        {"choice_text": "The sky", "votes": 5},
        {"choice_text": "Just hacking", "votes": 8},
        {"choice_text": "Not much", "votes": 2},
    ]

    questions = {"What's up?": {"choices": question1_choices, "pub_date": datetime.now()}}

    for question, question_data in questions.items():
        q = add_question(question, question_data["pub_date"])
        for c in question_data["choices"]:
            add_choice(q, c["choice_text"], c["votes"])

def add_question(question_text, pub_date):
    question = Question.objects.get_or_create(
        question_text=question_text, pub_date=pub_date)[0]
    question.save()
    return question

def add_choice(question, choice_text, votes):
    choice = Choice.objects.get_or_create(
        question=question, choice_text=choice_text, votes = votes)[0]
    choice.save()
    return choice

if __name__ == '__main__':
    populate()