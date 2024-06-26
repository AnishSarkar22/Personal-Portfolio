from flask import Flask, render_template, request, flash, redirect
from flask_compress import Compress
from forms.forms import ContactForm
from flask_mail import Mail, Message
import os

app = Flask(__name__, template_folder='')
# Explicitly set the environment
app.config['ENV'] = 'development'

Compress(app)

app.secret_key = '93p7#4HLQ&qA%P7*ovcSSA'

mail_settings = {
    "MAIL_SERVER": "smtp.gmail.com",
    "MAIL_PORT": 587,
    "MAIL_USE_TLS": True,
    "MAIL_USE_SSL": False,
    "MAIL_USERNAME": 'anishsarkar282@gmail.com',
    # "MAIL_PASSWORD": os.environ.get("EMAIL_PW")
    "MAIL_PASSWORD": "rnvkewymoxxxphfz"
}

app.config.update(mail_settings)
mail = Mail(app)

@app.before_request
def before_request():
    if app.config['ENV'] == "development":
        return
    if request.is_secure:
        return

    url = request.url.replace("http://", "https://", 1)
    code = 301
    return redirect(url, code=code)
    
@app.route('/', methods=['GET', 'POST'])
def handle_contact_form():
    """Handle the contact form."""

    form = ContactForm(request.form)

    if request.method == 'POST':
        if not form.validate():
            flash('Hmmm. Something isn\'t quite right with your submission.')
            return render_template('index.html', form=form)
        else:
            """Send Email."""
            msg = Message("Website Contact Form",
                       recipients=["lillianlakeswebsite@gmail.com"],
                       sender=(form.name.data, form.email.data))
            msg.body = f"Name: {form.name.data} \n Email: {form.email.data} \n Message: {form.message.data}"
            mail.send(msg)

            """Reset form after sending email."""
            form.name.data = ""
            form.email.data = ""
            form.message.data = ""

            return render_template('index.html', form=form, success=True)

    elif request.method == 'GET':
        return render_template('index.html', form=form)
    

if __name__ == '__main__':
    app.run(debug = True)