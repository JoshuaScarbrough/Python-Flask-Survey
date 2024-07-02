from flask import Flask, render_template, request, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey, Question


app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)



RESPONSES=[]
dummy=[]

# Changing button from get request to post request
@app.route('/')
def home_page():
    satisfaction = satisfaction_survey
    session['responses']=[]
    return render_template("base.html", satisfaction = satisfaction)

@app.route('/questions/<int:questions>', methods=["GET", "POST"])
def question_0(questions):

    # return render_template("questionOne.html", questionss=questionss, questions = questions, randName=randName )
    questions = questions
    satisfaction = satisfaction_survey
    choices = Question(satisfaction_survey.questions[questions].question).choices
    survey_question = satisfaction.questions[questions].question

    # Creates the empty sessions list
    

    if questions == len(session['responses']):
        print("success")
    else:
        print("failure")
        flash(" Invalid acces ")
        return redirect(f'/questions/{len(session['responses'])}')

    # return f"<p> {post} </P>"
    return render_template("questionOne.html", satisfaction=satisfaction, survey_question=survey_question, choices=choices, questions=questions)

@app.route('/answer/<int:questions>', methods=["POST"])
def question_answers(questions):
    questions = questions

    # session form
    jes = session['responses']
    answers=request.form['question0']
    jes.append(answers)
    session['responses'] = jes
    print(jes)

    length_questions = satisfaction_survey.questions
    qlen = len(length_questions)


    if len(session['responses']) == qlen:
        return f"Thank You, {session['responses']}"
    else: 
        return redirect(f'/questions/{len(session['responses'])}')

if __name__ == '__main__':
    app.run(debug=True)