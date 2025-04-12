from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def contact():
    name =request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    subject = request.form.get('subject')
    preferred  = request.form.get('preferred')
    agreement = request.form.get('agreement')
    return render_template('contact_form.html', name=name, email=email, phone=phone, message=message, subject=subject, preferred=preferred, agreement=agreement)



@app.route('/confirmation', methods = ['POST', 'GET'])
def confirm():
    return render_template('confirmation.html')



if __name__ == '__main__':
   app.run(debug = True)
