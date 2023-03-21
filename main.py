from flask import Flask, render_template, request  # Import Flask and RenderTemplate and Request
app = Flask(__name__)  # Create an Instance

question_list = ['Who was the first principal?',
                 'Who is our current principal?',
                 'What is our school motto?',
                 'How many houses do we have?',
                 'What is the name of the purple house?']  # insert your questions here

answer_list = ['Mr Manogaran Suppiah', 'Mr Heng Yew Seng','Discere Servire - Non Mihi Solum', '4','Athena']  # insert your answer here

question_num = 1
message = ''
correct_answer = 0
wrong_answer = 0


@app.route('/', methods=['GET', 'POST'])  # Route the Function and allow Requests
def quizpage():  # Run the function
    global question_num, message, correct_answer, wrong_answer # Allow global scope
    if request.method == 'POST':  # Identify Request Method
        user_input = request.form['user_input']  # Gather the Post Request
        if user_input.lower() == answer_list[question_num - 1].lower(): # check answer correct or wrong
            message = 'Correct'
            correct_answer += 1
        else:
            message = 'Wrong'
            wrong_answer += 1
        
        question_num += 1 # Next question
        
    try:
      question = question_list[question_num - 1] # Get the question from the list
    except IndexError: # Raise an exception if list index out of range
      return render_template('end.html', correct_answer=correct_answer, wrong_answer=wrong_answer) # Game end if there is no more question
    return render_template('index.html', question=question,
                           question_num=question_num, message=message)

app.run(host='0.0.0.0', port=5000)  # Run the Application 
