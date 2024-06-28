from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey, Question


app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)



RESPONSES=[]
dummy=[]

@app.route('/')
def home_page():
    satisfaction = satisfaction_survey
    return render_template("base.html", satisfaction = satisfaction)

@app.route('/questions/<int:questions>')
def question_0(questions):

    # return render_template("questionOne.html", questionss=questionss, questions = questions, randName=randName )
    questions = questions
    satisfaction = satisfaction_survey
    choices = Question(satisfaction_survey.questions[questions].question).choices
    survey_question = satisfaction.questions[questions].question

    print(questions)
    if questions == len(RESPONSES):
        print("success")
    else:
        print("failure")
        flash(" Invalid acces ")
        return redirect(f'/questions/{len(RESPONSES)}')

    # return f"<p> {post} </P>"
    return render_template("questionOne.html", satisfaction=satisfaction, survey_question=survey_question, choices=choices, questions=questions)

@app.route('/answer/<int:questions>', methods=['POST'])
def question_answers(questions):
    questions = questions
    answer=request.form['question0']
    RESPONSES.append(answer)
    length_questions = satisfaction_survey.questions
    qlen = len(length_questions)

    # print(questions)

    # if questions == len(RESPONSES) - 1:
    #     print("success")
    # else:
    #     print("failure")

    if len(RESPONSES) == qlen:
        return f"Thank You, {RESPONSES}"
    else:
        return redirect(f'/questions/{len(RESPONSES)}')

if __name__ == '__main__':
    app.run(debug=True)