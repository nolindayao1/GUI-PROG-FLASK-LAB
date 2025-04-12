from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def contact():
    return render_template('contact_form.html')

@app.route('/confirmation', methods=['POST'])
def confirm():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        subject = request.form['subject']
        preferred = request.form['preferred']
        agreement = request.form['agreement']

        return render_template('confirmation.html', name=name, email=email, phone=phone,
                            message=message, subject=subject, preferred=preferred, agreement=agreement)

if __name__ == '__main__':
    app.run(debug=True)
